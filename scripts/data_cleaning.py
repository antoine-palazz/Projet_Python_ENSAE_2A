import numpy as np
import pandas as pd

def clean_df_usagers(df):
    df_usagers = df.copy()

    df_usagers["sexe"].replace({
        1: "homme",
        2: "femme",
        -1: np.nan
    }, inplace=True)

    df_usagers["catu"].replace({
        1: "conducteur",
        2: "passager",
        3: "piéton",
        -1: np.nan
    }, inplace=True)

    df_usagers["trajet"].replace({
        -1: np.nan,
        0: np.nan,
        1: "domicile-travail",
        2: "domicile-école",
        3: "courses-achats",
        4: "utilisation pro",
        5: "promenade-loisirs",
        9: "autre"
    }, inplace=True)

    df_usagers["actp"].replace({
        "-1": np.nan,
        "0": np.nan,
        "1": "sens véhicule heurtant",
        "2": "sens inverse du véhicule",
        "3": "traversant",
        "4": "masqué",
        "5": "jouant - courant",
        "6": "avec animal",
        "9": "autre",
        "A": "monte/descend du véhicule",
        "B": np.nan
    }, inplace=True)

    df_usagers["etatp"].replace({
        "-1": np.nan,
        1: "seul",
        2: "accompagné",
        3: "en groupe"
    }, inplace=True)

    df_usagers.replace(-1, np.NaN, inplace=True)

    return df_usagers

def clean_df_caracs(df):

    df_caracs = df.copy()

    # On modifie le nom de la variable Accident_Id 
    # pour faciliter la jointure tout à l'heure

    df_caracs.rename(columns={"Accident_Id": "Num_Acc"}, inplace=True)

    df_caracs['heure'] = pd.to_datetime(df_caracs['hrmn'], format='%H:%M').dt.time
    
    df_caracs['lum'].replace({
        1: "plein jour",
        2: "crépuscule/aube"
        3: "nuit sans éclairage public",
        4: "nuit avec éclairage public non allumé",
        5: "nuit avec éclairage public allumé"
    })

    df_caracs['lat'] = df_caracs['lat'].str.replace(',', '.').astype(float)
    df_caracs['long'] = df_caracs['long'].str.replace(',', '.').astype(float)

    df_caracs["agg"].replace({
        1: "hors agglo",
        2: "agglo"
    }, inplace=True)

    df_caracs['int'].replace({
        1: "hors intersection",
        2: "intersection en X",
        3: "intersection en T",
        4: "intersection en Y",
        5: "intersection à +4 branches",
        6: "giratoire",
        7: "place",
        8: "passage à niveau",
        9: "autre"
    }, inplace=True)

    df_caracs['atm'].replace({
        -1: np.nan,
        1: "normale",
        2: "pluie légère",
        3: "pluie forte",
        4: "neige/grêle",
        5: "brouillard/fumée",
        6: "vent fort/tempête",
        7: "temps éblouissant",
        8: "temps couvert",
        9: "autre"
    }, inplace=True)

    df_caracs['col'].replace({
        -1: np.nan,
        1: "2 véhicules - frontale",
        2: "2 véhicules - par l'arrière",
        3: "2 véhicules - par le côté",
        4: "3+ véhicules - en chaîne",
        5: "3+ véhicules - collisions multiples",
        6: "autre collision",
        7: "sans collision"
    }, inplace=True)

    df_caracs.replace(-1, np.NaN, inplace=True)

    return df_caracs


def clean_df_lieux(df):
    df_lieux = df.copy()

    df_lieux["catr"].replace({
        1: "autoroute",
        2: "route nationale",
        3: "route departementale",
        4: "voie communale",
        5: "hors réseau public",
        6: "parc de stationnement",
        7: "route de métropole urbaine",
        9: "autre"
    }, inplace=True)

    df_lieux["circ"].replace({
        -1: np.nan,
        1: "chaussée unidirectionnelle",
        2: "chausée bidirectionnelle",
        3: "chaussée séparée",
        4: "avec voies d’affectation variable"
    }, inplace=True)

    df_lieux["vosp"].replace({
        -1: np.nan,
        0: np.nan,
        1: "piste cyclable",
        2: "bande cyclable",
        3: "voie réservée"
    }, inplace=True)

    df_lieux["plan"].replace({
        -1: np.nan,
        1: "partie rectiligne",
        2: "en courbe à gauche",
        3: "en courbe à droite",
        4: 'en "S"'
    }, inplace=True)

    df_lieux["larrout"].replace(-1, np.nan, inplace=True)

    df_lieux["surf"].replace({
        -1: np.nan,
        1: "normale",
        2: "mouillée",
        3: "flaque",
        4: "inondée",
        5: "enneigée",
        6: "boue",
        7: "verglacée",
        8: "corps gras",
        9: "autre"
    }, inplace=True)

    df_lieux["infra"].replace({
        -1: np.nan,
        0: np.nan,
        1: "tunnel",
        2: "pont",
        3: "bretelle",
        4: "voie ferrée",
        5: "carrefour aménagé",
        6: "zone piétonne",
        7: "zone de péage",
        8: "chantier",
        9: "autre"
    }, inplace=True)

    df_lieux["situ"].replace({
        -1: np.nan,
        0: np.nan,
        1: "chaussée",
        2: "bande d'arrêt d'urgence",
        3: "acottement",
        4: "trottoir",
        5: "piste cyclable",
        6: "voie spéciale",
        7: np.nan,
        8: "autre"
    }, inplace=True)

    # VMA indique la vitesse maximale autorisée. Lse vitesses supérieures à 130 sont
    # sont donc des erreurs. Puisqu'il n'existe pas d'autre base recensant les vitesses
    # (ce qui permettrait d'imputer les bonnes valeurs à l'aide d'un merge)
    # on les remplace par des NaN
    # Les valeurs très faibles comme 1 sont suspectes, mais dans le doute il est préférable
    # de les conserver

    df_lieux.loc[df_lieux['vma'] > 130, 'vma'] = np.nan
    df_lieux["vma"].replace(-1, np.nan, inplace=True)

    df_lieux["nbv"] = df_lieux["nbv"].replace({"#ERREUR": np.nan}).astype(float).replace({-1: np.nan, 0: np.nan})

    df_lieux.replace(-1, np.NaN, inplace=True)

    return df_lieux


def clean_df_vehicules(df):
    df_vehicules = df.copy()

    df_vehicules["senc"].replace({
        -1: np.nan
    }, inplace=True)

    df_vehicules["catv"].replace({
        0: np.nan
    }, inplace=True)

    df_vehicules["obs"].replace({
        -1: np.nan
    }, inplace=True)

    df_vehicules["obsm"].replace({
        -1: np.nan
    }, inplace=True)

    df_vehicules["choc"].replace({
        -1: np.nan
    }, inplace=True)

    df_vehicules["manv"].replace({
        -1: np.nan,
        0: np.nan
    }, inplace=True)

    df_vehicules["motor"].replace({
        -1: np.nan,
        0: np.nan
    }, inplace=True)

    df_vehicules.replace(-1, np.NaN, inplace=True)

    return df_vehicules
