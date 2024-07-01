""" Pour le jeu, nous allons commencer par créer une fonction
devant implementer la grille de jeu"""

from random import randrange

# orientation de la grille selon les vues
NORD, EST, SUD, OUEST = 0, 1, 2, 3
def create(lin, col, init):
    """
        Retourne une grille de `lin` lignes de `col` colonnes avec des valeurs `init`.

        :param lin: Nombre de lignes de la grille.
        :param col: Nombre de colonnes de la grille.
        :param init: Valeur initiale pour chaque élément de la grille.
        :return: Une grille de dimensions `lin` x `col` avec des valeurs `init`.
        """
    return [[init] * col for _ in range(lin)]
def create_alea(lin, col, mini=10, maxi=100):
    """Retourne une grille de dimensions 'lin', de nombres de colonnes 'col' avec des valeurs aléatoires
    comprises entre min et max."""
    return [[randrange(mini, maxi) for _ in range(col)] for _ in range(lin)]

def create_alea_lettres(lig,col):
    """
        Retourne une grille de dimensions `lig` x `col` avec des lettres majuscules aléatoires.

        :param lig: Nombre de lignes de la grille.
        :param col: Nombre de colonnes de la grille.
        :return: Une grille de dimensions `lig` x `col` avec des lettres majuscules aléatoires.
        """
    tab = create_alea(lig,col,65,90)
    for line in tab:
        for i in range(len(line)):
            line[i] = chr(line[i])
    return tab
def shape(tab):
    """
        Retourne les dimensions de la grille `tab`.

        :param tab: Une grille (liste de listes).
        :return: Un tuple (nb_lig, nb_col) représentant le nombre de lignes et de colonnes.
        """
    nb_lig = len(tab)  # la taille de la grille
    nb_col = len(tab[0]) if nb_lig else 0
    return nb_lig, nb_col
def line_str(tab, i):
    """
        Retourne une chaîne de caractères représentant la ligne `i` de la grille `tab`.

        :param tab: Une grille (liste de listes).
        :param i: Index de la ligne à afficher.
        :return: Une chaîne formatée représentant la ligne `i`.
        """
    return '|\t' + '\t'.join(str(val) for val in tab[i]) + '\t|'


def to_str(tab):
    """
     Retourne une chaîne de caractères représentant la grille `tab`.

     :param tab: Une grille (liste de listes).
     :return: Une chaîne formatée représentant la grille.
     """
    res = ''
    for i in range(len(tab)):
        res += '\n' + line_str(tab, i)
    return res


def line(tab, i):
    """
       Retourne la ligne `i` de la grille `tab`.

       :param tab: Une grille (liste de listes).
       :param i: Index de la ligne à extraire.
       :return: La ligne `i` de la grille.
       """
    return tab[i]


def column(tab, j):
    """
       Retourne la colonne `j` de la grille `tab`.

       :param tab: Une grille (liste de listes).
       :param j: Index de la colonne à extraire.
       :return: La colonne `j` de la grille sous forme de liste.
       """
    return [line[j] for line in tab]


def diago(tab):
    """
       Retourne la diagonale principale de la grille `tab`.

       :param tab: Une grille (liste de listes).
       :return: La diagonale principale de la grille sous forme de liste.
       """
    nb_lig, nb_col = shape(tab)
    size = min(nb_lig, nb_col)
    return [tab[i][i] for i in range(size)]


def anti_diago(tab):
    """
        Retourne l'antidiagonale de la grille `tab`.

        :param tab: Une grille (liste de listes).
        :return: L'antidiagonale de la grille sous forme de liste.
        """
    nb_lig, nb_col = shape(tab)
    size = min(nb_lig, nb_col)
    return [tab[i][nb_col - i - 1] for i in range(size)]


def identite(tab, val):
    """
        Vérifie si toutes les valeurs de la grille `tab` sont égales à `val`.

        :param tab: Une grille (liste de listes).
        :param val: Valeur à comparer.
        :return: True si toutes les valeurs de `tab` sont égales à `val`, False sinon.
        """
    return all([all([i == val for i in line]) for line in tab])


def is_square(tab):
    """
       Vérifie si la grille `tab` est carrée (même nombre de lignes et de colonnes).

       :param tab: Une grille (liste de listes).
       :return: True si `tab` est carrée, False sinon.
       """
    nb_lig, nb_col = shape(tab)
    return nb_lig == nb_col


def count(tab, val):
    """
     Compte le nombre d'occurrences de `val` dans la grille `tab`.

     :param tab: Une grille (liste de listes).
     :param val: Valeur à compter.
     :return: Le nombre d'occurrences de `val` dans `tab`.
     """
    return sum(line.count(val) for line in tab)


def add(tab):
    """
       Calcule la somme de tous les éléments de la grille `tab`.

       :param tab: Une grille (liste de listes).
       :return: La somme de tous les éléments de `tab`.
       """
    return sum(sum(line) for line in tab)


