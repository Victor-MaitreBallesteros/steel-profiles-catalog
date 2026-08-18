# steel_profiles/catalog.py
from dataclasses import dataclass
from .data import PROFILES_DB

@dataclass
class Profile:
    nom: str
    famille: str
    masse_kg_m: float
    h_mm: float
    b_mm: float
    tw_mm: float
    tf_mm: float
    r_mm: float
    hi_mm: float
    d_mm: float
    A_mm2: float
    Iy_mm4: float
    Iz_mm4: float

class CatalogueAcier:
    def get_profile(self, nom_profile: str) -> Profile:
        """Récupère un profilé spécifique par son nom (ex: 'IPE 600')"""
        nom = nom_profile.upper()
        
        if nom not in PROFILES_DB:
            raise ValueError(f"Le profilé {nom} n'existe pas dans le catalogue.")
        
        # On récupère le dictionnaire de caractéristiques instantanément O(1)
        infos = PROFILES_DB[nom]
        
        # On hydrate la dataclass en passant le nom et les infos
        return Profile(nom=nom, **infos)