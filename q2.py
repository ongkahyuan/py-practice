import q1

class q2:

    def __init__(self):
        self.remove_num_palin_list = []
        self.pf = q1.prime_finder()

    def get_prime_list(self):
        return self.remove_num_palin_list

    def find_nums(self, lower_limit, upper_limit):
        for i in range(lower_limit, upper_limit):
            if self.remove_digit_primality(i):
                self.remove_num_palin_list.append(i)

    def slice_string(self, n, idx):
        s = str(n)
        if len(s) > idx:
            s = s[0:idx:] + s[idx + 1::]
        return int(s)
            
    def remove_digit_primality(self, n):
        for i in range(len(str(n))):
            to_test_primality = self.slice_string(n,i)
            if self.pf.is_prime(to_test_primality) and self.pf.is_palin(to_test_primality):
                return True
        return False

if __name__ == "__main__":
    quest2 = q2()
    quest2.find_nums(115,130)
    print(quest2.get_prime_list())