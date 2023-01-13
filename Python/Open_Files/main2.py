with open("wordlist.txt", "w") as f:
    base = "diablo"
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    for c in abeceda:
        for d in abeceda:
            f.write(c+d+base+"\n")
            f.write(c+base+d+"\n")
            f.write(base+c+d+"\n")