z = 2 * 2048**512 + 4 * 512**1024 - 6 * 256**64 + 2 * 4096**128 - 8*16**24
v = 0
def bin24(n):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Используются цифры от 0 до 23
    result = ""
    while n > 0:
        remainder = n % 24
        result = digits[remainder] + result
        n //= 24
    return result
zv = (bin24(z))
print(zv.count("2"))