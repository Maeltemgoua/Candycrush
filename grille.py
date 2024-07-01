import random

# Définir les dimensions de la grille en hauteur et en largeur
WIDTH = 6
HEIGHT = 6

# Définir les gemmes de la grille
CANDIES = ["ressources/gemmes/gemme_verte.png","ressources/gemmes/gemme_rouge.png","ressources/gemmes/gemme_jaune.png","ressources/gemmes/gemme_rose.png"]  # R: Rouge, G: Vert, B: Bleu, Y: Jaune, P: Violet


def generate_grid(width, height, elements):
    """Génère une grille avec des éléments aléatoires."""
    return [[random.choice(elements) for _ in range(width)] for _ in range(height)]

def remplissage_grid(grid):
    """Fait tomber les éléments pour remplir les cases vides."""
    width = len(grid[0])
    height = len(grid)

    for x in range(width):
        # Obtenir la colonne actuelle
        column = [grid[y][x] for y in range(height)]
        # Retirer les éléments None
        new_column = [candy for candy in column if candy is not None]
        # Ajouter des None en haut pour remplir la colonne
        new_column = [None] * (height - len(new_column)) + new_column

        for y in range(height):
            grid[y][x] = new_column[y]
def remove_element(grid, x, y):
    """Supprime un élément de la grille en mettant la case à None."""
    grid[y][x] = None
def detect_combinations(grid):
    """Détecte les combinaisons de 3 bonbons ou plus dans la grille."""
    to_remove = set()

    # Vérification des lignes
    for y in range(HEIGHT):
        for x in range(WIDTH - 2):
            if grid[y][x] == grid[y][x + 1] == grid[y][x + 2] and grid[y][x] is not None:
                to_remove.update([(y, x), (y, x + 1), (y, x + 2)])

    # Vérification des colonnes
    for x in range(WIDTH):
        for y in range(HEIGHT - 2):
            if grid[y][x] == grid[y + 1][x] == grid[y + 2][x] and grid[y][x] is not None:
                to_remove.update([(y, x), (y + 1, x), (y + 2, x)])

    return to_remove
def fill_empty_spaces(grid):
    """Remplit les espaces vides en ajoutant de nouveaux éléments en haut de la grille."""
    width = len(grid[0])
    height = len(grid)

    for x in range(width):
        for y in range(height):
            if grid[y][x] is None:
                # Remplir avec un nouveau bonbon aléatoire
                grid[y][x] = random.choice(CANDIES)