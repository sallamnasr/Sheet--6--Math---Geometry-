
if __name__ == "__main__":
    t = 1
    # t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(61):
            arr.append(2**i)
        if n in arr:
            print("YES")
        else:
            print("NO")
