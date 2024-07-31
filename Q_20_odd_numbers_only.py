'''
 Write python program that user to enter only odd numbers, else will
raise an exception.
'''
class EvenNumberError(Exception):
    pass
def get_odd_number():
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise EvenNumberError(f"{number} is not an odd number!")
        return number
    except EvenNumberError as e:
        print(e)
        return get_odd_number()
    except ValueError:
        print("That's not a valid number! Please enter a number.")
        return get_odd_number() 

odd_number = get_odd_number()
print(f"Thank you! You entered the odd number: {odd_number}")