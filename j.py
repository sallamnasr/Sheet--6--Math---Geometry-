def isprime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def factors(num):
    arr = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            arr.append(i)
            if i != num // i:
                arr.append(num // i)
        i += 1
    return arr


def PrimeFactors(num):
    arr = []
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            num //= i
            arr.append(i)
    if num != 1:
        arr.append(num)
    return arr


if __name__ == "__main__":
    n = int(input())
    Pfactors = PrimeFactors(n)
    Ffactors = []
    for i in Pfactors:
        Ffactors.append(Pfactors.count(i))
    uniqe = []
    for i in Pfactors:
        if i not in uniqe:
            uniqe.append(i)
    res = ""
    for i in uniqe:
        res += f"({i}^{Pfactors.count(i)})*"
    print(res[0:len(res)-1])
