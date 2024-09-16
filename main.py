#### Fonction secondaire:
'''
author : oscar.brault@edu.esiee.fr
'''
def isprime(p):
    """
    Détermine si le nombre est premier à l'aide de sa divisibilité face aux nombres tel que:
    Si divisible seulement par 1 et lui même alors il est premier
    Sinon non
    """
    if p==1:
        return False
    for i in range (2,p):
        if p%i == 0:
            return False
        return True
print(isprime(7))
#### Fonction principale
def main():
    """
    Renvoie les 100 premiers nombres
    """
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print(7)
if __name__ == "__main__":
    main()
