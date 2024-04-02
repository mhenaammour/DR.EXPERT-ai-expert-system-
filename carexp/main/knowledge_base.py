"""from aima3.logic import *
from aima3.utils import *

symptomes = ["Fievre", "Douleur_abdominale", "Nausees", "Vomissements", "Diarrhee", "Maux_de_tete","Douleur_thoracique", "Essoufflement", "Eruptions_cutanees", "Fatigue", "Perte_de_poids","Toux", "Sensation_de_bruleur_en_urinant", "Douleurs_musculaires", "Douleurs_articulaires"]
             

fc = FolKB()


def Fievre(name):
    fc.tell(expr('Fievre("{}")'.format(name)))

def Douleur_abdominale(name):
    fc.tell(expr('Douleur_abdominale("{}")'.format(name)))

def Nausees(name):
    fc.tell(expr('Nausees("{}")'.format(name)))

def Vomissements(name):
    fc.tell(expr('Vomissements("{}")'.format(name)))

def Diarrhee(name):
    fc.tell(expr('Diarrhee("{}")'.format(name)))

def Maux_de_tete(name):
    fc.tell(expr('Maux_de_tete("{}")'.format(name)))

def Douleur_thoracique(name):
    fc.tell(expr('Douleur_thoracique("{}")'.format(name)))

def Essoufflement(name):
    fc.tell(expr('Essoufflement("{}")'.format(name)))

def Eruptions_cutanees(name):
    fc.tell(expr('Eruptions_cutanees("{}")'.format(name)))

def Fatigue(name):
    fc.tell(expr('Fatigue("{}")'.format(name)))

def Perte_de_poids(name):
    fc.tell(expr('Perte_de_poids("{}")'.format(name)))

def Toux(name):
    fc.tell(expr('Toux("{}")'.format(name)))

def Sensation_de_bruleur_en_urinant(name):
    fc.tell(expr('Sensation_de_bruleur_en_urinant("{}")'.format(name)))

def Douleurs_musculaires(name):
    fc.tell(expr('Douleurs_musculaires("{}")'.format(name)))

def Douleurs_articulaires(name):
    fc.tell(expr('Douleurs_articulaires("{}")'.format(name)))


        

fc.tell(expr("Fievre(x) & Douleur_abdominale(x) ==> Tellicite(x)"))
fc.tell(expr("Nausees(x) & Vomissements(x) ==> Gastro_enterite(x)"))
fc.tell(expr("Diarrhee(x) & Maux_de_tete(x) ==> Intoxication_alimentaire(x)"))
fc.tell(expr("Douleur_thoracique(x) & Essoufflement(x) ==> Maladie_cardiaque(x)"))
fc.tell(expr("Eruptions_cutanees(x) & Fatigue(x) ==> Infection_virale(x)"))
fc.tell(expr("Perte_de_poids(x) & Douleur_abdominale(x) ==> Cancer_du_colon(x)"))
fc.tell(expr("Fievre(x) & Toux(x) ==> Infection_respiratoire(x)"))
fc.tell(expr("Douleur_abdominale(x) & Sensation_de_bruleur_en_urinant(x) ==> Infection_urinaire(x)"))
fc.tell(expr("Douleurs_musculaires(x) & Maux_de_tete(x) ==> Grippe(x)"))
fc.tell(expr("Douleurs_articulaires(x) & Eruptions_cutanees(x) ==> Lupus(x)"))

name = input("Bonjour, quel est votre nom? ")

print(f"Bonjour {name}! Quels sont les symptômes que vous ressentez ? :")
print("avez-vous l'un des symptomes suivants :")

def ajouter_symptome(symptome):
    while True:
        reponse = input(f"Est-ce que vous avez {symptome} ? (oui/non) ")
        if reponse.lower() == 'oui':
            fc.tell(expr(f"{symptome}({name})"))
            return True
        elif reponse.lower() == 'non':
            return False
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")



for symptome in symptomes:
    ajouter_symptome(symptome)

#print(fc.clauses)


def diagnostiquer(name,fc):
    maladies = {
        "Tellicite": "Il est possible que vous souffriez d'une tellicite.",
        "Gastro_enterite": "Il est possible que vous souffriez d'une gastro-entérite.",
        "Intoxication_alimentaire": "Il est possible que vous souffriez d'une intoxication alimentaire.",
        "Maladie_cardiaque": "Il est possible que vous souffriez d'une maladie cardiaque.",
        "Infection_virale": "Il est possible que vous souffriez d'une infection virale.",
        "Cancer_du_colon": "Il est possible que vous souffriez d'un cancer du colon.",
        "Infection_respiratoire": "Il est possible que vous souffriez d'une infection respiratoire.",
        "Infection_urinaire": "Il est possible que vous souffriez d'une infection urinaire.",
        "Grippe": "Il est possible que vous souffriez de la grippe.",
        "Lupus": "Il est possible que vous souffriez de lupus."
    }

    trouv=0

    for maladie in maladies :
        solution = fc.ask(expr(f"{maladie}({name})"))
        if solution :
            print(maladies[f"{maladie}"], "and")
            trouv+=1
    if trouv==0 :
        print('aucune malade a diagnostiquer ')


diagnostiquer(name,fc)"""