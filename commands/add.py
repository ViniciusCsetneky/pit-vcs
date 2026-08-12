import os
import hashlib
from core.repo import require_repo, require_login, get_repo_path
from core.storage import read_json, write_json

def hash_content(content):
    return hashlib.sha1(content).hexdigest()

def add(caminho):
    require_repo()
    require_login()

    if not os.path.isfile(caminho):
        print(f"Erro: arquivo '{caminho}' nao encontrado")
        return

    with open(caminho, "rb") as f:
        content = f.read()

    file_hash = hash_content(content)

    objects_dir = os.path.join(get_repo_path(), "objects")
    object_path = os.path.join(objects_dir, file_hash)
    if not os.path.isfile(object_path):
        with open(object_path, "wb") as f:
            f.write(content)

    index = read_json("index.json")
    index[caminho] = file_hash
    write_json("index.json", index)

    print(f"Arquivo '{caminho}' adicionado ao index.")
