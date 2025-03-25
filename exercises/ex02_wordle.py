"""Wordle"""

__author__ = "730733853"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    n = 1
    turn = f"=== Turn {n}/6 ==="
    win = False
    while n <= 6 and not win:
        print(turn)
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {n}/6 turns")
            win = True
        n = n + 1
        turn = f"=== Turn {n}/6 ==="
    if not win:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, char: str) -> bool:
    """does the word contain this letter?"""
    assert len(char) == 1
    i = 0
    while i < len(word):
        if char == word[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """are the letters in the correct places?"""
    assert len(guess) == len(secret), """guess must be the same length as secret"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    word = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            word = word + GREEN_BOX
        elif contains_char(secret, guess[i]):
            word = word + YELLOW_BOX
        else:
            word = word + WHITE_BOX
        i += 1
    return word


def input_guess(n: int) -> str:
    """The player's guess should be n characters long"""
    guess = input(f"Enter a {n} character word")
    while len(guess) != n:
        guess = input(f"That wasn't {n} chars! Try again:")
    return guess


if __name__ == "__main__":
    main("codes")
