# Fireplan Code Generator

Code generator for FirePlan App access. This is useful to not have to start FirePlan if someone needs a new access code.

## Setup
Copy `.env.example` to `.env` and change the values inside. You can get the MS SQL Connection string and the utoken from the network traffic while running Fireplan. Proxyman and Wireshark are useful tools for that. The utoken seems to be valid forever

Next install the Python requirements with
```
pip install -r requirements.txt
```

## Usage
Run the tool with
```
python3 generator.py
```

Then you get a list of all people in Fireplan you can generate a code for. Enter the user id of that person. A new code gets generated that you can send that person. Please use only for people that are in the same Abteilung you enterd in `.env`.
