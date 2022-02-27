
"""
Description :

    Fonction récursive qui resout le problème de la Tour de Hanoi

    Nous avons à notre disposition n disques et 3 Bords :
        S : le bord Source
        D : le bord de destination
        I : le bord Intermédiaire

    Pour n = 0      =>  on ne renvoie rien

    Pour n > 0      =>  Nous faisons deux appels récursifs

Le but du jeu :

    c'est déplacer tous les disques du bord source (S)
    vers le bord de destination (D) en passant par le bord intermédiaire (I)

    Notons egalement qu'au début, les disques sont rangés dans l'ordre grand
    au plus petit en partant du bas vers le haut.

    Exemple : pour n = 3, le bord de départ S est comme suit : [3, 2, 1]
              => 1 au dessus de et 2 est lui aussi au dessus de 3

"""


import time         # Pour mesurer le temps d'éxéxution du programme


debut = time.time() # temps initial
end = time.time() # temps final

def Tour_Hanoi_Recursif(n , source, destination, Intermediaire):

    if n == 0:
            return

    #Premier appel

    Tour_Hanoi_Recursif(n-1, source, Intermediaire, destination)

    # On deplace l'element qui est au dessus du bord vers un autre

    print("\nDeplacer le disque ", n ," de ", source ," Vers ", destination)

    #Deuxième appel

    Tour_Hanoi_Recursif(n-1, Intermediaire, destination, source)

    global end



n = int(input ("\nSaisir le nombre de disques : ") )

print("\n****************************************")

Tour_Hanoi_Recursif(n,'S','D','I')

print("\n****************************************")

print("Temps d'éxécution du programme :" +  str( round(end-debut, 10)) )
