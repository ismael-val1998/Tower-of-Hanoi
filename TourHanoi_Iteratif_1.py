"""
Fonction itérative qui resout le problème de la Tour de Hanoi

	Nous allons créer 3 piles( representent les bords) pour stocker les disques

		S : la pile du bord Source
		D : la pile du bord destination
		I : la pile du bord Intermédiaire

Ensuite le deplacement des disques suivra l'algo suivant :

1. Calculez le nombre total de coups possible, en caluclant PUISSANCE (2,n)
												avec n : nombre de disques.

2. Si le nombre de disques est pair, alors  on echange D et I

3. pour i = 1 au nombre total de coups  faire :

		si i%3 == 1 :
			mouvement légal du disque supérieur entre S et D

		si i%3 == 2 :
			mouvement légal disque supérieur  entre le S et I

		si ie%3 == 0 :
			mouvement légal disque supérieur  entre le I et D

"""


import sys

# Nous creeonsune classe pour représenter une pile ( Les 3 brords)

class Stack:

	# Constructeur de la classe pour intialiser notre pile

	def __init__(self, taille):
		self.taille = taille
		self.top = -1
		self.array = [0]*taille


# fonction pour créer une pile de capacité donnée.

def Creer_Pile(taille):
	stack = Stack(taille)
	return stack

#La pile est pleine lorsque le haut de la pile est égal au dernier index

def isFull(stack):
	return (stack.top == (stack.taille - 1))

#La pile est vide lorsque le haut de la pile a pour index -1

def isEmpty(stack):
	return (stack.top == -1)

# Fonction pour ajouter un élément dans la pile ( empiler )

def push(stack, element):
	if(isFull(stack)):
		return
	stack.top = stack.top + 1
	stack.array[stack.top] = element

# Fonction pour supprimer un élément de la pile ( Dépiler )

def Pop(stack):
	if(isEmpty(stack)):
		return -sys.maxsize
	Top = stack.top
	stack.top = stack.top - 1
	return stack.array[Top]

# Fonction qui implemente les mouvement autorisée entre 2 bords

def Deplacer_Disque_Entre_2_Bords(source, destination, s, d):
	Bord_Source = Pop(source)
	Bord_Destination = Pop(destination)

	# Mouvement lorsque le bord source est vide

	if (Bord_Source == -sys.maxsize):
		push(source, Bord_Destination)
		Deplacer_Disque(d, s, Bord_Destination)

	# Mouvement lorsque le bord destination est vide

	elif (Bord_Destination == -sys.maxsize):
		push(destination, Bord_Source)
		Deplacer_Disque(s, d, Bord_Source)

	# Mouvement lorsque le haut(top) du bord source  > haut(top) du bord destination

	elif (Bord_Source > Bord_Destination):
		push(source, Bord_Source)
		push(source, Bord_Destination)
		Deplacer_Disque(d, s, Bord_Destination)

	# Mouvement lorsque le haut(top) du bord source  < haut(top) du bord destination

	else:
		push(destination, Bord_Destination)
		push(destination, Bord_Source)
		Deplacer_Disque(s, d, Bord_Source)

# Fonction pour montrer le mouvement des disques

def Deplacer_Disque(De_la_source, A_la_destination, n):
	print("\nDeplacer le disque ", n, " De ", De_la_source, " Vers ", A_la_destination)

# Construction de la fonction qui implemente le jeu

def Tour_Hanoi_Iteratif(n, source, Intermediaire, destination):
	s, d, inter = 'S', 'D', 'I'

	# Si le nombre de disques est pair, alors échangez D et I

	if (n % 2 == 0):
		temp = d
		d = i
		i = temp

	# Calcule le nombre de coup possible (nombre de deplacement)

	Nb_Deplacement = int(pow(2, n) - 1)

	# Les disques plus grands seront poussés en premier

	for i in range(n, 0, -1):
		push(source, i)

	for i in range(1, Nb_Deplacement + 1):
		if (i % 3 == 1):
			Deplacer_Disque_Entre_2_Bords(source, destination, s, d)

		elif (i % 3 == 2):
			Deplacer_Disque_Entre_2_Bords(source, Intermediaire, s, inter)

		elif (i % 3 == 0):
			Deplacer_Disque_Entre_2_Bords(Intermediaire, destination, inter, d)


n = int(input ("\nSaisir le nombre de disques : ") )

print("\n**************************************")

source = Creer_Pile(n)
destination = Creer_Pile(n)
Intermediaire = Creer_Pile(n)

Tour_Hanoi_Iteratif(n, source, Intermediaire, destination)


