class q1:
    def __init__(self):
        """Solves question 1"""
        self.palin_prime_list = []

    def get_prime_list(self) -> list:
        """Returns the list of primes"""
        return self.palin_prime_list

    def generate_palin_prime(self, lower_limit:int, upper_limit:int) -> list:
        """Generates the list of primes"""
        for i in range(lower_limit, upper_limit):
            #Check if number is a prime
            if self.is_prime(i):
                #Check if number is a palindrome
                if self.is_palin(i):
                    self.palin_prime_list.append(i)

    def is_prime(self, n:int) -> bool:
        """Checks if number is a prime using the 6k+-1 primality test"""
        # Account for numbers <=3:
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

    def is_palin(self, n:int) ->bool:
        """Checks if number is a palindrome"""
        num = str(n)
        return num == num[::-1]

if __name__ == "__main__":
    quest = q1()
    quest.generate_palin_prime(0,100000)
    print(quest.get_prime_list())
