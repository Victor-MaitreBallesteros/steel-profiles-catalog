# Steel Profiles Catalog (`steel-profiles-catalog`)

`steel-profiles-catalog` est un package Python pour les ingénieurs structure. Il fournit un catalogue numérique de profilés en acier gammes **IPE**, **HEA** et **HEB**) incluant leurs dimensions géométriques de base.

Le package stocke les données pré-calculées dans un dictionnaire interne (`O(1)`), permettant des requêtes sans latence de lecture disque ou de maillage par éléments finis en temps réel.

## Fonctionnalités

* Le data_generator.py contient en entrée les caractéristiques de base des profilés (extrait du catalogue de Arcelor Mittal) et produit en sortie le data.py qui lui est la bibliothèque contenant toutes les données.
  * Le programme utilise la bibliothèque sectionproperties pour calculer l'aire et les inerties quadratiques
* Le programme catalog.py prend le data.py en entrée et construit le dictionnaire
* Ainsi, il est possible d'importer le package puis de renseigner le nom du profilé recherché pour obtenir les caractéristiques recherchées et pouvoir les utiliser.


---

## 📂 Arborescence du projet

```text
steel-profiles-catalog/
│
├── pyproject.toml
└── steel_profiles/
    ├── __init__.py
    ├── catalog.py
    └── data.py
