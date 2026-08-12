import hashlib
import json
import time
from core.repo import require_repo, require_login
from core.storage import read_json, write_json, read_head, write_head

def commit(mensagem):
    require_repo()
    author = require_login()

    index = read_json("index.json")
    if not index:
        print("Erro: nao ha arquivos no index para commitar")
        return

    commits = read_json("commits.json")
    parent = read_head() or None

    commit_data = {
        "parent": parent,
        "author": author,
        "message": mensagem,
        "files": index,
        "timestamp": time.time(),
    }
    commit_id = hashlib.sha1(json.dumps(commit_data, sort_keys=True).encode()).hexdigest()
    commit_data["id"] = commit_id

    commits.append(commit_data)
    write_json("commits.json", commits)
    write_head(commit_id)
    write_json("index.json", {})

    print(f"[{commit_id[:7]}] {mensagem}")
