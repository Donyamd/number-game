import sys
import argparse
from random import randrange
parser = argparse.ArgumentParser(description="It's a number game!")
parser.add_argument('--start', '-s', type=int, default=0)
parser.add_argument('--end', '-e', type=int, default=10)
parser.add_argument('--rounds', '-r', type=int, default=3)

def take_a_guess(idx):
    try:
        guess = int(input(f"{idx}> GUESS THE NUMBER: "))
    except ValueError:
        return take_a_guess(idx)
    return guess

def single_player(range_start=0, range_end=10, rounds=3):
    random_number = randrange(range_start, range_end)
    won = False
    for idx, round in enumerate(range(rounds), start=1):
        guess = take_a_guess(idx)

        if guess < random_number:
            print("YOUR GUESS IS LESS THAN THE TARGET")

        elif guess > random_number:
            print("YOUR GUESS IS MORE THAN THE TARGET")
    
        else:
            won = True
            break

    print(f"--> ACTUAL NUMBER WAS: {random_number}" + " <--")
    return won

def main():
    args = parser.parse_args()
    if args.start >= args.end:
        print("THE VALUE FOR START SHOULD BE LESS THAN THE END!")
        sys.exit(1)

    if args.rounds <0:
        print("THE ROUNDS CAN'T BE NEGETIVE")
        sys.exit(1)
    won = single_player(args.start, args.end, args.rounds)
    if won:
        print("*** YOU WON! ***") 
    else:
        print("YOU LOST! :(")
        
main()