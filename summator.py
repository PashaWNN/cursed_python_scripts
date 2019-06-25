#!/usr/bin/python3

sum = 0

class Summator:

    def __init__(self, a):
        global sum
        sum += a

    def __call__(self, a):
        global sum
        sum += a
        return self

    def __repr__(self):
        global sum
        return str(sum)

    def __str__(self):
        global sum
        return str(sum)


if __name__ == '__main__':
    print(Summator(1)(2)(3)(-10))
