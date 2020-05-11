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
#__BOUCLES___________________________________________________________
#
#
#	- While
#
i = 0
#
while i < 10:
    print(i)
    i += 1

#
#
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'q' pour quitter : ")
    if lettre == "q":
        print("Fin de la boucle")
        break

#
#
i = 1
#
while i < 20: # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i

#
#
#
#
#	- For
#
chaine = "Hello World !"
#
for lettre in chaine:
    print(lettre)

#
#
chaine = "Hello World !"
#
for lettre in chaine:
    if lettre in "AEIOUYaeiouy":
        print(lettre)
    else:
        print("*")

#	Affiche les voyelles de la chaine de caractères "chaine"
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
def table(nb, max):
#
    i = 0
#
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

#
#
def table(nb, max=10):
#
    i = 0
#
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

#	Ici, si l'on décide de ne pas préciser le deuxième paramêtre lors de l'appel de la fonction, celui-ci sera égal à 0 par défaut
#
#
#
#
def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
#
fonc()
#	Affiche "a = 1 b = 2 c = 3 d = 4 e = 5"
#
fonc(4)
#	Affiche "a = 4 b = 2 c = 3 d = 4 e = 5"
#
fonc(3,5)
#	Affiche "a = 3 b = 5 c = 3 d = 4 e = 5"
#
fonc(b=8, d=5)
#	Affiche "a = 1 b = 8 c = 3 d = 5 e = 5"
#
fonc(b=35, c=48, a=4, e=9)
#	Affiche "a = 4 b = 35 c = 48 d = 4 e = 9"
#
#
#
#
def functionCarre(valeur):
    return valeur * valeur

print(functionCarre(5))
#	Affiche "25"
#
#
#
#
f = lambda x: x * x
#
print(f(4))
#	Affiche "16"
#
#
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
#
#
#
#
#	- Doctstring
#
def docstringFunction():
    """Voici le docstring de la fonction"""
    print("Hello World !")
 
help(docstringFunction)
#	Affiche "Voici le docstring de la fonction" dans une interface ("q" pour quitter)
#
#
#
#
#
#
#
#
#__MODULES & PACKAGES________________________________________________
#
#
import math
print(math.sqrt(16))
#	Affiche "4.0"
#
#
import math
help(math)
#	Affiche la docstring du module "math" ("Entrée" pour avancer d'une ligne, "Espace" pour avancer d'une page et "q" pour quitter)
#
#
import math as mathematiques
print(mathematiques.sqrt(25))
#	Affiche "5.0"
#
#
from math import sqrt
print(sqrt(16))
#	Affiche "4.0"
#
#
from math import *
print(sqrt(4))
#	Affiche "2.0"
#
#
#
#
if __name__ == "__main__":
    print("Hello World !")

#	La variable "__name__" est une variable qui existe dès le lancement de l'interpréteur. Si elle vaut "__main__", cela veut dire que le 
#	fichier appelé est le fichier exécuté. Autrement dit, si "__name__" vaut "__main__", vous pouvez mettre un code qui sera exécuté si 
#	le fichier est lancé directement comme un exécutable (et non importé dans un autre fichier).
#	=> Voir dossier "OpenClassrooms/exempleModules/"