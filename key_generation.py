import Crypto
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Util.number import *
import libnum

bits = 30

def keygenerate():
    p = Crypto.Util.number.getPrime(bits,randfunc = Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bits,randfunc= Crypto.Random.get_random_bytes)

    phi = (p-1)*(q-1)
    n = p*q

    e = 65537
    d = (libnum.invmod(e,phi))
    return ((e,n),(d,n))

f = open("auth_voters.txt", "w")

for i in range(6):
    ((e,n),(d,n)) = keygenerate()
    f.write(str(d) + " " + str(n)+ "\n")
f.close()
