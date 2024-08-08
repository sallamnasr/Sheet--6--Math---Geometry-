


if __name__ == "__main__" :
    l,r,x = map(int,input().split())
    res = 1 
    for i in range(l,r+1) :
        res *= i
    print(res%x)