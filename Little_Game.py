#! python3
# Little_Game.py - a little fun game! guess the next number of the series!

import random

class Series():
    def __init__(self, position: int):
        self.f = self.Fibonacci(position+1)
        self.g = self.Geo(position+1)
        self.m = self.Max(position+1)
        self.list = [self.f, self.g, self.m]

    def Guess(self):
        """Let player guess the next number of a random series"""

        series = random.choice(self.list)
        self.list.remove(series)
        print(series[:-1])
        answer = int(input("The next number is: "))
        if answer == series[-1]:
            again = input("Yes!!! Another turn? (yes/no)")
            if again == "yes":
                if self.list:
                    self.Guess()
                else:
                    print("You win!")
            
            return 1

        else:
            print("Nooo! Game over.")
            return 0

    def Fibonacci(self, position: int):
        """position: need to be an integer greater than 0, return first # numbers of the series"""

        if type(position) != int or position < 1:
            raise ValueError("position need to be an integer greater than 0")

        f = [1,1]
        if position > 2:
            while len(f) < position:
                new = f[-1] + f[-2]
                f.append(new)

        return f[:position]

    def Geo(self, position: int):
        """position: need to be an integer greater than 0, return first # numbers of the series"""

        if type(position) != int or position < 1:
            raise ValueError("position need to be an integer greater than 0")

        g = [1]
        if position > 1:        
            while len(g) < position:
                new = g[-1] * 3 - 1
                g.append(new)

        return g[:position]

    def Max(self, position: int):
        """position: need to be an integer greater than 0, return first # numbers of the series"""

        if type(position) != int or position < 1:
            raise ValueError("position need to be an integer greater than 0")

        m = [-1, 1]
        if position > 2:
            while len(m) < position:
                new = max(m[-2]*-1, m[-1]*-2)
                m.append(new)

        return m[:position]


if __name__ == "__main__":
    series = Series(6)
    series.Guess()