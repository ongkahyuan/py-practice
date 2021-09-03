import q1, q2, q3, q4, q5
import pprint

def print_answer(answer, question, part=0, pretty = True):
    for i in range(2): print("")
    if part==0:
        print("Result for question "+ str(question) + ":")
    else: 
        print("Result for question "+ str(question) + " part " + str(part) +":")
    pp = pprint.PrettyPrinter(sort_dicts=False)
    if pretty:
        pp.pprint(answer)
    else:
        print(answer)

# Get inputs for question 2
print("\n \nInputs for question 2")
inputs = False
while not inputs:
    num1 = input("Enter a number between 1 and 100000:")
    num2 = input("Enter another number between 1 and 100000:")
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num1 >0 and num1 <100000 and num2 >0 and num2 <100000:
            inputs = True
        else:
            print("\n \nInvalid! ")
    except:
        print("\n \nInvalid! ")

# Get path of question 3 article
print("\n \nInputs for question 3")
inputs = False
while not inputs:
    path = input("Enter path of text article (leave blank to use sample):")
    if len(path) == 0: 
        path = "sample_article.txt"
        inputs = True
    try:
        f = open(path, "r", encoding="utf-8")
        f.close()
        inputs = True
    except:
        print("\n \nInvalid! ")
    
# Question 1
quest1 = q1.q1()
quest1.generate_palin_prime(0,100000)
print_answer(quest1.get_prime_list(), 1, pretty=False)

# Question 2
quest2 = q2.q2()
quest2.find_nums(min(num1, num2),max(num1, num2))
print_answer(quest2.get_prime_list(), 2, pretty=False)

# Question 3
quest3 = q3.q3(path)
print_answer(quest3.generate_dict(), 3)

# Question 4
quest4 = q4.q4()
print_answer(quest4.generate_sorted(), 4)

# Question 5
quest5 = q5.q5()
print_answer(quest5.part_one(), 5, part=1)
print_answer(quest5.part_two(), 5, part=2)
print_answer(quest5.part_three(), 5, part=3)
print_answer(quest5.part_four(), 5, part=4)
res = quest5.part_five()
str_res = "I'd sell " + str(res[0][1]) + " in " + str(res[0][0]) + " because it's the combination of state and product category that yields the highest monthly profit, at $" + str(res[1])
print_answer(str_res, 5, part=5, pretty=False)
print("\n \n")