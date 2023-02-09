from ascii import title

# Start title(Ascii)
intro = "Let's start the game!!"
print(title)
print(intro)

# initialize setting 
tic_map = {1: {"a": "   ", "b": "   ", "c": "   "},
           2: {"a": "   ", "b": "   ", "c": "   "},
           3: {"a": "   ", "b": "   ", "c": "   "}}
player = 1
is_gameover = False
player1_mark = " ○ "
player2_mark = " × "
score1 = player1_mark + player1_mark + player1_mark
score2 = player2_mark + player2_mark + player2_mark
check_list = ["a", "b", "c"]

# draw tic tak toe map with row and column
def draw_map():
    print("      a   b   c ")
    for i, row in enumerate(tic_map.values()):
        print("-----------------")
        row_print = str(i+1) + ")  "
        for column in row.values():
            row_print = row_print + "|" + column
        print(row_print)

# check if input is appropriate
def check_input(letters):
    is_error = False
    letter_list = ["1", "2", "3", "a", "b", "c"]
    if len(letters) != 2:
        is_error = True
    else:
        for letter in letters:
            if letter not in letter_list:
                is_error = True
    return is_error

# ask for player input
def ask_input():
    input_row = input(f"Player{player}: which box do you choose? enter row: ")
    input_column = input("enter column: ")
    return input_row + input_column

# add check to appropriate box
def draw_input(player):
    entered_row = int(letters[0])
    entered_column = letters[1]
    if player == 1:
        tic_map[entered_row][entered_column] = player1_mark
        player = 2
    else:
        tic_map[entered_row][entered_column] = player2_mark
        player = 1
    return player

# check if there is a winner


def check_winner(is_gameover):
    for i in range(1, 3):
        if score1 == tic_map[i]["a"] + tic_map[i]["b"] + tic_map[i]["c"] or \
                score2 == tic_map[i]["a"] + tic_map[i]["b"] + tic_map[i]["c"] or \
                score1 == tic_map[1][check_list[i]] + tic_map[2][check_list[i]] + tic_map[3][check_list[i]] or \
                score2 == tic_map[1][check_list[i]] + tic_map[2][check_list[i]] + tic_map[3][check_list[i]]:
            is_gameover = True
        elif score1 == tic_map[1]["a"] + tic_map[2]["b"] + tic_map[3]["c"] or \
                score1 == tic_map[1]["c"] + tic_map[2]["b"] + tic_map[3]["a"] or \
                score2 == tic_map[1]["a"] + tic_map[2]["b"] + tic_map[3]["c"] or \
                score2 == tic_map[1]["c"] + tic_map[2]["b"] + tic_map[3]["a"]:
            is_gameover = True
    return is_gameover


while not is_gameover:
    # draw initial map
    draw_map()
    # ask for input
    letters = ask_input()
    # check input
    is_error = check_input(letters)
    while is_error:
        print("please re-enter")
        letters = ask_input()
        is_error = check_input(letters)
    # update map
    player = draw_input(player)
    draw_map()
    # check for win
    is_gameover = check_winner(is_gameover)
    
print("We have a winner!")
