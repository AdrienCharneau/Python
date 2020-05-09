#
#
#
#
#__VARIABLES_________________________________________________________
#	
#
#	- Mots-clés réservés
"""

and, as, assert, break, class, continue, def, del, elif, else, except,
false,finally, for, from, global, if, import, in, is, lambda, none,
nonlocal, not, or, pass, raise, return, true, try, while, with, yield

"""
#
#
#	- Booleans
#
variableBoolean_1 = True
variableBoolean_2 = False
#
#
#	- Nombres entiers et flottants
#
variableEntier = 1
variableFloat = 1.25
#
#
#	- Chaîne de caractères
#
variableString_1 = '''Exemple de chaîne'''
variableString_2 = """Exemple de chaîne"""
variableString_3 = 'Exemple de chaîne avec \''
variableString_4 = "Exemple de chaîne avec \""

varibaleString_5 = """Exemple de chaîne
					avec tab et saut à la ligne"""
#
#
#	- Caractères spéciaux
"""

\t                    Tab
\\                    Inserts a back slash
\'                    Inserts a single quote
\"                    Inserts a double quote
\n                    Inserts a ASCII Linefeed (a new line)

"""
#
#
#	- Affectations multiples
#
x = y = 3
#	x est égal à 3
#	y est égal à 3
#
#
#
#
#	- Permutation
#
a = 5
b = 32
a,b = b,a
#	a est maintenant égal à 32
#	b est maintenant égal à 5
#
#
#
#
#	- Instruction sur plusieures lignes
#
variableLigne = 1 + 4 - 3 * 19 + 33 - 45 * 2 + (8 - 3) \
-6 + 23.5
#
#
#
#
#
#
#
#
#__INSTRUCTIONS CONDITIONNELLES______________________________________
#
#
"""
	<	Strictement inférieur à

	>	Strictement supérieur à

	<=	Inférieur ou égal à

	>=	Supérieur ou égal à

	==	Égal à

	!=	Différent de

	is 

	is not
"""
#
#
a = 5
#
if a > 0:
	print("a est supérieur à 0.")

#	Affiche "a est supérieur à 0" !!! Ne pas oublier d'utiliser une tabulation à l'intérieur du bloc et de sauter une ligne pour le fermer !!!
#
#
a = 5
b = 8
#
if a > 0:
    b += 1
    print("a = ",a,"et b = ",b)

#	Affiche "a = 5 et b = 8"
#
#
a = 5
#
if a > 0:
	print("a est supérieur à 0.")
else:
	print("a est inférieur ou égal à 0.")

#	Affiche "a est supérieur à 0."
#
#
a = 5
#
if a > 0:
	print("a est positif.")
elif a < 0:
	print("a est négatif.")
else:
	print("a est nul.")
#
#	Affiche "a est positif."
#
#
a = 5
#
if a >= 2 and a <= 8:
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")

#	Affiche "a est dans l'intervalle."
#
#
a = 5
#
if a < 2 or a > 8:
    print("a n'est pas dans l'intervalle.")
else:
    print("a est dans l'intervalle.")

#	Affiche "a est dans l'intervalle."
#
#
variableBoolean = False
#
if variableBoolean is not True:
	print("variableBoolean est False.")

#	Affiche "variableBoolean est False."
#
#
#
#
#
#
#
#
#__FONCTIONS_________________________________________________________
#
#
#	- Print
#
print("Hello World !")
#	Affiche "Hello World !"
#
#
a = 3
print(a)
#	Affiche "3"
#
#
from platform import python_version
print("Python " + python_version())
#	Affiche la version courante de Python
#
#
import datetime
print("Current date and time : ")
print(datetime.datetime.now(), "\n")
#	Affiche la date et l'heure courante
#
#
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")
#	Affiche la date et l'heure courante (formaté)
#
#
#
#
#	- Types
#
a = 3
print(type(a))
#	Affiche "<class 'int'>"
#
#
print(type(3.4))
#	Affiche "<class 'float'>"
#
#
print(type("string"))
#	Affiche "<class 'str'>"