def case_to_lc(tab, num_case):
    """
       Convertit des coordonnées (num_lig, num_col) en numéro de case correspondant.

       :param tab: Une grille (liste de listes).
       :param num_lig: Numéro de la ligne.
       :param num_col: Numéro de la colonne."""
    _, nb_col = shape(tab)
    return num_case // nb_col, num_case % nb_col


def lc_to_case(tab, num_lig, num_col):
    """converti les coordonnées (``num_lig``, ``num_col``) de ``tab`` vers le numéro de case correspondant."""
    return num_lig * shape(tab)[1] + num_col


def set_case(tab, num_case, val):
    """Positionne la valeur ``val`` en ``num_case`` dans ``tab`` ."""
    lig, col = case_to_lc(tab, num_case)
    tab[lig][col] = val


def get_case(tab, num_case):
    """ extrait la valeur de ``tab`` en ``num_case``."""
    lig, col = case_to_lc(tab, num_case)
    return tab[lig][col]


def cases(tab, val):
    """Fournit la liste des numéros des cases à valeur égale à val dans ``tab``"""
    nb_lig, nb_col = shape(tab)
    return [i for i in range(nb_lig * nb_col) if get_case(tab, i) == val]


def lig_col_next(tab, lig, col, direction=NORD, tore=False):
    """calcule la paire (ligne, colonne) suivant (``lig``, ``col``) dans ``tab`` dans la direction ``direction``
        si ``tore`` est True, le dépassement des limites est géré en considérant la grilles comme un tore
        si ``tore`` est False, le dépassement des limites produit -1
    """
    nb_lig, nb_col = shape(tab)
    new_lig, new_col = lig, col
    if direction == NORD:
        if not tore and lig == 0:
            return -1
        new_lig, new_col = (lig - 1) % nb_lig, col
    if direction == EST:
        if not tore and col == nb_col - 1:
            return -1
        new_lig, new_col = lig, (col + 1) % nb_col
    if direction == SUD:
        if not tore and lig == nb_lig - 1:
            return -1
        new_lig, new_col = (lig + 1) % nb_lig, col
    if direction == OUEST:
        if not tore and col == 0:
            return -1
        new_lig, new_col = lig, (col - 1) % nb_col
    return new_lig, new_col


def num_case_next(tab, num_case, direction=NORD, tore=False):
    """calcule le numéro de la case d'arrivée suivante dans ``tab`` dans la direction ``direction``
        si ``tore`` est True, le dépassement des limites est géré en considérant la grilles comme un tore
        si ``tore`` est False, le dépassement des limites produit -1
    """
    lig, col = case_to_lc(tab, num_case)
    val = lig_col_next(tab, lig, col, direction, tore)
    if val == -1:
        return val
    return lc_to_case(tab, val[0], val[1])


def jump(tab, num_case, direction=NORD, tore=False, nb_cases=1):
    """calcule le numéro de la case d'arrivée ``num_case`` + ``nb_case`` dans ``tab`` dans la direction ``direction``
        si ``tore`` est True, le dépassement des limites est géré en considérant la grilles comme un tore
        si ``tore`` est False, le dépassement des limites produit -1
    """
    for _ in range(nb_cases):
        num_case = num_case_next(tab, num_case, direction, tore)
    return num_case


if __name__ == '__main__':
    assert create(3, 4, 'X') == [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]

    assert shape(create_alea(5, 6)) == (5, 6)

    assert line_str(create(3, 4, 0), 1) == '|\t0\t0\t0\t0\t|'
    assert to_str(create(3, 4, 0)) == '\n|\t0\t0\t0\t0\t|\n|\t0\t0\t0\t0\t|\n|\t0\t0\t0\t0\t|'

    grille_test = create(6, 5, 1)
    grille_test[2][1] = 5
    grille_test[1][3] = 6
    grille_test[3][3] = 7

    assert line(grille_test, 2) == [1, 5, 1, 1, 1]
    assert column(grille_test, 3) == [1, 6, 1, 7, 1, 1]
    assert diago(grille_test) == [1, 1, 1, 7, 1]
    assert anti_diago(grille_test) == [1, 6, 1, 1, 1]

    assert identite(create(4, 3, 0), 0)

    assert is_square(create(3, 3, 0))
    assert not is_square(create(3, 4, 0))

    assert count(grille_test, 1) == 27
    assert add(grille_test) == 45

    assert case_to_lc(grille_test, 11) == (2, 1)
    assert lc_to_case(grille_test, 2, 1) == 11

    set_case(grille_test, 9, 5)
    assert get_case(grille_test, 9) == 5
    print(to_str(grille_test))

    assert cases(grille_test, 5) == [9, 11]

    assert lig_col_next(grille_test, 1, 4, SUD, True) == (2, 4)
    assert lig_col_next(grille_test, 1, 4, EST, True) == (1, 0)
    assert lig_col_next(grille_test, 1, 4, EST) == -1

    assert num_case_next(grille_test, 29, SUD, True) == 4
    assert num_case_next(grille_test, 29, EST, True) == 25
    assert num_case_next(grille_test, 29, EST) == -1

    assert jump(grille_test, 6, EST, False, 4) == -1
    assert jump(grille_test, 6, EST, True, 4) == 5
