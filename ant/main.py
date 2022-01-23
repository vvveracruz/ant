import pandas as _pd
import numpy as _np

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