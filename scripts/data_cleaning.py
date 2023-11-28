import numpy as np
import pandas as pd

def clean_df_usagers(df):
    df_usagers = df
    df_usagers["grav"].replace({2: 4, 4: 2}, inplace=True)
    df_usagers["sexe"].replace({1: "homme", 
                                2: "femme", 
                                -1: np.nan}, 
                                inplace=True)
    df_usagers["catu"].replace({1: "conducteur", 
                                2: "passager", 
                                3: "piéton", 
                                -1: np.nan}, inplace=True)
    df_usagers["trajet"].replace({-1: np.nan, 
                                    0: np.nan, 
                                    1: "domicile-travail",
                                    2: "domicile-école",
                                    3: "courses-achats",
                                    4: "utilisation pro",
                                    5: "promenade-loisirs",
                                    9: "autre"},
                                    inplace=True)
    df_usagers["etatp"].replace({-1: np.nan,
                                    1: "seul",
                                    2: "accompagne",
                                    3: "en groupe"},
                                    inplace=True)
    df_usagers["actp"].replace({"-1": np.nan,
                                "0": np.nan,
                                "1": "sens véhicule heurtant",
                                "2": "sens inverse du véhicule",
                                "3": "traversant",
                                "4": "masqué",
                                "5": "jouant - courant",
                                "6": "avec animal",
                                "9": "autre",
                                "A": "monte/descend du véhicule", 
                                "B": np.nan}, inplace=True)
    df_usagers["etatp"].replace({"-1": np.nan,
                                    1: "seul",
                                    2: "accompagné",
                                    3: "en groupe"})
    return df_usagers

def clean_df_caracs(df):

    df_caracs = df

    # On modifie le nom de la variable Accident_Id 
    # pour faciliter la jointure tout à l'heure

    df_caracs.rename(columns={"Accident_Id": "Num_Acc"}, inplace=True)

    df_caracs['heure'] = pd.to_datetime(df_caracs['hrmn'], format='%H:%M').dt.time

    df_caracs['lat'] = df_caracs['lat'].str.replace(',', '.').astype(float)
    df_caracs['long'] = df_caracs['long'].str.replace(',', '.').astype(float)

    df_caracs["agg"].replace({1: "hors agglo",
                             2: "agglo"},
                             inplace=True)

    df_caracs.replace(-1, np.NaN, inplace=True)

    return df_caracs

