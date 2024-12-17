import math

class game:

    def __init__(self):
        print("welcome to the guessing game!!")
        print("guess a number in between 0 to 50...")
        self.correct_number = 6

    def user_number_check(self):
        self.user_number = int(input("guess a number: "))
        if self.user_number < 0 or self.user_number > 50:
            print("number out of range... please try again!")
            number.user_number_check()
    
    def is_user_number_prime(self):
        if self.user_number == 2:
            return True
        if self.user_number <= 1 or self.user_number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(self.user_number))+1, 2):
            if self.user_number % i == 0:
                return False
        return True
    
    def is_user_number_correct(self):
        if self.user_number == self.correct_number:
            if self.is_user_number_prime():
                print("correct and prime")
            else:
                print("correct but not prime")
        else:
            if self.is_user_number_prime():
                print("incorrect but prime")
            else:
                print("incorrect and not prime")
        



number = game()
number.user_number_check()
number.is_user_number_prime()
number.is_user_number_correct()

