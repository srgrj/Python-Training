import emoji
import sys


def create():
    # D = input().split()
    N = 33
    # int(D[0])
    M = 99
    # int(D[1])
    pattern1 = emoji.emojize(':sparkling_heart:')
    pattern2 = emoji.emojize(':heavy_minus_sign:')
    odds = [x for x in range(1, N) if x % 2 != 0]
    top(N, M, pattern1, pattern2, odds)
    middle(M, pattern2)
    bottom(N, M, pattern1, pattern2, odds)


def top(N, M, pattern1, pattern2, odds):
    for i in (range(0, (N - 1) // 2)):
        print((pattern1 * odds[i]).center(M, pattern2))


def middle(M, pattern2):
    centerText = " SOMESH " + emoji.emojize(':kiss:') + " SHRUTI "
    print(centerText.center(M+6, pattern2))


def bottom(N, M, pattern1, pattern2, odds):
    oddsRev = odds[::-1]
    for i in range(0, (N - 1) // 2):
        print((pattern1 * oddsRev[i]).center(M, pattern2))


create()


"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖💖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖💖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖💖💖💖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖SOMESH 💏 SHRUTI➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖💖💖💖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖💖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖💖💖💖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖💖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

"""