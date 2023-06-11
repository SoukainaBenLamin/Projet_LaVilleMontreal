from flask import Flask
from flask_mail import Mail, Message
import yaml

app = Flask(__name__)
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "inf5190.H22@gmail.com"
app.config['MAIL_PASSWORD'] = "INF5190*."
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
mail = Mail(app)

"""
    Cette fonction permet d'envoyer un email avec
    les nouveaux installations
"""


def send_installations(email, glissades, piscines, patinoires):
    msg = Message("INF5190 - La liste des nouveaux installation",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[email])
    msg.body = get_body_liste(glissades, piscines, patinoires)
    mail.send(msg)


"""
    Cette fonction permet d'écrire le body ou bien le contenu
    de l'email avec la liste des nouveaux installations.
"""


def get_body_liste(glissades, piscines, patinoires):
    body = f'''
    Il y a des nouveaux installations dans la ville de Montréal ! \n
    Voici la liste de ces installations : \n'''
    if len(glissades) != 0:
        for i in range(len(glissades)):
            body += f''' Le nom du nouveau glissade {i + 1} est :
            {glissades[i]} \n'''
    if len(piscines) != 0:
        for i in range(len(piscines)):
            body += f''' Le nom de la nouvelle piscine {i + 1} est :
            {piscines[i]} \n'''
    if len(patinoires) != 0:
        for i in range(len(patinoires)):
            body += f''' Le nom de nouveau patinoire {i + 1} est :
            {patinoires[i]} \n'''
    return body


"""
    Cette fonction permet d'envoyer un mail
"""


def send_mail(gliss, pisc, patin):
    yml = open('./static/emails.yml')
    yml_data = yaml.load(yml, Loader=yaml.FullLoader)
    if len(gliss) != 0 or len(pisc) != 0 or len(patin) != 0:
        for i in range(len(yml_data["users"])):
            send_installations(yml_data["users"][i], gliss, pisc, patin)
