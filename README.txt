Dans le dossier database se trouve tout les fichier python gérant la base de données : 
	-add_db pour les ajouts
	-delete_db pour les retrait
	-init_db pour initialiser notre ancienne base de données
	-models pour les modeles de la base de donnée
	-update_db pour mettre à jour les données
Templates :
	-addInternship pour ajouter des stages
	-addJob pour ajouter une occupation
	-addStudent pour ajouter un profil étudiant
	-detailedStudent pour avoir des détails sur l'étudiant
	-editUser pour éditer vos données / les données d'un élève
	-layout pour la barre de nav
	-listEnterprises pour la liste des Entreprises enregistrée
	-listStudents pour la liste des Etudiants
	-listTaf pour la list des tafs
	-login pour la page des connexions
	-promotion pour la liste des Promos
Static pour les images et les différents imports

Différent schéma d'utilisation prévue : 
1er : Un utilisateur possède déjà un profil :
Il se connecte, et peut regarder les autres alumnis. Il peut regarder les personnes qui ont fait une taf spécifiques entre certaines années, 
rechercher par promo, par entreprise dans laquelle les alumnis ont fait un stage. Il peut cliquer sur un profil pour avoir des détails. S'il
veut, il peut cliquer sur le nom du tuteur pour pouvoir le contacter.
Il peut éditer son profil et rajouter des occupations

2ème un admin :
Un admin peut gérer les entreprises, les pormos, les tafs et les étudiants

3ème : un utilisateur sans profil :
On suppose que les utilisateur utilise le CAS qui fait qu'ils ont un identifiant et un mdp même avant de créer un profil. Si il se connecte sans
avoir de profil , il créer tout d'abord un profil, puis un stage. Durant la création du stage, il peut choisir une entreprise, ou en créer une s'il
ne la trouve pas. C'est le même cas pour le tuteur. Une fois le stage créer, son profil est créé, avec comme seul occupation de mis alumni en actif.
Il pourra mettre à jour ses occupations après