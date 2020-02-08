import math
s = input()

def is_prime(n) :
    limit = int(math.sqrt(n)) + 1
    for i in range(2,limit + 1) :
        if n%i == 0 :
            return False
    return True

while s != "0.0" :
    n = float(s)
    last = len(s) - 2
    m = 0
    k = 1
    check = 0
    while m <= n*(10**last) :
        m = (n*(10**k))//1
        if is_prime(int(m)) :
            print("TRUE")
            check = 1
            break
        k += 1
    if check == 0 :
        print("FALSE")

    s = input()
        
    
