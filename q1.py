import random

class prime_finder:
    def __init__(self):
        self.palin_prime_list = []

    def get_prime_list(self):
        return self.palin_prime_list

    def generate_palin_prime(self, lower_limit, upper_limit):
        for i in range(lower_limit, upper_limit):
            if self.is_prime(i):
                if self.is_palin(i):
                    self.palin_prime_list.append(i)

    def is_prime(self, n):
        if n <=3:
            return n>1
        if n % 2 == 0 or n%3 ==0:
            return False
        i = 5
        #6k+-1 primality test
        while i**2 <=n:
            if n % i == 0 or n % (i+2) ==0:
                return False
            i += 6
        return True

    def is_palin(self, n):
        num = str(n)
        return num == num[::-1]

if __name__ == "__main__":
    pf = prime_finder()
    pf.generate_palin_prime(0,100000)
    print(pf.get_prime_list())
