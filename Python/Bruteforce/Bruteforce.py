input("insert password: ")

def brute_force():
    for i in range(100):
        print(i)
        if i == 50:
            print("Password found!")
            break
        else:
            print("Password not found!")
            
brute_force()
   