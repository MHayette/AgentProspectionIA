import os
import pandas as pd


def exporter_excel(agences):

    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(agences)

    df.to_excel(
        "data/agences.xlsx",
        index=False
    )

    print("Fichier Excel créé avec succès")