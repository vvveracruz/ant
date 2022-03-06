import pandas as _pd
import numpy as _np
import math as _math

def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 1
    while(count < n):
        num +=2 #optimization
        if is_prime(num):
            count +=1
    return num

def is_prime(num):
    # TODO: might be faster to use _math.gcd?
    factor = 2
    while (factor * factor <= num):
        if num % factor == 0:
             return False
        factor +=1
    return True

def chebyshev_theta_upto(n):
    '''
    Returns a pandas series with all the values of chebyshev's theta function
    up to n.

    TODO: change range steps to vary with size of n to stop it from loading 
    forever for big n.
    '''
    df=_pd.DataFrame(index=range(0, n, 1))
    df['is_prime']=df.index.map(lambda n: n if is_prime(n) else 0)
    df['log']=df.is_prime.map(lambda n: _np.log(n) if n!=0 else 0)
    df['chebyshev_theta']=df.log.cumsum()
    return df['chebyshev_theta']

def modulo_mult_table(n, returns_neg=False):
    df=_pd.DataFrame(index=range(0, n, 1))
    if returns_neg:
        R=range(0,-n, -1)
    else:
        R=range(0, n, 1)
    for i in R:
        df[str(i)]=df.index.map(lambda x: (x*i)%n)
    return df

def modulo_sum_table(n, returns_neg=False):
    df=_pd.DataFrame(index=range(0, n, 1))
    if returns_neg:
        R=range(0,-n, -1)
    else:
        R=range(0, n, 1)
    for i in R:
        df[str(i)]=df.index.map(lambda x: (x+i)%n)
    return df

def primes_less_than(n):
    # TODO: there's probably a better way to do this lol
    primes=[]
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)
    return primes

def coprimes_less_than(n):
    coprimes=[]
    for i in range(1, n):
        if _math.gcd(i, n)==1:
            coprimes.append(i)
    return coprimes