def clean_df_lieux(df):

    df_lieux = df

    df_lieux["catr"] = df_lieux["catr"].replace(1, "autoroute")
    df_lieux["catr"] = df_lieux["catr"].replace(2, "route nationale")
    df_lieux["catr"] = df_lieux["catr"].replace(3, "route departementale")
    df_lieux["catr"] = df_lieux["catr"].replace(4, "voie communale")
    df_lieux["catr"] = df_lieux["catr"].replace(5, "hors réseau public")
    df_lieux["catr"] = df_lieux["catr"].replace(6, "parc de stationnement")
    df_lieux["catr"] = df_lieux["catr"].replace(7, "route de métropole urbaine")
    df_lieux["catr"] = df_lieux["catr"].replace(9, "autre")

    df_lieux["circ"] = df_lieux["circ"].replace(-1, np.nan)
    df_lieux["circ"] = df_lieux["circ"].replace(1, "chaussée unidirectionnelle")
    df_lieux["circ"] = df_lieux["circ"].replace(2, "chausée bidirectionnelle")
    df_lieux["circ"] = df_lieux["circ"].replace(3, "chaussée séparée")
    df_lieux["circ"] = df_lieux["circ"].replace(4, "avec voies d’affectation variable")

    df_lieux["vosp"] = df_lieux["vosp"].replace(-1, np.nan)
    df_lieux["vosp"] = df_lieux["vosp"].replace(0, np.nan)
    df_lieux["vosp"] = df_lieux["vosp"].replace(1, "piste_cyclable")
    df_lieux["vosp"] = df_lieux["vosp"].replace(2, "bande cyclable")
    df_lieux["vosp"] = df_lieux["vosp"].replace(3, "voie réservée")

    df_lieux["vosp"] = df_lieux["vosp"].replace(-1, np.nan)
    df_lieux["vosp"] = df_lieux["vosp"].replace(1, "partie rectiligne")
    df_lieux["vosp"] = df_lieux["vosp"].replace(2, "courbe gauche" )
    df_lieux["vosp"] = df_lieux["vosp"].replace(3, "courbe à droite")
    df_lieux["vosp"] = df_lieux["vosp"].replace(4, "courbe en S")

    df_lieux["larrout"]=df_lieux["larrout"].replace(-1,np.nan)

    df_lieux["surf"] = df_lieux["surf"].replace(-1, np.nan)
    df_lieux["surf"] = df_lieux["surf"].replace(1, "normale")
    df_lieux["surf"] = df_lieux["surf"].replace(2, "mouillée")
    df_lieux["surf"] = df_lieux["surf"].replace(3, "flaque")
    df_lieux["surf"] = df_lieux["surf"].replace(4, "inondée")
    df_lieux["surf"] = df_lieux["surf"].replace(5, "enneigée")
    df_lieux["surf"] = df_lieux["surf"].replace(6, "boue")
    df_lieux["surf"] = df_lieux["surf"].replace(7, "verglacée")
    df_lieux["surf"] = df_lieux["surf"].replace(8, "corps gras")
    df_lieux["surf"] = df_lieux["surf"].replace(9, "autre")

    df_lieux["infra"] = df_lieux["infra"].replace(-1, np.nan)
    df_lieux["infra"] = df_lieux["infra"].replace(0, np.nan)
    df_lieux["infra"] = df_lieux["infra"].replace(1, "tunnel")
    df_lieux["infra"] = df_lieux["infra"].replace(2, "pont")
    df_lieux["infra"] = df_lieux["infra"].replace(3, "bretelle")
    df_lieux["infra"] = df_lieux["infra"].replace(4, "voie ferrée")
    df_lieux["infra"] = df_lieux["infra"].replace(5, "carrefour aménagé")
    df_lieux["infra"] = df_lieux["infra"].replace(6, "zone piétonne")
    df_lieux["infra"] = df_lieux["infra"].replace(7, "zone de péage")
    df_lieux["infra"] = df_lieux["infra"].replace(8, "chantier")
    df_lieux["infra"] = df_lieux["infra"].replace(9, "autre")

    df_lieux["situ"] = df_lieux["situ"].replace(-1, np.nan)
    df_lieux["situ"] = df_lieux["situ"].replace(0, np.nan)
    df_lieux["situ"] = df_lieux["situ"].replace(1, "chaussée")
    df_lieux["situ"] = df_lieux["situ"].replace(2, "bande d'arrêt d'urgence")
    df_lieux["situ"] = df_lieux["situ"].replace(3, "acottement")
    df_lieux["situ"] = df_lieux["situ"].replace(4, "trottoir")
    df_lieux["situ"] = df_lieux["situ"].replace(5, "piste cyclable")
    df_lieux["situ"] = df_lieux["situ"].replace(6, "voie spéciale")
    df_lieux["situ"] = df_lieux["situ"].replace(7, np.nan)
    df_lieux["situ"] = df_lieux["situ"].replace(8, "autre")

    # VMA indique la vitesse maximale autorisée. Lse vitesses supérieures à 130 sont
    # sont donc des erreurs. Puisqu'il n'existe pas d'autre base recensant les vitesses
    # (ce qui permettrait d'imputer les bonnes valeurs à l'aide d'un merge)
    # on les remplace par des NaN
    # Les valeurs très faibles comme 1 sont suspectes, mais dans le doute il est préférable
    # de les conserver

    df_lieux.loc[df_lieux['vma'] > 130, 'vma'] = np.nan
    df_lieux["vma"] = df_lieux["vma"].replace(-1, np.nan)

    return df_lieux

def clean_df_vehicules(df):

    df_vehicules = df

    df_vehicules["senc"] = df_vehicules["senc"].replace(-1, np.nan)
    df_vehicules["catv"] = df_vehicules["catv"].replace(0, np.nan)
    df_vehicules["senc"] = df_vehicules["senc"].replace(-1, np.nan)

    df_vehicules["obs"] = df_vehicules["obs"].replace(-1, np.nan)

    df_vehicules["obsm"] = df_vehicules["obsm"].replace(-1, np.nan)

    df_vehicules["choc"] = df_vehicules["choc"].replace(-1, np.nan)

    df_vehicules["manv"] = df_vehicules["manv"].replace(-1, np.nan)
    df_vehicules["manv"] = df_vehicules["manv"].replace(0, np.nan)

    df_vehicules["motor"] = df_vehicules["motor"].replace(-1, np.nan)
    df_vehicules["motor"] = df_vehicules["motor"].replace(0, np.nan)

    return df_vehicules