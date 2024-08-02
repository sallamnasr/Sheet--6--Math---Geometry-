
if __name__ == "__main__":
    n, x, h, m, s = map(int, input().split())
    total_second = s + m*60 + h*3600
    total_sand = x * total_second
    print(n-total_sand)
