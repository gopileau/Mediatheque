Rapport du Travail Effectué:

1. L'étude et les Correctifs du Code Fourni
Pour commencer, j'ai pris le temps d'examiner attentivement le code qui m'a été fourni. Mon objectif était de comprendre son fonctionnement et d'identifier les problèmes potentiels. Voici ce que j'ai fait :

Erreurs de syntaxe : J'ai remarqué quelques erreurs de syntaxe, comme des imports manquants ou incorrects et des erreurs de nommage de fonctions. J'ai corrigé ces erreurs pour garantir le bon fonctionnement du code.
Modèles Django : Certains modèles Django n'étaient pas correctement définis. J'ai ajouté les champs manquants, établi les relations nécessaires entre les modèles et ajusté les paramètres pour qu'ils répondent aux besoins de l'application.
Gestion des URLs : Le fichier urls.py contenait des redondances et des erreurs. J'ai nettoyé ce fichier et organisé les URLs de manière plus logique et cohérente.
Commentaires explicatifs : J'ai également ajouté des commentaires explicatifs dans le code pour faciliter la compréhension et la maintenance future.
2. Mise en Place des Fonctionnalités Demandées
Pour répondre aux besoins de la médiathèque, j'ai mis en place les fonctionnalités suivantes :

-Création de membres-emprunteurs à l'aide du modèle Member.
-Affichage de la liste des membres.
-Mise à jour des informations des membres.
-Affichage de la liste des médias disponibles à l'emprunt.
-Création d'un nouvel emprunt pour un média disponible.
-Ajout d'un nouveau média dans la base de données.
-Retour d'un emprunt.
-Affichage de la liste de tous les médias pour les membres.

3. Stratégie de Tests:
Pour assurer la qualité du code et le bon fonctionnement de l'application, j'ai mis en place une stratégie de tests unitaires. Voici les principales catégories de tests :

-Test des Modèles : Ces tests vérifient le bon fonctionnement des modèles Django, notamment en ce qui concerne la création et la modification d'objets.
-Test des Vues : Ces tests vérifient que les vues de l'application répondent correctement aux requêtes HTTP.
-Test des Formulaires : Ces tests vérifient la validation des formulaires utilisés dans l'application, en simulant différentes soumissions de formulaires.
-Test des URLs : Ces tests vérifient que les URLs sont correctement configurées et dirigent les utilisateurs vers les bonnes vues.

4. Base de Données avec des Données Test
J'ai créé une base de données SQLite pour stocker les données de l'application. Cette base inclut des données de test pour chaque modèle, ce qui permet de tester les fonctionnalités de l'application dans un environnement contrôlé.

5. Instructions d'Exécution du Programme
Pour exécuter le programme sur n'importe quelle machine sans prérequis particuliers, suivez les étapes suivantes :

-Cloner le repository GitHub :
git clone https://github.com/gopileau/Mediatheque.git
-Installer Python et Django : Assurez-vous que Python et Django sont installés sur votre machine. Si ce n'est pas le cas, suivez les instructions sur les sites officiels de Python et Django.
-Activer un environnement virtuel :
python -m venv venv
ou
python3 -m venv venv
-Ensuite, activez l'environnement virtuel :
source venv/bin/activate
-Installer les dépendances :
pip install -r requirements.txt
-Appliquer les migrations :
python manage.py migrate
-Lancer le serveur de développement :
python manage.py runserver

Accéder à l'application : Ouvrez votre navigateur et accédez à http://127.0.0.1:8000/.
Ces instructions vous permettront d'exécuter l'application localement sur votre machine.
