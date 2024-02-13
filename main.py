import sys
import json
from types import SimpleNamespace
from story.core import Statement, Game, Factors

def prompt() -> bool:
    while True:
        response = input("Do you [a]gree or [d]isagree ('q' to quit): ").lower()
        if response in ['a', 'y']:
            return True
        elif response in ['d', 'n']:
            return False
        elif response == 'q':
            return None
        else:
            print("Invalid input. Please type 'a' for agree, 'd' for disagree, or 'q' to quit.")
    
    return response

def display_factors(game: Game):
    factors = game.factors
    print(f"Players: {factors.players} | Fans: {factors.fans} | Mgmt: {factors.management} | Fins: {factors.finances}")

def main():
    print("Welcome to AdvFM demo")
    if len(sys.argv) != 2:
        print("Usage: python main.py <statements_001.json>")

    json_file_path = sys.argv[1]

    with open(json_file_path, 'r') as file:
        data: list[Statement] = json.load(file,  object_hook=lambda d: SimpleNamespace(**d))

    game = Game(10, 10, 10, 10)

    for statement in data:
        print(statement.statement)
        agree = prompt()

        if agree is not None:
            decision = statement.agree if agree else statement.disagree
            game.apply(decision)
            display_factors(game)
        else:
            print("Quitting...bye!")
            break

if __name__ == "__main__":
    main()