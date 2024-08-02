def isprime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":

    # t = int(input())
    t = 1

    for _ in range(t):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a

        # Calculate total sum
        cnt_of_NUM = b - a + 1
        if cnt_of_NUM % 2 == 0:
            total_sum = (a + b) * (cnt_of_NUM // 2)
        else:
            total_sum = (a + b) * (cnt_of_NUM // 2) + (a + b) // 2

        print(total_sum)

        # Calculate even sum
        import math
        i = math.ceil(a / 2)
        j = b // 2
        even_start = 2 * i
        even_end = 2 * j

        if i > j:
            even_sum = 0
        else:
            cnt_of_even_NUM = (even_end - even_start) // 2 + 1
            even_sum = (even_start + even_end) * cnt_of_even_NUM // 2

        print(even_sum)

        # Calculate odd sum
        odd_sum = total_sum - even_sum

        print(odd_sum)
