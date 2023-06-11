## Cours INF5190 - Hiver 2022
### Nom et prénom : BEN LAMIN SOUKAINA
### Code permanent : 
### Les fonctionnalités développées :
- #### A1 :
```
Cette fonctionnalité a été bien implémentée, pour pouvoir la tester, 
vous pouvez simplement consulter la base de données qui existe dans 
le répertoire db/,en exécutant des requettes SQL dans 
l'invite de commande sqlite3. 
Exemple : 
    commande pour se connecter à la base: 
        sqlite3 db.db
    commande pour lister tous les installations de type glissades :
        SELECT * FROM glissade; 
```
- #### A2 :
```
Cette fonctionnalité a été bien implémenté, l'importation des données de 
point A1 se fait chaque jour à minuit, pour faire des tests, vous devez 
changer l'heure et minutes dans le cron job.
Exemple : 
    scheduler.add_job(import_data, 'cron', args=(get_db(),), day_of_week='mon-sun', hour=14, minute=2)
Remarque :
    Il est important de savoir que la base de données contenue dans le 
    répertoire db/ est récente et remplie, donc c'est possible, que vous ne remarquez aucun 
    changement lors l'imporation des données et le travail de Background scheduler.
    Alors, si vous voulez voir toutes les détails d'imporations, il suffit que vous créer
    une autre base de données et de la transmettre comme paramétre pour le
    cron job 
```
- #### A3 :
```
Cette fonctionnalité est bien implémenté, pour la tester il suffit de démarrer
l'application comme mentionné dans le fichier README.md, et ensuite accéder
à l'application via l'adresse ip de serveur suivi de port 5000. 
vous pouvez visualiser la liste de documentation des servies API en cliquant sur le lien 
"documentation" dans le menu ou bien d'utiliser l'url "/doc"
```
- #### A4 :
```
Cette fonctionnalité est bien implémenté, pour tester ce point, il suffit d'accéder à l'url 
du service api et de lui donnéer des queryParameters
Exemple : 
    adresse IP de serveur + numero de port +/api/installations?arrondissement=LaSalle
```
- #### A5 :
```
Cette fonctionnalité est bien implémenté, pour faire des tests, vous devez accéder au 
"/" de l'application et effectuer des recherches dans le formulaire présenté dans la page d'accueil.
```
- #### A6 :
```
Cette fonctionnalité est bien implémenté, pour tester, il faut que vous accéder à la page d'accueil et 
ensuite utiliser les buttons radios et le select pour lancer la recherche.
```
- #### F1 :
```
L'application a été bien déployé dans la plateforme infonuagique Heroku. 
pour visualiser le résultat cliquez sur le lien ci-dessous  : 
``` 
##### lien de l'application sur Heroku : [https://project-inf5190.herokuapp.com/](https://project-inf5190.herokuapp.com/)

- #### B1 :
```
Cette fonctionallité a été bien implémenté, pour faire des tests ils suffit que vous ajouter 
votre courriel dans le fichier "emails.yml" qui existe dans le dossier static de l'application,
ensuite, vous devez adapter la date et heure pour l'importation de données du Point A2, puis, 
vous lancer l'application

REMARQUE IMPORTANTE : 
    - Si vous allez utiliser la base de données que je vous ai fournis dabs le répertoire db/, alors
    c'est POSSIBLE que vous ne recevrez aucun email de la part de l'application, car tout simplement
    il y'aura pas des nouvelles installations, par contre, si il y'en a des nouvelles installations
    vous allez recevoir une liste contenant les de ces installations.
    - Dans le cas, d'aucune nouveauté dans la base de données vous devez créer une nouvelle base de données
    (ou supprimer celle qui existe et de la regénérer de nouveau)  et vous lancer le point A2. Mais, il faut supprimer
     la partie de poster des Tweets sur Twitter, car dans ce cas on aura plus de 1000 nouvelles installations, 
     du coup on va dépasser la limite de nombre de tweets par jours dans Twitter.
``` 

- #### B2 :
```
Cette fonctionnalité a été bien implémenté, pour faire des tests il suffit d'Ajuster 
l'heure et minutes de cron job de fonctionnalité A2 et de lancer l'application.

REMARQUE IMPORTANTE :
     - Si vous allez utiliser la base de données que je vous ai fournis dabs le répertoire db/, alors
    c'est POSSIBLE que la fonctionnalité ne poste aucun tweet, car tout simplement
    il y'aura pas des nouvelles installations, par contre, si il y'en a des nouvelles installations
    vous allez voir dans la page profil, les nouveaux postes de tweets.
    - Dans le cas, d'aucune nouveauté dans la base de données vous devez créer une nouvelle base de données
    (ou supprimer celle qui existe et de la regénérer de nouveau)  et vous lancer le point A2. Mais, il faut savoir
     la partie de poster des Tweets sur Twitter ne peut pas poster tous les nouveaux installations, car dans ce cas on aura 
     plus de 1000 nouvelles installations, du coup on va dépasser la limite de nombre de tweets par jours dans Twitter.

LE COMPTE TWITTER :
    Voir ci-dessous
```
##### Le lien vers la page profil de compte Twitter : https://twitter.com/INF5190_H22
##### Crédentiels du Compte Twitter : 
    - Courriel : ******@gmail.com
    - Mot de passe : ******.

- #### C1 :
```
Cette fonctionnalité a été bien implémenté, pour tester vous pouvez consulter le lien 
"Les installations en JSON" dans le menu de l'application.
```
- #### C2 :
```
Cette fonctionnalité a été bien implémenté, pour tester vous pouvez consulter le lien 
"Les installations en XML" dans le menu de l'application.
```
- #### C3 :
```
Cette fonctionnalité a été bien implémenté, pour tester vous pouvez consulter le lien 
"Les installations en CSV" dans le menu de l'application.
```



