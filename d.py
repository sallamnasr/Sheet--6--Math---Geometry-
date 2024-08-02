if __name__ == "__main__":

    # t = int(input())
    t = 1

    for _ in range(t):
        a, b, q = map(int, input().split())
        x = a ^ b
        if q % 3 == 0:
            print(x)
        elif q % 3 == 1:
            print(a)
        else:
            print(b)
