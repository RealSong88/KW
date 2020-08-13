def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(i * n)
        i += 1
    return result


def thr_fif_sum(n):
    i = 1
    sum = 0
    while i < n:
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        i += 1
    return sum


print(thr_fif_sum(1000))


def thr_fif_sum2(n):
    i = 1
    sum = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            sum += i

        i += 1
    return sum


print(thr_fif_sum2(1000))


def getTotalPage(m, n):
    if m % n == 0:
        return m / n
    else:
        return m // n + 1


print(getTotalPage(5, 10))
print(getTotalPage(17, 5))
