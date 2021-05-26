#! python3
# Little_Game.py - a little fun game! guess the next number of the series!

def Usage():
    print("""
Usage:
    #1
    Play(postion: int=6)

    ==> play the game!
    """)

import os
import random

class Series():
    def __init__(self, position: int):
        self.totalScore = 0
        self.guessNum = 0
        self.score = str(self.totalScore) + "/" + str(self.guessNum)
        self.f = self.Fibonacci(position+1)
        self.g = self.Geo(position+1)
        self.m = self.Alt(position+1)
        self.list = [self.f, self.g, self.m]

    def Record(self, right: bool):
        """record the score"""
        if right:
            self.totalScore += 1
        self.guessNum += 1
        self.score = str(self.totalScore) + "/" + str(self.guessNum)

    def Save(self, path: str = r".\score.txt"):
        """Save the score in a txt file"""

        with open(path, "w") as txt:
            txt.write(self.score)

    def Read(self, path: str = r".\score.txt"):
        """read score for last time"""

        if os.path.isfile(path):
            with open(path) as txt:
                text = txt.read()
                print("Your score last time was %s" %(text))

    def Guess(self):
        """Let player guess the next number of a random series"""

        self.Read()
        series = random.choice(self.list)
        self.list.remove(series)
        print(series[:-1])
        answer = int(input("The next number is: "))
        if answer == series[-1]:
            self.Record(True) # record the score
            if self.list:
                again = input("Yes!!! Another turn? (yes/no)")
                if again == "yes":
                    self.Guess()
                else:
                    print("Your score: %s" % (self.score))
                    self.Save()
            else:
                print("Your score: %s" % (self.score))
                self.Save()
                print("You win!")
            
            return 1

        else:
            self.Record(False) # record the score
            print("Your score: %s" % (self.score))
            self.Save()
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

    def Alt(self, position: int):
        """position: need to be an integer greater than 0, return first # numbers of the series"""

        if type(position) != int or position < 1:
            raise ValueError("position need to be an integer greater than 0")

        a = [-1]
        if position > 1:
            while len(a) < position:
                if a[-1] > 0:
                    new = (a[-1] + 7) * -1
                else:
                    new = (a[-1] - 7) * -1
                a.append(new)

        return a[:position]


def Play(postion: int=6):
    """play the game!"""

    series = Series(6)
    series.Guess()


if __name__ == "__main__":
    Play()