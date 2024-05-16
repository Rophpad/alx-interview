#!/usr/bin/python3
""" Prime Game
"""


class Player:
    """ Class of Prime Game's players
    """
    def __init__(self, score, status):
        self.score = score
        self.playing = status


def isWinner(x, nums):
    """  Return the winner for the Prime Game
    """
    if (not isinstance(x, int) or not isinstance(nums, list)):
        return None

    Maria = Player(0, False)
    Ben = Player(0, False)
    Round = 1
    while(Round <= x and Round <= len(nums)):
        n = nums[Round - 1]
        oneToN = list(range(1, n + 1))
        primeNums = list(
            filter(
                lambda x: x >= 2 and all(
                    x % div != 0 for div in range(2, int(x**0.5) + 1)
                ), oneToN
            )
        )

        if (len(primeNums) == 0):
            Ben.score += 1

        initiaLen = len(primeNums)
        while (len(primeNums) != 0):
            Maria.playing = True
            Ben.playing = False

            primeNums.pop(0)

            if (len(primeNums) == 0):
                if (initiaLen % 2 != 0):
                    Maria.playing = False
                    Ben.playing = True
                break

            Maria.playing = False
            Ben.playing = True
        # Out of previous while loop while
        # (cause next player can't play) is Maria tour
        if (Maria.playing):
            Ben.score = Ben.score + 1
        elif (Ben.playing):
            Maria.score = Maria.score + 1

        Maria.playing = False
        Ben.playing = False

        Round = Round + 1  # Next round
    return None if (Maria.score == Ben.score)\
        else "Maria" if (Maria.score > Ben.score) else "Ben"
