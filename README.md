# EPSI-M1-DataManagement-TD2

## TD 2 : qualité de la donnée

Ce dépôt contient deux exercices indépendants portant sur le
**nettoyage**, la **validation** et l'**analyse** de données issues de
fichiers CSV.\
Chaque exercice dispose de son propre script Python, de son fichier CSV
associé et d'une documentation dédiée.

L'objectif est d'explorer à la fois :

- la construction d’un pipeline complet de data-quality,
- la validation et le formatage correct de données personnelles et textuelles.

------------------------------------------------------------------------

## 🚀 Objectifs pédagogiques

✔ Charger et manipuler des données CSV avec Pandas
✔ Appliquer les dimensions de la qualité des données (unicité, complétude…)
✔ Nettoyer, formater et valider des colonnes hétérogènes
✔ Mettre en place des règles métier (dates, prix, catégories)
✔ Utiliser les expressions régulières pour valider emails, noms et téléphones
✔ Normaliser et formater des chaînes de caractères
✔ Améliorer la cohérence d’un dataset textuel

------------------------------------------------------------------------

## 📂 Structure générale du TD

    EPSI-M1-DataManagement-TD2/
    │── LICENSE.txt
    │── .gitignore
    │── exo1_data_cleaning/
    │   ├── main.py
    │   ├── products.csv
    │   ├── README.md
    │   └── requirements.txt
    │
    │── exo2_regex_validation/
    │   ├── script.py
    │   ├── Td2Exercice2.csv
    │   ├── README.md
    │   └── requirements.txt
    │
    └── README.md   ← ce fichier général

------------------------------------------------------------------------

# 🧪 Exercice 1 — Pipeline de Nettoyage & Qualité des Données
## 🔍 Description

Ce projet met en place un pipeline complet de nettoyage et validation d’un fichier CSV contenant des produits.

Le script applique :

### 1. Unicité

Suppression des doublons

### 2. Complétude

Retrait des lignes sans prix

Remplacement des quantités manquantes par 0

### 3. Validité & formatage

Nettoyage des prix (suppression du “€” et des virgules)

Conversion en float

Vérification des quantités (entier positif)

### 4. Cohérence

Normalisation des catégories :

minuscules

suppression des accents

### 5. Actualité (Timeliness)

Filtrage des produits dont la date_added est antérieure au 01/01/2024

🎯 **Objectif : produire un dataset propre, cohérent, exploitable et conforme aux règles métier.**

------------------------------------------------------------------------

📦 Technologies utilisées

    - pandas
    - unicodedata
    - datetime

------------------------------------------------------------------------

# 🧪 Exercice 2 — Validation et Nettoyage avec Expressions Régulières
## 🔍 Description

Ce projet se concentre sur la validation et la normalisation des données textuelles à l’aide d’expressions régulières :

### ✔ Validation par regex

    - Emails
    - Noms complets (format français)
    - format standardisé : 0X XX XX XX XX

### ✔ Nettoyage & formatage

    - Suppression des caractères parasites
    - Normalisation des chaînes (., ,, :, _…)
    - Reformattage automatique des noms (capitalisation correcte)
    - Nettoyage et normalisation des numéros de téléphone

### ✔ Génération d’indicateurs de validation

    - ajout de colonnes _validate pour chaque champ
    - affichage des lignes invalides

🎯 **Objectif : assurer la qualité, la structure et la conformité des données textuelles.**

------------------------------------------------------------------------

## 📦 Technologies utilisées

    - pandas
    - re (expressions régulières)

------------------------------------------------------------------------

# 🛠 Installation générale

### 1. Créer un environnement virtuel

    python -m venv venv

### 2. Activer l'environnement

**Windows**

    venv\Scripts\activate

**macOS / Linux**

    source venv/bin/activate

### 3. Installer les dépendances

    pip install -r exo1_data_cleaning/requirements.txt
    pip install -r exo2_regex_validation/requirements.txt

------------------------------------------------------------------------

# ▶️ Exécution

### Exercice 1 : pipeline de nettoyage

    python exo1_data_cleaning/main.py

### Exercice 2 : validation regex

    python exo2_regex_validation/main.py

------------------------------------------------------------------------

# 🎯 Compétences acquises

- Construire un pipeline complet de qualité des données
- Nettoyer et structurer des datasets hétérogènes
- Appliquer toutes les dimensions classiques de Data Quality
- Utiliser efficacement les expressions régulières
- Normaliser et formater automatiquement des champs textuels
- Détecter et signaler les valeurs invalides dans un dataset

------------------------------------------------------------------------

# 📄 Licence

Projet libre d'utilisation et de modification --- usage pédagogique
EPSI.