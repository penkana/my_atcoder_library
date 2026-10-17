# N以下の素数列挙


def generate_primes(number: int):
    primes = []
    cache = {}

    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        # 素数である
        primes.append(x)
        cache[x] = True
        # x の倍数はすべて素数ではないので、cacheのFalseとして処理
        for y in range(x * 2, number + 1, x):
            cache[y] = False

    return primes


def sieve_of_eratosthenes(n):  # エラトステネスのふるい
    candidate = list(range(2, n + 1))
    prime = []
    limit = n**0.5 + 1

    while True:
        p = candidate[0]
        if limit <= p:
            prime.extend(candidate)
            break
        prime.append(p)
        candidate = [i for i in candidate if i % p != 0]

        """
        i = 0
        while True:
            if i >= len(candidate):  # iはcandidateの長さ分
                break
            elif candidate[i] % p == 0:  # 余りがゼロなら
                candidate.pop(i)  # 素数ではないのでpop(取り除く)する
            i += 1
        """

    return prime
