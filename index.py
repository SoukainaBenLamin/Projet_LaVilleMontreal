import json
from database import Database
from flask import g, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from setup import *
from flask import request, render_template, redirect, flash, make_response
from dicttoxml import dicttoxml
from json import loads
from tweet import *
from emails import *
import collections
collections.Iterable = collections.abc.Iterable

"""
    Cette fonction permet de créer une base
    de données
"""


def get_db():
    # Créer une ressource si cette dernière n'existe pas
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


"""
    Cette fonction permet de se deconnecter
    d'une base de données
"""


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


"""
    Cette fonction permet de valider les queryParameters d'une requette http
"""


def validate_arguments(requette):
    if requette.args is not None and len(request.args) == 1:
        arrondis = request.args.get("arrondissement")
        if arrondis is not None:
            return True
    return False


"""
    Cette fonction permet de importer les données de la ville de montreal
    et de les inclure dans notre base de données, également , il permet
    d'envoyer les emails et poster des tweets à chaque importation de données
"""


def import_data(db):
    liste = [
        get_glissades_data(db),
        get_piscines_data(db),
        get_patinoire_data(db)]
    with app.app_context():
        send_mail(list(set(liste[0])), list(
            set(liste[1])), list(set(liste[2])))
        post_tweets(list(set(liste[0])), list(
            set(liste[1])), list(set(liste[2])))


"""
    le context de notre application :
    ici, on déclare le déclencheur Backgroundscheduler()
"""
with app.app_context():
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Canada/Eastern'})
    scheduler.add_job(import_data, 'cron', args=(get_db(),),
                      day_of_week='mon-sun', hour=0, minute=0)
    scheduler.start()

"""
    Cette route permet de voir la liste de toutes les installations
    d'un arrondissment spécifique
"""


@app.route('/api/installations', methods=['GET'])
def research_by_arrondissment():
    if validate_arguments(request):
        arrondis = request.args.get("arrondissement")
        piscines = get_db().get_piscines_of_arrondis(arrondis)
        glissades = get_db().get_glissades_of_arrondis(arrondis)
        patinoires = get_db().get_patinoires_of_arrondis(arrondis)
        if len(piscines) == 0 and len(glissades) == 0 and len(patinoires) == 0:
            return jsonify({'vide': True}), 200
        else:
            data_pis = [{"nom": piscine[0]} for piscine in piscines]
            data_glis = [{"nom": glissade[0]} for glissade in glissades]
            data_pati = [{"nom": patinoire[0]} for patinoire in patinoires]
            return jsonify({'piscines': data_pis, 'glissades': data_glis,
                            'patinoires': data_pati}), 200
    else:
        return render_template("404.html"), 404


"""
    c'est la route de la page d'accueil de notre application
"""


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


"""
    Cette route permet de voir la documentation de tous
    les services Rest Api
"""


@app.route('/doc')
def documentation():
    return render_template('documentation.html')


"""
    Cette route permet de voir toutes les informations
    d'une piscine spécifiée par son nom.
"""


@app.route('/api/piscine/<name>', methods=['GET'])
def piscine_info(name):
    info_piscine = get_db().get_piscine_infos(name)
    if len(info_piscine) == 0:
        return render_template("404.html"), 404
    data_pis = [{"Id": info_piscine[0][1],
                 "Type": info_piscine[0][2],
                 "Nom": info_piscine[0][3],
                 "Arrondissement": info_piscine[0][4],
                 "Adresse": info_piscine[0][5],
                 "Propriété": info_piscine[0][6]}]

    return jsonify({"infos": data_pis})


"""
    Cette route permet de voir toutes les informations
    d'une glissade spécifiée par son nom.
"""


@app.route('/api/glissade/<name>', methods=['GET'])
def glissade_info(name):
    info_glissade = get_db().get_one_glissade(name)
    if len(info_glissade) == 0:
        return render_template("404.html"), 404
    data_glis = [{"Nom": info_glissade[0][1],
                  "Arrondissement": info_glissade[0][2],
                  "Cle": info_glissade[0][3],
                  "Date": info_glissade[0][4],
                  "Ouvert": info_glissade[0][5],
                  "Deblaye": info_glissade[0][6],
                  "Condition": info_glissade[0][7]}]

    return jsonify({"infos": data_glis})


"""
    Cette route permet de voir toutes les informations
    d'un patinoire spécifié par son nom.
"""


@app.route('/api/patinoire/<name>', methods=['GET'])
def patinoire_info(name):
    info_patinoire = get_db().get_one_patinoire(name)
    if len(info_patinoire) == 0:
        return render_template("404.html"), 404
    data_pati = [{"Nom": info_patinoire[0][1],
                  "Arrondissement": info_patinoire[0][2],
                  "Date": info_patinoire[0][3],
                  "Ouvert": info_patinoire[0][4],
                  "Deblaye": info_patinoire[0][5],
                  "Arrose": info_patinoire[0][6],
                  "resurface": info_patinoire[0][7]}]

    return jsonify({"infos": data_pati})


"""
    Cette route permet de voir toutes les installations soit de type
    piscines, glissades ou patinoires.
"""


