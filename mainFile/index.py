from customtkinter import CTk, CTkButton, CTkEntry, StringVar

zone_txt = ""

# Initialiser l'interface graphique
root = CTk()
root.title("YL-Calculateur")
root.geometry("375x300")

# Créer StringVar après l'initialisation de root
affichage = StringVar()

# Fonction pour gérer l'entrée de texte
def txt(input_txt):
    """
    Géstion d'entrée de texte (verification,modification zone_txt,ajout)
    txt (input_txt:String) : void | null
    """
    global zone_txt

    # Vérifier si les caractères spéciaux sont saisis dans un contexte valide
    if input_txt in ['%', '!', '²']:
        if not zone_txt or not zone_txt[-1].isdigit():
            return  

    # Gérer la saisie de la racine carrée
    if input_txt == '√':
        if zone_txt and (zone_txt[-1].isdigit() or zone_txt[-1] in ['%', '!', '²']):
            return 

    # Empêcher la répétition des opérateurs mathématiques
    if zone_txt and zone_txt[-1] in ['+', '-', 'x', '÷', '.']:
        if input_txt in ['+', '-', 'x', '÷', '.']:
            return 
    
    # Supprimer le dernier caractère si "~" est saisi
    if input_txt == '~':  
        zone_txt = zone_txt[:-1]
    else:
        zone_txt += input_txt

    # Mettre à jour l'affichage
    affichage.set(zone_txt)

# Fonction pour changer le signe (+/-) d'un nombre
def toggle_sign():    
    """
    Basculer entre le signe positif ou négatif si zone_txt contient uniquement des nombres.
    toggle_sign() : void
    """
    global zone_txt
    try:
        if zone_txt.lstrip('-').isdigit():
            if zone_txt.startswith('-'):
                zone_txt = zone_txt[1:]  # Supprimer le signe "-"
            else:
                zone_txt = '-' + zone_txt  # Ajouter le signe "-"
            affichage.set(zone_txt)
        else:
            affichage.set("Erreur")  # Afficher une erreur si l'entrée est invalide
    except Exception:
        affichage.set("Erreur")
        zone_txt = ""

# Fonction pour calculer l'inverse d'un nombre
def reciprocal():
    """
    Calcule l'inverse d'un nombre saisi dans la zone_txt.
    reciprocal() : void
    """
    global zone_txt
    try:
        if zone_txt.isdigit():
            zone_txt = str(1 / float(zone_txt))
            affichage.set(zone_txt)
        else:
            affichage.set("Erreur")
    except Exception:
        affichage.set("Erreur")

# Fonction pour calculer la racine carrée d'un nombre
def square_root():
    """
    Calcule la racine carrée du nombre actuellement saisi dans la zone_txt.
    square_root() : void
    """
    global zone_txt
    try:
        if zone_txt.isdigit():
            zone_txt = str(float(zone_txt) ** 0.5)
            affichage.set(zone_txt)
        else:
            affichage.set("Erreur")
    except Exception:
        affichage.set("Erreur")

# Fonction pour calculer le carré d'un nombre
def square():
    """
    Calcule le carré du nombre actuellement saisi dans la zone_txt.
    square() : void
    """
    global zone_txt
    try:
        if zone_txt.isdigit():
            zone_txt = str(float(zone_txt) ** 2)
            affichage.set(zone_txt)
        else:
            affichage.set("Erreur")
    except Exception:
        affichage.set("Erreur")

# Fonction pour effacer le texte actuel
def clear():
    """
    Efface complètement la zone_txt.
    clear() : void
    """
    global zone_txt
    zone_txt = ""
    affichage.set(zone_txt)

