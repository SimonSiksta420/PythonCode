def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()

input("Výpis tabulky násobení: " + str(multiplication_table()))
