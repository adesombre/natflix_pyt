from users import users

def display():
    print("-"*100)
    print(f"*{'NATFLIX':^98}*")
    print("-" * 100)


def display_menu():
    print("1: s'inscrire ")
    print("2: se connecter ")
    print("3: sortir du programme")

def main():
    choix = algo_menu()
    print("mon choix", choix)
    match(choix):
        case '1':
            print("inscription")
            user=users.infos_user()

        case'2':
            print("se connecter")
        case '3':
            print("fin du programme")


def algo_menu():
    display_menu()
    choix = None
    while choix is None:
        choix = input("Entrer votre choix : ")
        if choix not in ('1','2','3'):
            print("votre choix n'est pas valide ")
            choix = None
    return choix
if __name__ == '__main__':
   main()