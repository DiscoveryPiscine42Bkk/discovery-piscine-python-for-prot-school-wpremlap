num = 0


while num <= 10:
    i = 0
    print(f"Table de {num}: ", end="")


    while i <= 10:
        print(num * i, end= " " if i < 10 else "\n")
        i += 1

        num += 1