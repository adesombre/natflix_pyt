import re
import csv

def infos_user():
    name = None
    while name is None:
        name=input("entrer votre nom :")
        if name.split() == "":
            print('entrer un nom correct ')
            name = None
    email =None
    while email is None:
        email=input("entrer votre email :")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex,email) or email.split() == "":
            print("votre adresse n'est pas valide")
            email = None
    age = None
    while age is None:
        age =input("entrer votre age :")
        if not age.isdigit():
            print("veuillez entrer un age correct")
            age=None
    country =None
    while country is None:
        country =input("entrer votre pay")
        if country.split()== "":
            print("veuiller entrer un pay correct ")
            country=None
    subscription = None
    while subscription is None:
        subscription=input("entrer votre formule d'abonnement 1 ou 2 ")
        if not subscription in ('1','2'):
            print("la formule n'exite pas !!")
            subscription= None
    password= None
    while password is None:
        password=input("entrer votre mot de passe ")
        if  not re.match(r'[A-Za-z0-9@#$]{6,12}', password):
            print("votre mot de passe n'est pas correct")
            password =None
        data=(name,email,age,country,subscription,password)

    return data


def datas():
    with open('data.csv', 'a') as f:
        texte = csv.writer(f)
        texte.writerow(data)


if __name__ == '__main__':
    data=infos_user()
    datas()



