"""Code pour vérifier si une chaine de caractère est un palindrome,
 c'est a dire se lit de la même manière de G à D et de D à G"""
import re
import unicodedata


def ispalindrome(p):
    """Verifie si une chaine de caracrère est un palindrome, renvoie vrai si c'est le cas"""
    verif=True
    # votre code ici
    sans_accent= ''.join(c for c in unicodedata.normalize('NFD', p)
                  if unicodedata.category(c) != 'Mn')
    sans_accent=sans_accent.lower().replace(" ","")

    filtre= re.sub(r'[^a-zA-Z0-9]','',sans_accent)

    for i in range (int(len(filtre)/2)) :
        if filtre[i]!=filtre[len(filtre)-i-1] :
            verif= False
    return verif

#### Fonction sans_accentrincisans_accentale


def main():
    """fonction executable"""
    # vos asans_accentsans_accentels à la fonction secondaire ici

    for s in ["Radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
