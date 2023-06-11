import sqlite3

"""
    Cette classe présente notre base
    de données
"""


class Database:
    """
        Cette fonction permet d'initier un objet
        le constructeur
    """

    def __init__(self):
        self.connection = None

    """
        Cette fonction permet de se connecter
        à une base de données
    """

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/db.db')
        return self.connection

    """
        Cette fonction permet de se déconnecter
        d'une base de données
    """

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    """
    ********************************************************************
    *************************** section piscines ***********************
    ********************************************************************
    """

    """
        Cette fonction permet de chercher l'id d'un piscine
        en particulier pour eviter les doublons
    """

    def get_one_piscine(self, id_uev, type, nom):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT * FROM piscine WHERE id_uev = ? and type = ? and nom = ? ",
            (id_uev, type, nom))
        piscine = cursor.fetchall()
        return piscine

    """
        permet de lister toutes les informaions d'une piscine
        à partir de son nom
    """

    def get_piscine_infos(self, name):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT * FROM piscine WHERE nom like ?",
            (name,))
        piscine = cursor.fetchall()
        return piscine

    """
        Cette fonction permet de chercher les piscines d'un
        arrondissent en particulier
    """

    def get_piscines_of_arrondis(self, arrondis):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT nom FROM piscine WHERE "
            "REPLACE(REPLACE(LOWER(arrondisse), ' ', ''),'–','-') like ? "
            "ORDER BY nom",
            (((arrondis.lower()).replace(" ", "")).
             replace("–", "-"),))
        piscines = cursor.fetchall()
        return piscines

    """
        Cette fonction permet de selectionner et de lister les noms
        de toutes les piscines
    """

    def get_piscines_by_nom(self):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT nom FROM piscine order by nom")
        piscines = cursor.fetchall()
        return piscines

    """
        Cette fonction permet de lister toutes les piscines
        avec leurs informations.
    """

    def get_all_piscines(self):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT * FROM piscine order by nom")
        piscines = cursor.fetchall()
        return piscines

    """
        Cette fonction permet d'ajouter une nouvelle piscine
    """

    def add_piscine(self, id_uev, type, nom, arrondisse, adresse, propriete,
                    gestion, x, y, equipement, long, lat):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO piscine(id_uev, type, nom, arrondisse,"
            " adresse, propriete,"
            " gestion, pointx, pointy, equipement,long,lat)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (id_uev, type, nom, arrondisse, adresse, propriete, gestion, x,
             y, equipement, long, lat))
        connection.commit()

    """
         Cette fonction permet de modifier un piscine
    """

    def update_piscine(self, id_uev, type, nom, change, val):
        connection = self.get_connection()
        cursor = connection.cursor()
        if change == "adresse":
            cursor.execute(
                "UPDATE piscine SET adresse = ? WHERE id_uev = ? and "
                " type = ? and nom = ?",
                (val, id_uev, type, nom))
        elif change == "propriete":
            cursor.execute(
                "UPDATE piscine SET propriete = ? WHERE id_uev = ? "
                "and type = ? and nom = ?",
                (val, id_uev, type, nom))
        elif change == "gestion":
            cursor.execute(
                "UPDATE piscine SET gestion = ? WHERE id_uev = ? and "
                "type = ? and nom = ?",
                (val, id_uev, type, nom))
        else:
            cursor.execute(
                "UPDATE piscine SET equipement = ? WHERE id_uev = ? and"
                " type = ? and nom = ?",
                (val, id_uev, type, nom))
        connection.commit()

    """
        *******************************************************************
        *************************** section glissades *********************
        *******************************************************************
    """

    """
        Cette fonction permet de chercher les informations d'un glissade
        en particulier à prtir de son nom.
    """

    def get_one_glissade(self, name):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT * FROM glissade WHERE nom like ?",
            (name,))
        glissade = cursor.fetchall()
        return glissade

    """
        Cette fonction permet de chercher les glissades
        d'un arrondissement en particulier
    """

    def get_glissades_of_arrondis(self, arrondis):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT nom FROM glissade WHERE "
            "REPLACE(LOWER(nom_arrondisse), ' ', '') like ?"
            "ORDER BY nom", ((arrondis.lower()).replace(
                " ", ""),))
        glissades = cursor.fetchall()
        return glissades

    """
        Cette fonction permet d'ajouter un nouveau glissade
    """

    def add_glissade(
            self,
            nom,
            nom_arrondisse,
            cle_arrondisse,
            date_maj,
            ouvert,
            deblaye,
            condition):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO glissade(nom, nom_arrondisse, cle_arrondisse,"
            " date_maj, ouvert, deblaye, condition)"
            "VALUES(?,?,?,?,?,?,?)",
            (nom, nom_arrondisse, cle_arrondisse, date_maj, ouvert,
             deblaye, condition))
        connection.commit()

    """
        Cette fonction permet de modifier une glissade
    """

    def update_glissade(self, name, change, val):
        connection = self.get_connection()
        cursor = connection.cursor()
        if change == "date_maj":
            cursor.execute("UPDATE glissade SET date_maj = ? WHERE nom = ? ",
                           (val, name))
        elif change == "ouvert":
            cursor.execute("UPDATE glissade SET ouvert = ? WHERE nom = ?",
                           (val, name))
        elif change == "deblaye":
            cursor.execute("UPDATE glissade SET deblaye = ? WHERE nom = ?",
                           (val, name))
        else:
            cursor.execute("UPDATE glissade SET condition = ? WHERE nom = ?",
                           (val, name))
        connection.commit()

    """
        Cette fonction permet de lister la liste des
        noms de tous les glissades.
    """

    def get_glissades_by_nom(self):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT nom FROM glissade")
        glissades = cursor.fetchall()
        return glissades

    """
        Cette fonction permet d'obtenir toute les informations
        de tous les glissades.
    """

    def get_all_glissades(self):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT * FROM glissade order by nom")
        glissades = cursor.fetchall()
        return glissades

    """
       *****************************************************************
       *************************** section patinoires ******************
       *****************************************************************
    """

    """
        Cette fonction permet de chercher un patinoire
        en particulier
    """

    def get_one_patinoire(self, name):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT * FROM patinoire WHERE nom like ?",
            (name,))
        patinoire = cursor.fetchall()
        return patinoire

    """
        Cette fonction permet de chercher les patinoires d'un arrondissement
        en particulier
    """

    def get_patinoires_of_arrondis(self, arrondis):
        cursor = self.get_connection().cursor()
        cursor.execute(
            "SELECT nom FROM patinoire WHERE "
            "REPLACE(LOWER(nom_arrondisse), ' ', '') like ?"
            "ORDER BY nom", ((arrondis.lower()).replace(
                " ", ""),))
        patinoires = cursor.fetchall()
        return patinoires

    """
        Cette fonction permet d'ajouter un nouveau patinoire
    """

    def add_patinoire(
            self,
            nom,
            nom_arrondisse,
            date_maj,
            ouvert,
            deblaye,
            arrose,
            resurface):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO patinoire(nom, nom_arrondisse, date_maj, ouvert,"
            " deblaye, arrose, resurface)"
            "VALUES(?,?,?,?,?,?,?)",
            (nom, nom_arrondisse, date_maj, ouvert, deblaye,
             arrose, resurface))
        connection.commit()

    """
        Cette fonction permet de modifier un patinoire
    """

    def update_patinoire(self, name, date, ouvert, deblaye, arrose, resurface):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE patinoire SET date_maj = ?, ouvert = ?, deblaye = ?,"
            " arrose = ?, resurface = ?"
            " WHERE nom = ?", (date, ouvert, deblaye, arrose, resurface, name))
        connection.commit()

    """
        Cette fonction permet de lister la liste des noms
        de tous les patinoires
    """

    def get_patinoires_by_nom(self):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT nom FROM patinoire ORDER BY nom")
        patinoires = cursor.fetchall()
        return patinoires

    """
        Cette fonction permet de lister toutes les informations
        de tous les patinoires
    """

    def get_all_patinoires(self):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM patinoire order by nom")
        patinoires = cursor.fetchall()
        return patinoires