@app.route('/api/installations/<type>', methods=['GET'])
def installations_by_type(type):
    if type == 'piscines':
        piscines = get_db().get_piscines_by_nom()
        data_pis = [{"nom": piscine[0]} for piscine in piscines]
        return jsonify({'piscines': data_pis}), 200
    elif type == 'glissades':
        glissades = get_db().get_glissades_by_nom()
        data_glis = [{"nom": glissade[0]} for glissade in glissades]
        return jsonify({'glissades': data_glis}), 200
    elif type == 'patinoires':
        patinoires = get_db().get_patinoires_by_nom()
        data_pat = [{"nom": patinoire[0]} for patinoire in patinoires]
        return jsonify({'patinoires': data_pat}), 200
    else:
        return render_template("404.html"), 404


"""
    Cette fonction permet créer un objet Json de
    tous les piscines et ses informations
"""


def fill_piscines_data(piscines):
    data_pis = [{"Id": piscines[i][1],
                 "Type": piscines[i][2],
                 "Nom": piscines[i][3],
                 "Arrondissement": piscines[i][4],
                 "Adresse": piscines[i][5],
                 "Propriété": piscines[i][6],
                 "Gestion": piscines[i][7],
                 "Point_x": piscines[i][8],
                 "Point_y": piscines[i][9],
                 "Equipement": piscines[i][10],
                 "Longitude": piscines[i][11],
                 "Latitude": piscines[i][12]} for i in range(len(piscines))]
    return data_pis


"""
    Cette fonction permet créer un objet Json de
    tous les glissades et ses informations
"""


def fill_glissades_data(glissades):
    data_glis = [{"Nom": glissades[i][1],
                  "Arrondissement": glissades[i][2],
                  "Cle": glissades[i][3],
                  "Date": glissades[i][4],
                  "Ouvert": glissades[i][5],
                  "Deblaye": glissades[i][6],
                  "Condition": glissades[i][7]} for i in range(len(glissades))]
    return data_glis


"""
    Cette fonction permet créer un objet Json de
    tous lies patinoires et ses informations
"""


def fill_patinoires_data(patinoires):
    data_pati = [{"Nom": patinoires[i][1],
                  "Arrondissement": patinoires[i][2],
                  "Date": patinoires[i][3],
                  "Ouvert": patinoires[i][4],
                  "Deblaye": patinoires[i][5],
                  "Arrose": patinoires[i][6],
                  "resurface": patinoires[i][7]}
                 for i in range(len(patinoires))]
    return data_pati


"""
    Cette fonction permet d'extraire toutes les installations,
    ainsi que leurs informations
"""


def extract_all_data(db):
    piscines = db.get_all_piscines()
    glissades = db.get_all_glissades()
    patinoires = db.get_all_patinoires()
    data_pis = fill_piscines_data(piscines)
    data_glis = fill_glissades_data(glissades)
    data_pati = fill_patinoires_data(patinoires)
    return data_glis, data_pis, data_pati


"""
    Cette fonction permet de fusionner les differents dataFrame
    des données
"""


def construct_data_frames():
    fd = open('./static/all_glis.json', 'r')
    donn_glis = json.loads(fd.read())
    fd.close()
    df_g = pd.json_normalize(donn_glis)
    fd = open('./static/all_piss.json', 'r')
    donn_pis = json.loads(fd.read())
    df_pi = pd.json_normalize(donn_pis)
    fd.close()
    fd = open('./static/all_pati.json', 'r')
    donn_pati = json.loads(fd.read())
    fd.close()
    df_p = pd.json_normalize(donn_pati)
    return df_g, df_pi, df_p


"""
    Cette route permet de lister toutes les installations en format
    JSON.
"""


@app.route('/api/all_installations/', methods=['GET'])
def list_installations():
    data_pis = extract_all_data(get_db())[1]
    data_glis = extract_all_data(get_db())[0]
    data_pati = extract_all_data(get_db())[2]
    return make_response(jsonify({'piscines': data_pis, 'glissades': data_glis,
                                  'patinoires': data_pati}), 200)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


"""
    Cette route permet de lister toutes les installations en format
    XML.
"""


@app.route('/api/all_installations_xml/', methods=['GET'])
def list_installations_xml():
    json_object = list_installations()
    xml_object = dicttoxml(loads(json_object.data))
    response = make_response(xml_object)
    return response


"""
    Cette route permet de lister toutes les installations en format
    CSV.
"""


@app.route('/api/all_installations_csv/', methods=['GET'])
def list_installations_csv():
    with open('./static/all_glis.json', 'w') as f:
        f.write(json.dumps(extract_all_data(get_db())[0]))
        f.close()
    with open('./static/all_piss.json', 'w') as f:
        f.write(json.dumps(extract_all_data(get_db())[1]))
        f.close()
    with open('./static/all_pati.json', 'w') as f:
        f.write(json.dumps(extract_all_data(get_db())[2]))
        f.close()
    result = pd.concat([construct_data_frames()[0],
                        construct_data_frames()[1],
                        construct_data_frames()[2]])
    result.to_csv('./static/all_installations.csv', index=False,
                  encoding='utf-8')
    fi = open('./static/all_installations.csv', 'r')
    return fi.read()
