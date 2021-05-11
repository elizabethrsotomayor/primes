from typing import List


def factors(value: int) -> List[int]:
    """Compute the prime factors of a given natural number."""
    primes = []
    factor = 2

    while value > 1:
        if value % factor == 0:
            primes.append(factor)
            value /= factor
        else:
            if factor > 2:
                factor += 2
            else:
                factor += 1

    return primes
