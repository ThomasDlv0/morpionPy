import tkinter

def check_null():
    print("Match null")

def print_winner():
    global win
    if  win is False:
        win = True
        print(f"Le joeur {current_playeur} a gagné le jeu")


def switch_playeur():
    global current_playeur

    if  current_playeur == "X":
        current_playeur = "O"
    else:
        current_playeur = "X"

def check_win(clicked_row, clicked_col):
    # detecter la victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]

        if  current_button["text"] == current_playeur:
            count += 1
        if count == 3:
            print_winner()

    # detecter la victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]

        if current_button["text"] == current_playeur:
            count += 1
        if count == 3:
            print_winner()

# detecter la victoire diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]

        if current_button["text"] == current_playeur:
            count += 1
        if count == 3:
            print_winner()

# detecter la victoire diagonale inverse
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]

        if current_button["text"] == current_playeur:
            count += 1
        if count == 3:
            print_winner()

        if win is False:
            count = 0
            for col in range(3):
                for row in range(3):
                    current_button = buttons[col][row]
                    if current_button["text"] == "X" or current_button["text"] == "O":
                        count += 1
            if count == 9:
                check_null()


def place_symbol(row, column):
    print("click", row, column)

    clicked_button = buttons[column][row]
    if  clicked_button["text"] == "":
        clicked_button.config(text=current_playeur)

    check_win(row, column)
    switch_playeur()

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width="5",
                height="3",
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# stocker dans les variables
buttons = []
current_playeur = "X"
win = False

# Créer la fenêtre du jeu
root = tkinter.Tk()

# Personnalisation de la fenêtre
root.title("Morpion")
root.minsize(500, 500)
draw_grid()
root.mainloop()

