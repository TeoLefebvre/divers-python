# Divers-python

Divers programmes amusants en langage python en un seul fichier chacun.

## Installation

Je vous conseil d'installer les modules dans un [environnement virtuel python](https://virtualenv.pypa.io/en/latest/user_guide.html) pour éviter de polluer votre installation environnement global et installer la bonne version des modules pour chaque projet.

Pour manjaro : 
```bash
sudo pacman -S python-virtualenv # installation module virtualenv
virtualenv env # création d'un environnement virtuel dans le dossier env
source env/bin/activate # activation de l'environnement virtuel
pip install -r requirements.txt # installation des modules nécessaires pour les différents programmes
```