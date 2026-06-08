def is_answer(x: int) -> bool:
    """
    Function that gives the answer.

    x (int): number you want to check
    """
    if x == 42:
        ans = ""
    else:
        ans = " not"
    msg = f"{x} is{ans} the answer to the question of life, universe, and everything"
    print(msg)

def hello_world():
    """
    Simple hello world print
    """
    print("Hello world")
