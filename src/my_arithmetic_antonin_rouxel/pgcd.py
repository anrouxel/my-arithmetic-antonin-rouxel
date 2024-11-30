def pgcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux nombres entiers.

    Cette fonction utilise l'algorithme d'Euclide pour trouver le PGCD de deux nombres entiers a et b.

    :param a: Premier nombre entier.
    :type a: int
    :param b: Deuxième nombre entier.
    :type b: int
    :return: Le plus grand commun diviseur de a et b.
    :rtype: int
    """
    while b:
        a, b = b, a % b
    return a