import requests
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os
import argparse

env_file = find_dotenv()
print("Using dot env file: \033[1m{}\033[0m".format(env_file))
load_dotenv(env_file)

ACTIVATION_ID = os.getenv("ACTIVATION_ID")
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
ABTEILUNG = os.getenv("ABTEILUNG")
UTOKEN = os.getenv("UTOKEN")

ALL_PEOPLE_URL = "https://fireplanapi.azurewebsites.net/api/PersonalNamenV2"
DEVICES_URL = "https://fireplanapi.azurewebsites.net/api/AppDevices/"

ALL_PEOPLE = None

def get_people():
    global ALL_PEOPLE
    response = requests.get(ALL_PEOPLE_URL, headers={"utoken": UTOKEN}).json()
    ALL_PEOPLE = pd.DataFrame(response)

def generate_code(personal_number):
    body = {
        "userpin": 0,
        "registerid": ACTIVATION_ID,
        "connstring": CONNECTION_STRING,
        "abteilung": ABTEILUNG,
        "personalid": personal_number
    }
    response = requests.post(DEVICES_URL + ACTIVATION_ID, json=body)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fireplan Code Generator")
    parser.add_argument("-p", "--personalnummer", type=str, help="Die persönliche Nummer für die Code-Generierung")
    args = parser.parse_args()

    print("###########################")
    print("# Fireplan Code Generator #")
    print("###########################")

    print("Using registration id: \033[1m{}\033[0m".format(ACTIVATION_ID))

    # Wenn eine Personalnummer als Argument übergeben wurde, direkt Code generieren
    if args.personalnummer:
        personal_number = args.personalnummer
        print("Es wird ein neuer Code für \033[1m{}\033[0m generiert....".format(personal_number))
    else:
        # Ohne Argument: Lade die Liste und frage nach der Personalnummer
        print("Alle Feuerwehrleute:")
        get_people()
        print(ALL_PEOPLE[['PersonalNr', 'DisplayName']].to_string(index=False, header=False))
        print("Für welche persönliche Nummer soll ein Code generiert werden?")
        personal_number = input("Bitte Nummer eingeben: ")
        print("Es wird ein neuer Code für \033[1m{}\033[0m generiert....".format(person['DisplayName'].values[0]))

    code = generate_code(personal_number)
    print("Code: \033[1m{}\033[0m".format(code))
