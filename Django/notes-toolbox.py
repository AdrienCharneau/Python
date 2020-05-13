#__INTRODUCTION______________________________________________________
#
#
"""

	- Framework

		Django est un framework web écrit en Python, qui se veut complet tout 
		en facilitant la création d’applications web riches.  Ce n’est pas le 
		seul dans sa catégorie, nous pouvons compter d’autres frameworks 
		Python du même genre comme web2py, TurboGears, Tornado ou encore 
		Flask. Il a cependant le mérite d’être le plus exhaustif, 
		d’automatiser un bon nombre de tâches et de disposer d’une très 
		grande communauté.


	- Histoire

		Django est créé en 2003 dans une agence de presse, Lawrence 
		Journal-World, qui devait développer des sites web complets dans des 
		laps de temps très courts (d’où l’idée du framework). En 2005, cette 
		agence décide de proposer Django au grand public, le jugeant assez 
		mature pour être réutilisé n’importe où. Trois ans plus tard, la 
		fondation Django Software est créée par les fondateurs du framework 
		afin de pouvoir maintenir celui-ci et la communauté très active qui 
		l’entoure. Aujourd’hui, Django est utilisé par des sociétés du monde 
		entier, telles qu’Instagram, Pinterest, et même la NASA.


	- Don't repeat yourself

		Si Django est devenu très populaire, c’est notamment grâce à sa 
		philosophie qui a su séduire de nombreux développeurs et chefs de 
		projets. En effet, le framework prône le principe du « Don't repeat 
		yourself ».

		Django applique sa philosophie de plusieurs manières. Par exemple, 
		l’interaction avec une base de données se fait via un ensemble 
		d’outils spécialisés et très pratiques. Il est donc inutile de 
		perdre son temps à écrire directement des requêtes, car 
		Django le fait automatiquement. De plus, le framework inclut 
		des fonctionnalités diverses comme un espace membres, ou une 
		bibliothèque permettant la traduction de votre application 
		web en plusieurs langues.


	- Documentation

		https://docs.djangoproject.com/en/3.0/


	- Packages

		https://djangopackages.org/


	- Snippets

		https://djangosnippets.org/

"""
#
#
#
#
#
#
#
#
#__ARCHITECTURE______________________________________________________
#
#
#	- MVC
#
#		Le modèle MVC s’agit d’un modèle distinguant plusieurs rôles 
#		précis d’une application, qui doivent être accomplis. Comme 
#		son nom l’indique, l’architecture (ou « patron ») 
#		Modèle-Vue-Contrôleur est composée de trois entités 
#		distinctes, chacune ayant son propre rôle à remplir.
#
#
#	- Modèle
#
#		Le modèle représente une information enregistrée quelque 
#		part, le plus souvent dans une base de données. Il permet 
#		d’accéder à l’information, de la modifier, d’en ajouter une 
#		nouvelle, de la mettre à jour, etc. Il s’agit d’une interface 
#		supplémentaire entre votre code et la base de données.
#
#
#	- Vue
#
#		La vue est, comme son nom l’indique, la visualisation de 
#		l’information. C’est la seule chose que l’utilisateur peut 
#		voir. Non seulement elle sert à présenter une donnée, mais 
#		elle permet aussi de recueillir une éventuelle action de 
#		l’utilisateur (un clic sur un lien, ou la soumission d’un 
#		formulaire, par exemple).
#
#
#	- Controlleur
#
#		Le contrôleur prend en charge tous les événements de 
#		l’utilisateur (accès à une page, soumission d’un formulaire, 
#		etc.). Il se charge, en fonction de la requête de 
#		l’utilisateur, de récupérer les données voulues dans les 
#		modèles. Après un éventuel traitement de ces données, il 
#		transmet celles-ci à la vue, afin qu’elle s’occupe de les 
#		afficher.
#
#
#	- MVT
#
#		Django gère lui-même la partie contrôleur (gestion des 
#		requêtes du client, des droits sur les actions…). Ainsi, nous 
#		parlons plutôt de framework utilisant l’architecture MVT : 
#		Modèle-Vue-Template.
#
#
#
#
#
#
#
#
#__INSTALLATION______________________________________________________
#
#
#	- PIP
#
#		sudo apt-get install python3-pip
#		pip3 install Django==3.0
#		pip3 install Django --upgrade
#
#
#	- Test
#		
		#!/usr/bin/python3
		# -*-coding:Utf-8 -*
#
		import django
		print(django.get_version())
		#	Affiche '3.0' ou autre version
#
#
#	- Initialisation
#
#		cd /home/user/Projets/
#		python3 -m django startproject nom_du_projet
#
#
#
#
#
#
#
#
