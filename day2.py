import io

def gamescore(score, player1, player2):
    '''
    calculates score of a single rock paper scissors turn
    '''
    game_dict_player1 = {"A": 1, "B": 2, "C": 3}
    game_dict_player2 = {"X": 1, "Y": 2, "Z": 3}
    win = 6
    draw = 3
    if game_dict_player1[player1] == game_dict_player2[player2]:
        score += draw + game_dict_player2[player2]
    elif game_dict_player1[player1] == 1 and game_dict_player2[player2] == 3:
        score += game_dict_player2[player2] 
    elif game_dict_player1[player1] == 2 and game_dict_player2[player2] == 1:
        score += game_dict_player2[player2] 
    elif game_dict_player1[player1] == 3 and game_dict_player2[player2] == 2:
        score += game_dict_player2[player2] 
    elif game_dict_player2[player2] == 1 and game_dict_player1[player1] == 3:
        score += win + game_dict_player2[player2] 
    elif game_dict_player2[player2] == 2 and game_dict_player1[player1] == 1:
        score += win + game_dict_player2[player2] 
    elif game_dict_player2[player2] == 3 and game_dict_player1[player1] == 2:
        score += win + game_dict_player2[player2] 
    return score

def strategy(player1, player2):
    game_dict_player1 = {"A": 1, "B": 2, "C": 3}
    game_dict_player2 = {"X": 1, "Y": 2, "Z": 3}
    if game_dict_player1[player1] == 1 and game_dict_player2[player2] == 1:
        return "Z"
    if game_dict_player1[player1] == 1 and game_dict_player2[player2] == 2:
        return "X"
    if game_dict_player1[player1] == 1 and game_dict_player2[player2] == 3:
        return "Y"
    if game_dict_player1[player1] == 2 and game_dict_player2[player2] == 1:
        return "X"
    if game_dict_player1[player1] == 2 and game_dict_player2[player2] == 2:
        return "Y"
    if game_dict_player1[player1] == 2 and game_dict_player2[player2] == 3:
        return "Z"
    if game_dict_player1[player1] == 3 and game_dict_player2[player2] == 1:
        return "Y"
    if game_dict_player1[player1] == 3 and game_dict_player2[player2] == 2:
        return "Z"
    if game_dict_player1[player1] == 3 and game_dict_player2[player2] == 3:
        return "X"

def main():
    score = 0
    with open("adventofcode.com_2022_day_2_input.txt") as f:
        games = f.readlines()
        for game in games:
            if game != "\n":
                player1, player2 = game.strip().split()
                player2 = strategy(player1, player2)
                score = gamescore(score, player1, player2)
            else:
                print(score)
                score = 0
    
        print(score)
main()