# Fonction pour calculer la factorielle d'un nombre
def fraction(n):
    """
    Calcule la factorielle d'un nombre donné.
    fraction(n : int) : int
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Fonction pour effectuer les calculs à partir de l'expression actuelle
def calcul():
    """
    Évalue l'expression mathématique dans la zone_txt et affiche le résultat.
    calcul() : void
    """
    global zone_txt

    try:
        # Remplacer les symboles pour permettre l'évaluation de l'expression
        expression = zone_txt.replace('x', '*').replace('÷', '/').replace('²', '**2')
        expression = expression.replace('√', '**(1/2)').replace('%', '/100')

        # Vérifier la présence de la factorielle
        if '!' in expression:
            number = int(expression.replace('!', ''))
            result = fraction(number)
        else:
            result = eval(expression)

        zone_txt = str(result)
        affichage.set(zone_txt)

    except Exception:
        affichage.set("Erreur")
        zone_txt = ""

# Fonction pour gérer les événements de saisie clavier
def handle_keypress(event):
    """
    Gère les événements clavier et appelle les fonctions spécifiques en fonction des touches pressées.
    handle_keypress(event) : void
    """
    global zone_txt
    key = event.char  # Le caractère de la touche appuyée
    keysym = event.keysym  # Le nom symbolique de la touche (par ex., "BackSpace")

    # Gérer la saisie des chiffres
    if key.isdigit():
        txt(key)
    # Gérer les opérateurs (+, -, %, ., !)
    elif key in ['+', '-', '%', '.', '!']:
        if not zone_txt or zone_txt[-1] in ['+', '-', 'x', '÷', '.', '!']:
            pass  # Ignorer les symboles consécutifs invalides
        else:
            txt(key)
    # Gérer la multiplication
    elif key in ['x', 'X', '*']:
        if not zone_txt or zone_txt[-1] in ['+', '-', 'x', '÷', '.', '!']:
            pass  # Ignorer les séquences invalides
        else:
            txt('x')
    # Gérer la division
    elif key in ['/']:
        if not zone_txt or zone_txt[-1] in ['+', '-', 'x', '÷', '.', '!']:
            pass  # Ignorer les séquences invalides
        else:
            txt('÷')
    # Basculer le signe avec 'p'
    elif key in ['p']:
        if not zone_txt or not zone_txt.isdigit():
            pass  # Ignorer si le nombre n'est pas valide
        else:
            toggle_sign()
    # Calculer la racine carrée avec 'r'
    elif key in ['r']:
        if not zone_txt or not zone_txt[-1].isdigit():
            pass  # Ignorer si non valide
        else:
            square_root()
    # Calculer le carré avec 'q' ou '^'
    elif key in ['q', '^']:
        if not zone_txt or not zone_txt[-1].isdigit():
            pass  # Ignorer si non valide
        else:
            square()
    # Calculer l'inverse avec '/'
    elif key in ['/']:
        if not zone_txt or not zone_txt.isdigit():
            pass  # Ignorer si non valide
        else:
            reciprocal()
    # Gérer l'appui sur Entrée ou '='
    elif key in ['=', '\r']:
        calcul()
    # Gérer l'effacement avec 'c' ou 'C'
    elif key in ['c', 'C']:
        clear()
    # Gérer la touche Backspace ou Delete
    elif keysym in ["BackSpace", "Delete"]:
        txt("~")
    # Ignorer les autres touches
    else:
        pass  # Entrée invalide ignorée

# Entrée pour afficher les calculs
CTkEntry(root, textvariable=affichage, font=("Arial", 24), justify="right", width=360).grid(row=0, column=0, columnspan=4, pady=10)

# Disposition des boutons
buttons = [
    ["%", "√", "C", "⌫"],
    ["1/x", "²", "x!", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

# Assignation des commandes aux boutons
commands = [
    [lambda: txt("%"), square_root, clear, lambda: txt("~")],
    [reciprocal, square, lambda: txt("!"), lambda: txt("÷")],
    [lambda: txt("7"), lambda: txt("8"), lambda: txt("9"), lambda: txt("x")],
    [lambda: txt("4"), lambda: txt("5"), lambda: txt("6"), lambda: txt("-")],
    [lambda: txt("1"), lambda: txt("2"), lambda: txt("3"), lambda: txt("+")],
    [toggle_sign, lambda: txt("0"), lambda: txt("."), calcul]
]

# Création des boutons dans la grille
for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        if label:
            CTkButton(root, text=label, command=commands[r][c], font=("Arial", 20), width=80).grid(row=r + 1, column=c, padx=7, pady=5)

# Lier les événements de touches clavier
root.bind("<Key>", handle_keypress)  # Touches générales
root.bind("<BackSpace>", handle_keypress)  # Touche Suppr
root.bind("<Delete>", handle_keypress)  # Touche ⌫

root.mainloop()


    #^                                                             YL-Calculateur
    #^                                                          ____________________
    #^                                                         |___________________|
    #^                                                         | %    CE   C    ⌫ |
    #^                                                         | 1/X  x²   ²√x  ÷ |
    #^                                                         | 7    8    9    X |
    #^                                                         | 4    5    6    - |
    #^                                                         | 1    2    3    + |
    #^                                                         | +/-  0    ,    = |
    #^                                                         ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