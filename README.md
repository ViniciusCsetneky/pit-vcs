# pit-vcs
A simple version control system inspired by git

## Instalação

O `pit` roda como um comando global via link simbólico. Depois de clonar o
repositório, rode (uma vez por máquina):

```bash
chmod +x pit.py
mkdir -p ~/.local/bin
ln -sf "$(pwd)/pit.py" ~/.local/bin/pit
```

Garanta que `~/.local/bin` está no seu `PATH` (na maioria das distros Linux
já vem configurado por padrão). Depois disso, o comando `pit` funciona a
partir de qualquer diretório, sem precisar de `python3 pit.py`.

Obs: o link simbólico é local à máquina e não é versionado no git. Quem
clonar o repositório em outra máquina precisa repetir os comandos acima.

## Uso

```bash
pit init                     # cria o repositório na pasta atual
pit register                 # cria um usuário
pit login                    # loga com um usuário existente
pit logout                   # desloga o usuário atual
pit add <arquivo>            # adiciona um arquivo ao index
pit commit -m "mensagem"     # cria um commit com os arquivos do index
```

Todo comando (exceto `init`, `register` e `login`) exige um usuário logado.
