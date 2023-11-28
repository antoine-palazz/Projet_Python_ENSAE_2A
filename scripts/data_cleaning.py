def clean_df_usagers(df_usagers):
    df_usagers["grav"].replace({2: 4, 4: 2}, inplace=True)
    df_usagers["sexe"].replace({1: "homme", 
                                2: "femme", 
                                -1: np.NaN}, 
                                inplace=True)
    df_usagers["catu"].replace({1: "conducteur", 
                                2: "passager", 
                                3: "piéton", 
                                -1: np.NaN}, inplace=True)
    df_usagers["trajet"].replace({-1: np.NaN, 
                                    0: np.NaN, 
                                    1: "domicile-travail",
                                    2: "domicile-école",
                                    3: "courses-achats",
                                    4: "utilisation pro",
                                    5: "promenade-loisirs",
                                    9: "autre"},
                                    inplace=True)
    df_usagers["etatp"].replace({-1: np.NaN,
                                    1: "seul",
                                    2: "accompagne",
                                    3: "en groupe"},
                                    inplace=True)
    df_usagers["actp"].replace({"-1": np.NaN,
                                "0": np.NaN,
                                "1": "sens véhicule heurtant",
                                "2": "sens inverse du véhicule",
                                "3": "traversant",
                                "4": "masqué",
                                "5": "jouant - courant",
                                "6": "avec animal",
                                "9": "autre",
                                "A": "monte/descend du véhicule", 
                                "B": np.NaN}, inplace=True)
    df_usagers["etatp"].replace({"-1": np.NaN,
                                    1: "seul",
                                    2: "accompagné",
                                    3: "en groupe"})
    return df_usagers

def clean_df_caracs(df_caracs):
