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
#__FONCTIONS_________________________________________________________
#
#
#	- Print
#
print("ceci est un print()")
#	Affiche "ceci est un print()"
#
#
a = 3
print(a)
#	Affiche "3"
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
#
#
#
#
#
#
#
#
#
#
#
#
#	- Display curent Python version on the console
#
from platform import python_version
print("Python " + python_version())
#
#
#
#
#	- Display curent time on console
#
import datetime
print("Current date and time : ")
print(datetime.datetime.now(), "\n")
#
#
#
#
#	- Display curent time on console (formatted)
#
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")