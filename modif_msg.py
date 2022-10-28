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
    
print("g^ab = ",gab)
#Secret partagé : g^ab=469298015 
def dec_to_bin(n):
    x=n
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    #print(len(string))
    if len(string) < 24:
        str1="0"
        string=str1+string

    return string
    

def fun1(string):
    liste = []
    for x in string:
        car = ord(x)
        if (len(dec_to_bin(car)) == 9):
            liste.append(dec_to_bin(car)[1:])
        else:
            liste.append(dec_to_bin(car))
        #print(liste)
    my_lst_str = ''.join(liste)
    return my_lst_str


line = 'Rendez-vous a 17h15 au point de latitude Nord 48.7000, longitude Est 7.7800'
def fun2(param):
    n = 3
    liste = []
    param = [line[i:i+n] for i in range(0, len(line), n)]
    print(param)
    for x in param:
        y = fun1(x)
        liste.append(y)
    return liste

def fun3(x):
    y = x*gab
    z = y%p 
    print(z)
    
#print(fun2(line))

print("the_hour_changement_6h1 = ",fun1('6h1'))
the_hour_changement_6h1 = 0b001101100110100000110001
fun3(the_hour_changement_6h1)

print("remplacer_58 = ",fun1('.58'))
remplacer_58 = 0b001011100011010100111000
fun3(remplacer_58)

print("remplacer_15 = ",fun1('15,'))
remplacer_58 = 0b001100010011010100101100
fun3(remplacer_58)

print("remplacer_503 = ",fun1('503'))
remplacer_58 = 0b001101010011000000110011
fun3(remplacer_58)