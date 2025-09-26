import tkinter as tk
from tictactoe import matrix, reset_matrix, replace, checkWinner, checkDraw, randomizer, printMatrix

symbol = 'X'
opposite = 'O'
if randomizer == 1:
    symbol, opposite = 'O', 'X'

root = tk.Tk()
root.title("Tic Tac Toe") 
root.geometry("800x500")
root.configure(bg="light gray")

# Title
label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 20), bg="light gray")
label.pack(pady=15)

# Turn indicator
turnLabel = tk.Label(root, text=f"{symbol}'s turn!", font=("Arial", 18), bg="light gray")
turnLabel.pack(pady=5)

# Board frame (where we use grid)
board_frame = tk.Frame(root, bg="light gray")
board_frame.pack(pady=20)


buttons = []

def create_buttons():
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(board_frame, text="_", width=5, height=2, font=("Arial", 24))
            btn.grid(row=i, column=j, padx=5, pady=5)
            row.append(btn)
        buttons.append(row)

def set_button_commands():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(command=lambda x=i, y=j, b=buttons[i][j]: button_click(x, y, b))

def button_click(x, y, btn):
    global symbol, opposite
    
    if matrix[x][y] == '_':
        replace(symbol, x, y)
        btn.config(text=symbol, state="disabled")

        if checkWinner(matrix, symbol):
            turnLabel.config(text=f"{symbol} wins!")
            disableAll()
            return
        elif checkDraw(matrix):
            turnLabel.config(text="It's a tie!")
            return
        symbol, opposite = opposite, symbol
        turnLabel.config(text=f"{symbol}'s turn!")

def disableAll():
    for row in buttons:
        for b in row:
            b.config(state="disabled")

def reset_game():
    global symbol, opposite 
    reset_matrix()
    printMatrix()
    for row in buttons:
        for b in row:
            b.config(text="_", state="normal")
    if randomizer == 1:
        symbol, opposite = 'O', 'X'
    else:
        symbol, opposite = 'X', 'O'
    turnLabel.config(text=f"{symbol}'s turn!")

resetButton = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset_game)
resetButton.pack()
resetButton.place(x=650, y=450)



# Create buttons and set their commands
create_buttons()
set_button_commands()

root.mainloop()
