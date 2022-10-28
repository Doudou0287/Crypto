def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
 
#n = 4850522843
#print(prime_factors(n))

p =59021
q =82183
def PGCD(a,b):
    r=a%b
    if r==0 :
        return b
    else:
        return PGCD(b,r)

def estPremier(a,b):
    return PGCD(a,b)==1

def phi(m):
    if m == 1:
        return 1
    else:
        r = [n for n in range(1,m) if estPremier(m,n)]  
        return len(r)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

phiN = (p-1)*(q-1)
e = 1067
#print("phi(n) = phi(q)*phi(p) = (q-1)*(p-1) = ", phiN)
print("clé privée de Bob d = ", modinv(e,phiN))