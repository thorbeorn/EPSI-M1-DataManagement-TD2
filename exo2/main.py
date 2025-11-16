import pandas as pd
import re

CSVpath = 'Td2Exercice2.csv'
regex_valid_mail = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
regex_nom_valide = r"^[A-ZÉÈÊËÀÂÄÎÏÔÖÛÜ][a-zéèêëàâäîïôöûüç-]+ [A-ZÉÈÊËÀÂÄÎÏÔÖÛÜ][a-zéèêëàâäîïôöûüç\- ]+$"

def load_data(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def main():
    df = load_data(CSVpath)

    # invalid_emails = df.loc[~df["Email"].str.match(regex_valid_mail, na=False), "Email"]
    # print(invalid_emails)
    df["email_valide"] = df["Email"].str.match(regex_valid_mail, na=False)

    df["Nom_Complet"] = (
        df["Nom_Complet"]
        .str.replace(r"[.,;:_]+", " ", regex=True)  
        .str.replace(r"\s+", " ", regex=True)       
        .str.strip()                                
    )
    df["Nom_Complet"] = df["Nom_Complet"].str.replace(
        r"^(\w+)\s+(\w+)$", lambda m: m.group(2) + " " + m.group(1)
        if "," in m.string else m.group(0), regex=True
    )
    df["Nom_Complet"] = df["Nom_Complet"].str.replace(
        r"\b(\w)(\w*)\b",
        lambda m: m.group(1).upper() + m.group(2).lower(),
        regex=True
    )
    df["Nom_Valide"] = df["Nom_Complet"].str.match(regex_nom_valide, na=False)

    df["Tel_Clean"] = df["Telephone_FR"].str.replace(r"\D", "", regex=True)
    df["Tel_Clean"] = df["Tel_Clean"].str.replace(
        r"^(?:0033|33)0?(\d{9})$",
        r"0\1",
        regex=True
    )
    df["Tel_Clean"] = df["Tel_Clean"].str.slice(0, 10)
    df["Tel_Clean"] = df["Tel_Clean"].str.replace(
        r"^(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})$",
        r"\1 \2 \3 \4 \5",
        regex=True
    )
    df["Tel_valide"] = (df["Tel_Clean"].str.replace(r"\s+", "", regex=True).str.fullmatch(r"\d{10}", na=False))
    
    print(df)

main()