
"""
Description :

    hanoi_iteratif(n,source,Intermediaire,destination)
    déplacer n disques de la tour source à la tour destination
    en utilisant la tour Intermediaire comme tour de transition
    Nous utilisons une liste pour stocker les différents états

"""

def hanoi_iteratif(n,source,Intermediaire,destination) :


    pile = []
    contexte = (n,source,Intermediaire,destination,"appel")
    pile.append(contexte)
    while pile != [] :
        (n,source,Intermediaire,destination,etat) = pile.pop()
        if n > 0 :
            if (etat == "appel") :
                pile.append((n,source,Intermediaire,destination,"retour"))
                pile.append((n-1,source,destination,Intermediaire,"appel"))
            else :
                deplacer(n,source,destination)
                pile.append((n-1,Intermediaire,source,destination,"appel"))


#deplacer(n,depart,arrivee)
#déplacer le disque n de la tour depart à la tour arrivé

def deplacer(n,depart,arrivee) :


    print("\nDeplacer le disque ", n ," de ", depart ," Vers ", arrivee)
    return



n = int(input ("\nSaisir le nombre de disques : ") )

print("\n****************************************")

hanoi_iteratif(n,"S","I","D")








