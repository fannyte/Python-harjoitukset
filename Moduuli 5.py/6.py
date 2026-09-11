import random
N = int(input("Anna arvottavien pisteiden määrä: "))
i = 0
n = 0
while i < N:
    i = i + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    pi = 4 * n / N
    # print(f"Arvottujen pisteiden määrä: {pisteiden_määrä}")
    # print(f"Ympyrän sisälle osuneiden pisteiden määrä: {n}")