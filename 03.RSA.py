def gcd(m,n):
    if n==0:
        return m;
    else:
        return gcd(n,m%n);

p = 79
q = 89
e=2
d=2

#calculate n
n = p*q 

#calculate totient
totient = (p-1)*(q-1) 

#finding the value of k
for e in range(2,totient): 
    if gcd(e,totient)== 1: 
        break

#finding the value of d
#de mod Φ(n) = 1
while (d*e)%totient != 1:
    d+=1;

message = "It is a secret";
encrypted_message = ""
for c in message:
    encrypted_message += chr(pow(ord(c),e)  % n);


decrypted_message = ""
for c in encrypted_message:
    decrypted_message += chr(pow(ord(c),d) % n)
