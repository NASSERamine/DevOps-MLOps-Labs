import pytest
import os

def test_src_directory_exists():
    """
    Vérifie que le répertoire 'src' existe.
    """
    # '..' remonte d'un niveau (de /tests à la racine du projet)
    project_root = os.path.dirname(os.path.dirname(__file__))
    src_path = os.path.join(project_root, 'src')
    
    assert os.path.exists(src_path), "Le dossier 'src' est manquant"
    assert os.path.isdir(src_path), "Le chemin 'src' n'est pas un dossier"

def test_train_script_exists():
    """
    Vérifie que le script d'entraînement 'src/train.py' existe.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    train_script_path = os.path.join(project_root, 'src', 'train.py')
    
    assert os.path.exists(train_script_path), "Le script 'src/train.py' est manquant"
    assert os.path.isfile(train_script_path), "Le chemin 'src/train.py' n'est pas un fichier"

def test_requirements_file_exists():
    """
    Vérifie que le fichier 'requirements.txt' existe à la racine.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    req_path = os.path.join(project_root, 'requirements.txt')
    
    assert os.path.exists(req_path), "Le fichier 'requirements.txt' est manquant à la racine"
    assert os.path.isfile(req_path), "Le chemin 'requirements.txt' n'est pas un fichier"