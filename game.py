import random
low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_run = True 

print("python number guessing game ")
print(f"select a number beteween {low_num , high_num}")

while is_run :
    get = input("Enter a random guess : ")

    if get.isdigit():
        get = int(get)
        guesses +=1
        
        if get < low_num or get > high_num :
            print("the number is out of range")
            print(f"Enter a number between{low_num} and {high_num}")
        elif get < answer :
            print("Too low  , Try again")
        elif get > answer :
            print("Too high, Try agian")

        else :
            print(f"Correct answer!, The answer is {answer}")
            print(f"The no of guesses is {guesses}")
            is_run = False

    else :
        print("Ivalid number")
        print(f"Enter a number beteween {low_num} and {high_num}")




 




