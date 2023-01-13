with open('test.txt', 'a') as f:
    f.write('\nnovy radek')

with open('test.txt', 'r') as f:
    print(f.read())