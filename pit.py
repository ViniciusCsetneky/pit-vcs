import sys
from commands.init import init
from commands.auth import register, login, logout
from commands.add import add
from commands.commit import commit

def main():
    if len(sys.argv) < 2:
        print("Uso: pit <comando>")
        print("Comandos disponíveis: init, register, login, logout, add, commit")
        return

    comando = sys.argv[1]

    if comando == "init":
        init()
    elif comando == "register":
        register()
    elif comando == "login":
        login()
    elif comando == "logout":
        logout()
    elif comando == "add":
        if len(sys.argv) < 3:
            print("Uso: pit add <arquivo>")
            return
        add(sys.argv[2])
    elif comando == "commit":
        if len(sys.argv) < 3:
            print("Uso: pit commit <mensagem>")
            return
        commit(sys.argv[2])
    else:
        print(f"Comando '{comando}' não reconhecido.")

if __name__ == "__main__":
    main()