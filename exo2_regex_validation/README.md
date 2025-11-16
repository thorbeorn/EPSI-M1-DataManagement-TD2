# Nettoyage et Validation de Données CSV

Ce projet propose un script Python permettant de **charger**, **nettoyer**, **formater** et **valider** des données issues d’un fichier CSV.  
Il utilise des expressions régulières pour vérifier la validité des **adresses e-mail**, **noms complets** et **numéros de téléphone français**.

---

## 🚀 Fonctionnalités

### ✔ Chargement du fichier CSV
Le script charge un fichier CSV via **pandas** grâce à :
```python
load_CSV_To_Dataframe()
```

### ✔ Validation par regex
- Validation des e‑mails  
- Validation des noms complets au format français  
- Validation des numéros de téléphone français (format `0X XX XX XX XX`)

### ✔ Nettoyage et formatage
Le script :
- Normalise les caractères (`.` `,` `:` `_` etc.)
- Reformate les noms propres (capitalisation correcte)
- Nettoie et reformate les numéros de téléphone (suppression des caractères non numériques, normalisation au format FR)

---

## 📦 Installation

Assurez‑vous d’avoir Python 3 installé.

### 1. Clone ou téléchargement du projet
```bash
git clone <url_du_projet>
cd <dossier_du_projet>
```

### 2. Installation des dépendances
```bash
pip install -r requirements.txt
```

---

## 📁 Fichiers importants

| Fichier | Description |
|--------|-------------|
| `Td2Exercice2.csv` | Fichier de données à traiter |
| `script.py` | Script Python contenant la logique |
| `requirements.txt` | Dépendances Python |
| `README.md` | Documentation du projet |

---

## ▶️ Utilisation

Exécutez simplement :

```bash
python script.py
```

Le script :
1. Affiche la liste des e‑mails invalides  
2. Ajoute des colonnes `_validate` dans le DataFrame  
3. Nettoie et formate les chaînes  
4. Affiche le DataFrame final propre et validé  

---

## 📚 Expressions régulières utilisées

### E‑mail
```
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

### Nom complet (format français complexe)
```
^[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+(?:[- ][A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+)*\s+(?:[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+|(?:de|du|des|le|la|les|d')\s+[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+(?:[- ][A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+)*)$
```

### Téléphone français
```
^0[1-9](?:\s\d{2}){4}$
```

---

## 📄 Licence
Libre d’utilisation et de modification.
