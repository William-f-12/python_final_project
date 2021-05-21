#! python3
# Little_Game.py - a little fun game!

class Series():
    def __init__(self):
        self.list = []

    def Fibonacci(self, position: int):
        """position: need to be an integer greater than 0, return first # numbers of the series"""

        if type(position) != int or position < 1:
            try:
                raise ValueError("position need to be an integer greater than 0")
            except Exception as e:
                print(e)
                return 0

        f = [1,1]
        if position < 3:
            return f[:position]

        while len(f) < position:
            new = f[-1] + f[-2]
            f.append(new)
        return f[:position]
