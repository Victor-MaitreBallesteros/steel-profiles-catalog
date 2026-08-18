# Permet d'importer directement depuis steel_profiles
from .catalog import CatalogueAcier, Profile

# Définit ce qui est exporté quand quelqu'un fait "from steel_profiles import *"
__all__ = ["CatalogueAcier", "Profile"]