#Clé D.H. de Bob : p=544563259, g=257605477, g^a =40139340
#Clé D.H. d'Alice : g^b = 32645465

a = 0
g = 257605477
p = 544563259
ga = 40139340
gb = 32645465
LIMITE = 20000

def fun(param):
    x = 1
    for a in range(LIMITE+1):
        #printf("\nPour a=%ld ;", a);
        x = (x*g) %p; 
        #printf("  x = %ld[%ld]\n", x, p);
        if (x==param):
            a = a+1
            return a
        
a = fun(ga)
gab = gb ** a % p
    
print(gab)
#Secret partagé : g^ab=469298015  