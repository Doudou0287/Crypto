blocks = "474055773,303755870,223921789,468397959,345933175,346247998,145314099,290987117,65720302,34074289,1103544,425784355,308647921,80807828,33803669,299883420,181882989,448511457,294079167,242890823,308647921,213631765,118271084,533755237,170641126"

gab=469298015
p = 544563259
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
        
blocks = blocks.split(",")
print(blocks)

c = modinv(469298015,544563259)  
p = 544563259  
def my_function(param):
    v = int(param)
    v = (v * c) % p
    return v 
  
  
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
   
def sep(par):
    a_string = dec_to_bin(par)
    n = 8
    split_strings = [a_string[index : index + n] for index in range(0, len(a_string), n)]
    return split_strings

def binaryToDecimal(n):
	num = n
	dec_value = 0
	base = 1
	temp = num
	while(temp):
		last_digit = temp % 10
		temp = int(temp / 10)
		dec_value += last_digit * base;
		base = base * 2
	return dec_value;    
	
def chg(para):
    thislist = sep(para)
    for x in thislist:
        y = int(x)
        z = binaryToDecimal(y)
        print(z) 
        
def chk(param):
    mylist = param
    for i in mylist :
        #print(i)
        x = binaryToDecimal(int(i))
        #print(x)
        print(chr(x), end = '')
        
        #return i
    
for i in blocks :
    #print()
    #print(i, "the original number")
    new = my_function(i)
    #print(dec_to_bin(new))
    #print(sep(new))
    chk(sep(new))
    #print(chr(lets))
    #l = sep(int(dec_to_bin(new)))
    
    #chg(i)
    print()
    


