#!/usr/bin/env python3
import argparse
from commands.init import init
from commands.auth import register, login, logout
from commands.add import add
from commands.commit import commit

def main():
    parser = argparse.ArgumentParser(prog="pit")
    subparsers = parser.add_subparsers(dest="comando")

    subparsers.add_parser("init")
    subparsers.add_parser("register")
    subparsers.add_parser("login")
    subparsers.add_parser("logout")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("arquivo")

    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("-m", "--mensagem", required=True)

    args = parser.parse_args()

    if args.comando == "init":
        init()
    elif args.comando == "register":
        register()
    elif args.comando == "login":
        login()
    elif args.comando == "logout":
        logout()
    elif args.comando == "add":
        add(args.arquivo)
    elif args.comando == "commit":
        commit(args.mensagem)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
