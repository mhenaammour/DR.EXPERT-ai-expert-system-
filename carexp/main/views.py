import datetime
from django.shortcuts import render,redirect
from aima3.logic import *
from aima3.utils import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.units import inch


doctor_name = "DR EXPERT"




def expertpage(request):
    symptomes = ["Fievre", "Douleur_abdominale", "Nausees", "Vomissements", "Diarrhee", "Maux_de_tete","Douleur_thoracique", "Essoufflement", "Eruptions_cutanees", "Fatigue", "Perte_de_poids","Toux", "Sensation_de_bruleur_en_urinant", "Douleurs_musculaires", "Douleurs_articulaires"]

    return render(request,'expert.html',{'symptomes':symptomes})

def index(request):
    return render(request,'index.html')



def generate_prescription_for_disease(disease):
    prescription = []
    
    if disease == "Tellicite":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_A", "1 comprimé deux fois par jour", "7 jours"])
    elif disease == "Gastro_enterite":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_B", "1 comprimé toutes les 6 heures", "3 jours"])
        prescription.append(["Medicament_C", "1 comprimé deux fois par jour", "5 jours"])
    elif disease == "Intoxication_alimentaire":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_D", "2 comprimés deux fois par jour", "5 jours"])
    elif disease == "Maladie_cardiaque":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_E", "1 comprimé une fois par jour", "30 jours"])
    elif disease == "Infection_virale":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_F", "1 comprimé deux fois par jour", "7 jours"])
    elif disease == "Cancer_du_colon":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_G", "3 comprimés une fois par jour", "60 jours"])
    elif disease == "Infection_respiratoire":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_H", "1 comprimé deux fois par jour", "10 jours"])
    elif disease == "Infection_urinaire":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_I", "2 comprimés deux fois par jour", "7 jours"])
    elif disease == "Grippe":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_J", "1 comprimé trois fois par jour", "5 jours"])
    elif disease == "Lupus":
        prescription.append(["Nom du médicament", "Posologie", "Durée"])
        prescription.append(["Medicament_K", "2 comprimés une fois par jour", "30 jours"])
    
    return prescription


def create_medical_prescription(patient_name, doctor_name, diseases, filename):
    # Obtenir la date actuelle
    prescription_date = datetime.datetime.now()
    
    # Créer un document PDF
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # Styles pour le titre et le contenu
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    content_style = styles["Normal"]
    
    # Contenu de l'ordonnance
    prescription_content = []
    prescription_content.append(Paragraph("ORDONNANCE MÉDICALE", title_style))
    prescription_content.append(Spacer(1, 12))
    
    # Informations du patient et du médecin
    patient_info = "Patient: {}".format(patient_name)
    doctor_info = "Médecin: {}".format(doctor_name)
    prescription_date_info = "Date: {}".format(prescription_date)
    patient_doctor_info = Table([[patient_info, doctor_info, prescription_date_info]], colWidths=[2*inch, 2*inch, 2*inch], style=[('ALIGN', (0,0), (-1,-1), 'LEFT')])
    prescription_content.append(patient_doctor_info)
    prescription_content.append(Spacer(1, 12))
    
    # Générer une ordonnance pour chaque maladie
    for disease in diseases:
        prescription_content.append(Paragraph(f"Ordonnance pour {disease}:", content_style))
        medication_list = generate_prescription_for_disease(disease)
        if medication_list:
            medication_table = Table(medication_list, colWidths=[2*inch, 2*inch, 2*inch])
            prescription_content.append(medication_table)
            prescription_content.append(Spacer(1, 12))
        else:
            prescription_content.append(Paragraph("Aucun médicament prescrit pour cette maladie.", content_style))
            prescription_content.append(Spacer(1, 12))
    
    # Ajouter le contenu au document
    doc.build(prescription_content)






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
        msge=[]
        for maladie in maladies:
            if fc.ask(expr(f"{maladie}('{name}')")):
                messages.append(maladies[maladie])
                msge.append(maladie)
                trouv = trouv + 1
        if trouv == 0:
            messages.append("Aucune maladie trouvée.")
        print(fc.clauses)
        create_diagnosis_report(name, messages)
        create_medical_prescription(name, doctor_name, msge, f"{name}_ord_report.pdf")


        return render(request,'result.html', {'messages': messages , 'name' : name})
 

    return render(request,'result.html', {'messages': messages , 'name' : name})




