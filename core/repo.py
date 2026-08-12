import os
import json

MYVCS_DIR = ".myvcs"

def get_repo_path():
    return os.path.join(os.getcwd(), MYVCS_DIR)

def repo_exists():
    return os.path.isdir(get_repo_path())

def require_repo():
    if not repo_exists():
        print("Erro, repositorio nao encontrado, rode 'pit init'para criar um novo repositorio")
        exit(1)

def require_login():
    auth_path = os.path.join(get_repo_path(), "auth.json")
    with open(auth_path, "r") as f:
        auth = json.load(f)

    if not auth["logged_in"]:
        print("Erro: você precisa estar logado, rode 'pit login'")
        exit(1)

    return auth["logged_in"]
