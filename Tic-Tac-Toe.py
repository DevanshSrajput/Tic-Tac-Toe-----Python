import tkinter

# Initialize global variables
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"
turns = 0
game_over = False

# Initialize scores
scoreX = 0
scoreO = 0

# Create window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)

# Label for turn indication
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_gray,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Labels for scores
score_label = tkinter.Label(frame, text=f"Score of X: {scoreX}\nScore of O: {scoreO}", font=("Consolas", 20), background=color_gray,
                            foreground="white")
score_label.grid(row=1, column=0, columnspan=3, sticky="we")

# Function to set tile and switch players
def set_tile(row, column):
    global curr_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player  # Mark the board

    # Switch player
    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = curr_player+"'s turn"

    # Check winner
    check_winner()

# Function to check for a winner or tie
def check_winner():
    global turns, game_over, scoreX, scoreO
    
    turns += 1

    # Check horizontally, vertically and diagonally for a winner
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            update_score(board[row][0]["text"])
            return

    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            update_score(board[0][column]["text"])
            return

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        update_score(board[0][0]["text"])
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        update_score(board[0][2]["text"])
        return

    # Check for tie
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

# Function to update scores based on the winner
def update_score(winner):
    global scoreX, scoreO
    if winner == playerX:
        scoreX += 1
    elif winner == playerO:
        scoreO += 1
    
    score_label.config(text=f"Score of X: {scoreX} Score of O: {scoreO}")

# Function to start a new game
def new_game():
    global turns, game_over

    turns = 0
    game_over = False
    label.config(text=curr_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

# Setup buttons and layout
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue,
                                            width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+2, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
button.grid(row=5, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window on screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()