from django.shortcuts import render,redirect
from aima3.logic import *
from aima3.utils import *

def expertpage(request):
    symptomes = ["Fievre", "Douleur_abdominale", "Nausees", "Vomissements", "Diarrhee", "Maux_de_tete","Douleur_thoracique", "Essoufflement", "Eruptions_cutanees", "Fatigue", "Perte_de_poids","Toux", "Sensation_de_bruleur_en_urinant", "Douleurs_musculaires", "Douleurs_articulaires"]

    return render(request,'expert.html',{'symptomes':symptomes})

def index(request):
    return render(request,'index.html')



from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_diagnosis_report(name, messages):
    filename = f"{name}_diagnosis_report.pdf"
    document_title = f"Rapport de diagnostic pour {name}"
    intro_text = f"Bonjour {name},\n\nVoici votre rapport de diagnostic.\n\n"
    
    # create the PDF file
    c = canvas.Canvas(filename, pagesize=letter)

    # add the title and introduction text
    c.setTitle(document_title)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 700, document_title)
    c.setFont("Helvetica", 12)
    c.drawString(50, 650, intro_text)
    
    # add the diagnosis messages
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 600, "Diagnostic:")
    c.setFont("Helvetica", 12)
    for i, message in enumerate(messages):
        textobject = c.beginText(50, 570-i*20)
        textobject.textLine(message)
        c.drawText(textobject)

    # save and close the PDF file
    c.save()

    return filename

def symptom_checker(request):
    symptomes = ["Fievre", "Douleur_abdominale", "Nausees", "Vomissements", "Diarrhee", "Maux_de_tete","Douleur_thoracique", "Essoufflement", "Eruptions_cutanees", "Fatigue", "Perte_de_poids","Toux", "Sensation_de_bruleur_en_urinant", "Douleurs_musculaires", "Douleurs_articulaires"]
    fc = FolKB()
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
    name = request.POST.get('name', '')
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        for symptome in symptoms:
            fc.tell(expr(f"{symptome}('{name}')"))
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
        trouv = 0
        messages = []
        for maladie in maladies:
            if fc.ask(expr(f"{maladie}('{name}')")):
                messages.append(maladies[maladie])
                trouv = trouv + 1
        if trouv == 0:
            messages.append("Aucune maladie trouvée.")
        print(fc.clauses)
        create_diagnosis_report(name, messages)

        return render(request,'result.html', {'messages': messages , 'name' : name})
 

    return render(request,'result.html', {'messages': messages , 'name' : name})
