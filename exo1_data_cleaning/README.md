# Pipeline de Nettoyage des Données

Ce projet fournit un script Python permettant de charger, nettoyer,
valider et analyser des données produits à partir d'un fichier CSV.\
Il applique plusieurs contrôles de qualité tels que l'unicité, la
complétude, la validité, la cohérence et la fraîcheur des données.

------------------------------------------------------------------------

## 📂 Structure du Projet

    .
    ├── main.py
    ├── products.csv
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🔧 Installation

1.  Clonez le dépôt ou téléchargez les fichiers du projet.
2.  Installez les dépendances :

``` bash
pip install -r requirements.txt
```

**requirements.txt**

    pandas
    unicodedata

------------------------------------------------------------------------

## ▶️ Utilisation

Exécutez le script principal :

``` bash
python main.py
```

------------------------------------------------------------------------

## 🧹 Étapes de Nettoyage des Données

### 1. **Unicité**

Supprime les lignes dupliquées avec `drop_duplicates`.

### 2. **Complétude**

-   Les lignes sans prix sont supprimées.
-   Les quantités en stock manquantes sont remplacées par `0`.

### 3. **Validité & Formatage**

-   Nettoyage des valeurs de prix : suppression du symbole `"€"` et des
    virgules.
-   Conversion en `float`.
-   Vérification que la quantité en stock est positive et de type
    entier.

### 4. **Cohérence**

-   Suppression des accents et mise en minuscules sur les catégories.

### 5. **Actualité (Timeliness)**

Filtre les produits dont `date_added` est antérieure à **2024-01-01**.

------------------------------------------------------------------------

## 📝 Description des Fonctions

  Fonction                          Description
  --------------------------------- ------------------------------------------------------
  `load_CSV_To_Dataframe`           Charge le fichier CSV dans un DataFrame
  `uniqueness`                      Supprime les doublons
  `completeness`                    Gestion des valeurs manquantes
  `validity_And_Formatting_Price`   Nettoie et convertit les prix
  `validity_Stock_Quantity`         Valide les quantités de stock
  `consistency`                     Normalise les catégories
  `timeliness`                      Détecte les produits périmés (selon la date d'ajout)

------------------------------------------------------------------------

## 📊 Résultats Affichés

Le script affiche :

-   Le jeu de données initial
-   Les statistiques descriptives
-   Les produits périmés
-   Le jeu de données final nettoyé

------------------------------------------------------------------------

## 📜 Licence

Ce projet est libre d'utilisation et de modification.
