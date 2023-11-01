import math
"""
    Returns if the integer is prime.

    Parameters
    ----------
    n : integer
 
    Returns
    -------
    Boolean
      True or False, if the number is prime.

    Examples
    --------
    >>> from prime_ar4609_1 import prime_ar4609_1
    >>> prime_ar4609_1.is_prime(5)
    True
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True