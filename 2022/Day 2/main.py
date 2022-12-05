
possible_plays = [
    {'name': 'rock',
     'letter': 'A',
     'points': 1,
     'wins': 'C'
     },
    {'name': 'paper',
     'letter': 'B',
     'points': 2,
     'wins': 'A'
     },
    {'name': 'scissors',
     'letter': 'C',
     'points': 3,
     'wins': 'B'
     },
]

win = 6
draw = 3
loss = 0


def main():
    follow_strategy()


def follow_strategy():
    input_file = open('input.txt', 'r')
    total_points = 0
    for line in input_file:
        line = line.replace("\n", "")
        total_points += result(line.split(' '))

    print(f"Following the strategy it results in {total_points} points")


def strategy_encryption() -> list:
    return {'A': 'X', 'B': 'Y', 'C': 'Z'}


def result(play):
    play_1_translated = get_play_from_possible_plays(play[0])
    ## Removed after day one. To run day one uncomment the line below and comment the next
    #play_2_decoded = strategy_decrypt(play[1])
    play_2_decoded = get_updated_strategy(play[1], play_1_translated)
    play_2_translated = get_play_from_possible_plays(play_2_decoded)

    if play[0] == play_2_decoded:
        return draw + play_2_translated['points']

    if play_2_decoded.upper() == play_1_translated['wins']:
        return loss + play_2_translated['points']

    if play_1_translated['letter'].upper() == play_2_translated['wins']:
        return win + play_2_translated['points']


def strategy_decrypt(play: str) -> str:
    strategy = strategy_encryption()
    for p in strategy:
        if strategy[p.upper()] == play.upper():
            return p
    raise Exception(f"The play {play} cannot be decrypted.")


def get_updated_strategy(play: str, play_from_1: dict) -> str:
    match play.upper():
        case "X":
            for p in possible_plays:
                if p['letter'].upper() == play_from_1['wins'].upper():
                    return p['letter'].upper()
        case "Y":
            return play_from_1['letter'].upper()
        case "Z":
            for p in possible_plays:
                if p['letter'].upper() != play_from_1['letter'].upper() and p['letter'].upper() != play_from_1['wins'].upper():
                    return p['letter'].upper()



def get_play_from_possible_plays(play: str) -> dict:
    for p in possible_plays:
        if p['letter'].upper() == play.upper():
            return p

    raise Exception(f"Play {play} does not exist in the possible plays.")


if __name__ == "__main__":
    main()
