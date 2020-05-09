#	
#
#	Mots-clés réservés
"""

and, as, assert, break, class, continue, def, del, elif, else, except,
false,finally, for, from, global, if, import, in, is, lambda, none,
nonlocal, not, or, pass, raise, return, true, try, while, with, yield

"""
#
#
#	Nombres entiers et flottants
#
variableEntier = 1
variableFloat = 1.25
#
#
#	Chaîne de caractères
#
variableString_1 = """Exemple de chaîne"""
variableString_2 = 'Exemple de chaîne avec \''
variableString_3 = "Exemple de chaîne avec \""

varibaleString_4 = """Exemple de chaîne
					avec tab et saut à la ligne"""
#
#
#	Caractères spéciaux
"""

\t                    Tab
\\                    Inserts a back slash
\'                    Inserts a single quote
\"                    Inserts a double quote
\n                    Inserts a ASCII Linefeed (a new line)

"""
#
#
#
#
#	Display curent Python version on the console
#
from platform import python_version
print("Python " + python_version())
#
#
#
#
#	Display curent time on console
#
import datetime
print("Current date and time : ")
print(datetime.datetime.now(), "\n")
#
#
#
#
#	Display curent time on console (formatted)
#
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")