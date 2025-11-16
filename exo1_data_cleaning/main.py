import pandas as pd
import unicodedata

PATHS = {
    "csv": "products.csv"
}

def load_CSV_To_Dataframe(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")
def remove_accents(text):
    if isinstance(text, str):
        return ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )
    return text

def uniqueness(dataframe, subset=None, keep='first', inplace=False, ignore_index=False):
    return dataframe.drop_duplicates(subset=subset, keep=keep, inplace=inplace, ignore_index=ignore_index)
def completeness(dataframe):
    dataframe_Temp = dataframe.dropna(subset=['price'], inplace=False)
    dataframe_Temp['stock_quantity'] = dataframe_Temp['stock_quantity'].fillna(0)
    return dataframe_Temp
def validity_And_Formatting_Price(dataframe):
    dataframe['price'] = (
        dataframe['price']
        .str.replace('€', '', regex=False)
        .str.replace(',', '', regex=False)
        .astype(float)
    )
    return dataframe
def validity_Stock_Quantity(dataframe):
    dataframe['stock_quantity'] = dataframe['stock_quantity'].apply(lambda x: x if x >= 0 else 0)
    dataframe['stock_quantity'] = dataframe['stock_quantity'].astype(int)
    return dataframe
def consistency(dataframe):
    dataframe['category'] = dataframe['category'].apply(remove_accents).str.lower()
    return dataframe
def timeliness(dataframe):
    dataframe['date_added'] = pd.to_datetime(dataframe['date_added'].copy(), errors='coerce')
    return dataframe[dataframe['date_added'] < '2024-01-01']

def main():
    dataframe = load_CSV_To_Dataframe(PATHS['csv'])

    if dataframe is not None:
        print("\n########Jeu de données initial :########")
        print(dataframe)
        print(dataframe.info())
        print(dataframe.describe())

        dataframe = uniqueness(dataframe)
        dataframe = completeness(dataframe)
        dataframe = validity_And_Formatting_Price(dataframe)
        dataframe = validity_Stock_Quantity(dataframe)
        dataframe = consistency(dataframe)

        print("\n########Jeu de données périmés :########")
        expired_products = timeliness(dataframe)
        print(f"\nNombre total de produits périmés: {len(expired_products)}")
        if not expired_products.empty:
            print(expired_products[['product_name', 'date_added']])

        print("\n########Jeu de données après nettoyage :########")
        print(dataframe)
        print(dataframe.info())

if __name__ == "__main__":
    main()