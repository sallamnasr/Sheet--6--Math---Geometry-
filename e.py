

if __name__ == "__main__":
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        x = (-1 + (1+8*n)**0.5)/2
        y = (-1 - (1+8*n)**0.5)/2
        if x > 0:
            print(int(x))
        else:
            print(int(y))
