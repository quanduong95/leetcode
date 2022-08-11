
def guessNumber(n):
    bottom = 1
    top = n
    g = (top+bottom)//2

    while True:
        choice = guess(g)
        if choice == 0:
            return g
        elif choice == -1:
            top = g-1
            g = (top+bottom)//2

        else:
            bottom = g+1
            g = (top+bottom)//2
