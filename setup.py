from urllib import request
import xml.etree.ElementTree as ET
import pandas as pd

"""
***********************************************
manipuler le fichier des piscines
***********************************************
"""


def get_piscines_data(db):
    url = "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-" \
          "e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/" \
          "download/piscines.csv"
    request.urlretrieve(url, "files/piscines.csv")
    new_piscines = []
    piscines = pd.read_csv('./files/piscines.csv')
    for _, pis in piscines.iterrows():
        old_pis = db.get_one_piscine(pis['ID_UEV'], pis['TYPE'], pis['NOM'])
        if len(old_pis) == 0:
            db.add_piscine(
                pis['ID_UEV'],
                pis['TYPE'],
                pis['NOM'],
                pis['ARRONDISSE'],
                pis['ADRESSE'],
                pis['PROPRIETE'],
                pis['GESTION'],
                pis['POINT_X'],
                pis['POINT_Y'],
                pis['EQUIPEME'],
                pis['LONG'],
                pis['LAT'])
            new_piscines.append(pis['NOM'])
        else:
            if old_pis[0][5] != pis['ADRESSE']:
                db.update_piscine(
                    pis['ID_UEV'],
                    pis['TYPE'],
                    pis['NOM'],
                    "adresse",
                    pis['ADRESSE'])
            elif old_pis[0][6] != pis['PROPRIETE']:
                db.update_piscine(
                    pis['ID_UEV'],
                    pis['TYPE'],
                    pis['NOM'],
                    "propriete",
                    pis['PROPRIETE'])
            elif old_pis[0][7] != pis['GESTION']:
                db.update_piscine(
                    pis['ID_UEV'],
                    pis['TYPE'],
                    pis['NOM'],
                    "gestion",
                    pis['GESTION'])
            elif old_pis[0][10] != pis['EQUIPEME']:
                db.update_piscine(
                    pis['ID_UEV'],
                    pis['TYPE'],
                    pis['NOM'],
                    "equipement",
                    pis['EQUIPEME'])
    return new_piscines


"""
****************************************
manipuler le fichier des glissades
****************************************
"""


def get_glissades_data(db):
    url = "http://www2.ville.montreal.qc.ca/services_citoyens/" \
          "pdf_transfert/L29_GLISSADE.xml"
    new_glissades = []
    request.urlretrieve(url, "files/glissades.xml")
    glissades = ET.parse("files/glissades.xml")
    racine = glissades.getroot()
    for glissade in racine:
        old_glissade = db.get_one_glissade(glissade[0].text)
        # si c'est un nouveau glissade, on l'ajoute
        if len(old_glissade) == 0:
            db.add_glissade(glissade[0].text,
                            glissade[1][0].text, glissade[1][1].text,
                            glissade[1][2].text, glissade[2].text,
                            glissade[3].text, glissade[4].text)
            new_glissades.append(glissade[0].text)
        else:
            if old_glissade[0][4] != glissade[1][2].text:
                db.update_glissade(
                    old_glissade[0][1],
                    "date_maj",
                    glissade[1][2].text)
            elif old_glissade[0][5] != glissade[2].text:
                db.update_glissade(
                    old_glissade[0][1], "ouvert", glissade[2].text)
            elif old_glissade[0][6] != glissade[3].text:
                db.update_glissade(
                    old_glissade[0][1],
                    "deblaye",
                    glissade[3].text)
            elif old_glissade[0][7] != glissade[4].text:
                db.update_glissade(
                    old_glissade[0][1],
                    "condition",
                    glissade[4].text)
    return new_glissades


"""
***************************************
manipuler le fichier des patinoires
***************************************
"""


def add_to_patinoire_list(arrondisse, patinoire, liste, condition):
    for k in condition:
        if k.tag == "date_heure":
            date = k.text.strip()
        if k.tag == "ouvert":
            ouvert = k.text.strip()
        if k.tag == "deblaye":
            deblaye = k.text.strip()
        if k.tag == "arrose":
            arrose = k.text.strip()
        if k.tag == "resurface":
            resurface = k.text.strip()
    liste.append((arrondisse, patinoire, date, ouvert, deblaye,
                  arrose, resurface))
    return liste


def get_patinoire_elements(racine):
    liste = []
    for a in racine:
        nom_arr = a[0].text.strip()
        lent = len(list(a[1]))
        nom_pat = a[1][0].text.strip()
        for i in range(1, lent):
            if a[1][i].tag == "nom_pat":
                add_to_patinoire_list(nom_arr, nom_pat, liste, a[1][i - 1])
                nom_pat = a[1][i].text.strip()
            if i == lent - 1:
                add_to_patinoire_list(nom_arr, nom_pat, liste, a[1][i - 1])
    return liste


def get_patinoire_data(db):
    url = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd" \
          "-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0" \
          "/download/l29-patinoire.xml "
    request.urlretrieve(url, "files/patinoires.xml")
    patinoires = ET.parse("files/patinoires.xml")
    racine = patinoires.getroot()
    liste = get_patinoire_elements(racine)
    new_patinoire = []
    for each in liste:
        old_patinoire = db.get_one_patinoire(each[1])
        if len(old_patinoire) == 0:
            db.add_patinoire(each[1], each[0], each[2], each[3], each[4],
                             each[5], each[6])
            new_patinoire.append(each[1])
        else:
            if old_patinoire[0][3] != each[2]:
                db.update_patinoire(old_patinoire[1], each[2], each[3],
                                    each[4], each[5], each[6])
    return new_patinoire
