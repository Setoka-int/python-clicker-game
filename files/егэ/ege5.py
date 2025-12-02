for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 5 == 0:
        s = s + "11"
    else:
        s = s + bin(n // 5)[2:]
    r = int(s, 2)

    print(n, r)

