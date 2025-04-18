import math
import secrets
import random

def generatePrimeNumber(bits, k=40):
    if bits < 2: raise ValueError("Minimum 2 bits")
    if bits == 2: return 3
    
    def isPrime(n):
        if n < 2: return False
        for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
            if n%p == 0: return n==p
        d,s = n-1,0
        while d%2 == 0: d,s = d//2,s+1
        for _ in range(k):
            a = secrets.randbelow(n-3)+2
            x = pow(a,d,n)
            if x in (1,n-1): continue
            for __ in range(s-1):
                x = pow(x,2,n)
                if x == n-1: break
            else: return False
        return True

    while True:
        p = secrets.randbits(bits)|(1<<bits-1)|1
        if p%2 !=0 and isPrime(p): return p

def generatePrimers(bitsNum):
    pBits = int(bitsNum / 2)
    qBits = int(bitsNum / 2)
    p = generatePrimeNumber(pBits)
    q = generatePrimeNumber(qBits)
    return p, q

def generateCryptoModule(p, q):   
    n = (p * q)
    return n

def generateEilerFunction(p, q):
    fn = (p - 1) * (q - 1)
    return fn

def generatePublicExponent(fn):
    publicExponent = random.randint(2, fn-1)
    while math.gcd(publicExponent, fn) != 1:
        publicExponent = random.randint(2, fn-1)
    return publicExponent

def generatePrivateExponent(publicExponent, fn):
    old_r, r = publicExponent, fn
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    if old_r != 1:
        raise ValueError("Error of private Exponent generating")
    return old_s % fn

def mainGeneration(bitsNum):
    primers = generatePrimers(bitsNum) #p - 0, q - 1
    n = generateCryptoModule(primers[0], primers[1])
    fn = generateEilerFunction(primers[0], primers[1])
    publicExponent = generatePublicExponent(fn)
    privateExponent = generatePrivateExponent(publicExponent, fn)

    return primers[0], primers[1], n, fn, publicExponent, privateExponent



print(mainGeneration(100))