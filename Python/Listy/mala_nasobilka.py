multiplication_table = []
for i in range(1, 11):
    multiplication_table.append([])
    for j in range(1, 11):
        multiplication_table[i - 1].append(i * j)
        
print(multiplication_table)