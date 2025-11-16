import pandas as pd
import re

PATHS = {
    "csv": "Td2Exercice2.csv"
}

regex_Mail_Valid = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
regex_Nom_Valid = r"^[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+(?:[- ][A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+)*\s+(?:[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+|(?:de|du|des|le|la|les|d')\s+[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+(?:[- ][A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+)*)$"
regex_Phone_Valid = r"^0[1-9](?:\s\d{2}){4}$"

def load_CSV_To_Dataframe(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")

def dataframe_Validate_Flag_By_Regex(dataframe, column, regex):
    dataframe[column + "_validate"] = dataframe[column].str.match(regex, na=False)
    print()
    return dataframe
def string_Validity_And_Formatting(dataframe, column):
    dataframe[column] = dataframe[column].str.replace(r"[.,;:_]+", " ", regex=True).str.replace(r"\s+", " ", regex=True).str.strip()
    dataframe[column] = dataframe[column].str.replace(r"^(\w+)\s+(\w+)$", lambda m: m.group(2) + " " + m.group(1) if "," in m.string else m.group(0), regex=True)
    dataframe[column] = dataframe[column].str.replace(r"\b(\w)(\w*)\b", lambda m: m.group(1).upper() + m.group(2).lower(), regex=True)
    return dataframe
def phone_Validity_And_Formatting(dataframe, column):
    dataframe[column] = dataframe[column].str.replace(r"\D", "", regex=True)
    dataframe[column] = dataframe[column].str.replace(r"^(?:0033|33)0?(\d{9})$", r"0\1", regex=True)
    dataframe[column] = dataframe[column].str.slice(0, 10)
    dataframe[column] = dataframe[column].str.replace(r"^(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})$", r"\1 \2 \3 \4 \5", regex=True)
    return dataframe

def main():
    dataframe = load_CSV_To_Dataframe(PATHS["csv"])

    print("##########List of invalid mail##########")
    invalid_emails = dataframe.loc[~dataframe["Email"].str.match(regex_Mail_Valid, na=False), "Email"]
    print(invalid_emails)

    dataframe = dataframe_Validate_Flag_By_Regex(dataframe, "Email", regex_Mail_Valid)
    dataframe = string_Validity_And_Formatting(dataframe, "Nom_Complet")
    dataframe = dataframe_Validate_Flag_By_Regex(dataframe, "Nom_Complet", regex_Nom_Valid)

    dataframe = phone_Validity_And_Formatting(dataframe, "Telephone_FR")
    dataframe = dataframe_Validate_Flag_By_Regex(dataframe, "Telephone_FR", regex_Phone_Valid)
    
    print("##########dataframe processed##########")
    print(dataframe)

if __name__ == "__main__":
    main()