import q1

class q2:

    def __init__(self):
        """Solves question 2. Requires two ints as input."""
        self.remove_num_palin_list = []
        self.pf = q1.q1() #reuse part 1 for primality check

    def get_prime_list(self) -> list:
        return self.remove_num_palin_list

    def find_nums(self, lower_limit:int, upper_limit:int):
        """Between the upper and lower limit, checks if number is a prime when any of its digits is removed, adds it to the list"""
        for i in range(lower_limit, upper_limit):
            if self.remove_digit_primality(i): #if the number passes the conditions
                self.remove_num_palin_list.append(i)

    def slice_string(self, n:int, idx:int) ->int:
        """Returns the int n with the digit at index idx removed"""
        s = str(n)
        #if the index is valid and not a single digit number
        if len(s) > idx and len(s)>1:
            s = s[0:idx:] + s[idx + 1::] #create the number from two slices
        return int(s)
            
    def remove_digit_primality(self, n):
        """Checks if number is a prime when any of its digits is removed"""
        for i in range(len(str(n))):

            #check every slice combination for primality
            to_test_primality = self.slice_string(n,i)
            if self.pf.is_prime(to_test_primality) and self.pf.is_palin(to_test_primality):
                return True
        return False

if __name__ == "__main__":
    quest2 = q2()
    quest2.find_nums(115,130)
    print(quest2.get_prime_list())