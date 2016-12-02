"""

>>> check_number(8, 7, 100, 1)
True

>>> check_number(95, 95, 100, 1)
False

"""

upper_bound = 100
lower_bound = 1

def generate_user_number(upper_bound, lower_bound):
    """
    input: upper and lower bound as integers
    usage: ask user for number between bounds and confirm w/ if statement
    output: user's number as integer
    """
    user_number = int(input("Hi! Choose a number between 1 and 100! >> "))
    if user_number < lower_bound or user_number > upper_bound:
        user_number = int(input("Your number is outside the parameters. Please choose a different number. >> "))
    return user_number

def computer_guess(upper_bound, lower_bound, guess_count):
    """
    input: upper and lower bounds as integers
    usage: generate computer guess, starting at 1 and incrementing by 1
    output: computer's guess as integer, increments guess_count by 1
    """
    comp_number = guess_count + 1
    higher_or_lower = input("The computer guessed {}, is that higher (H) or lower (L)? > ".format(comp_number))
    return comp_number

def check_number(user_number, comp_number, upper_bound, lower_bound):
    """
    input: user_number, comp_number, upper and lower bounds as integers
    usage: compares user_number to comp_number and changes one boundary
    output: False if numbers match, True otherwise
    """
    if user_number == comp_number:
        return False
    else:
        if comp_number > user_number:
            upper_bound = comp_number - 1
        elif comp_number < user_number:
            lower_bound = comp_number + 1
        return True

def main(upper_bound, lower_bound):
    """
    input: upper and lower bounds
    usage: calls all functions necessary to execute guessing game
    output: print statement describing how many guesses the comp needed
    """
    guess_count = 0
    user_number = generate_user_number(upper_bound, lower_bound)
    comp_number = computer_guess(upper_bound, lower_bound, guess_count)
    while check_number(user_number, comp_number, upper_bound, lower_bound):
        comp_number = computer_guess(upper_bound, lower_bound, guess_count)
        guess_count += 1
    print("It took the computer {} guesses to find {}.".format(guess_count, user_number))

main(upper_bound, lower_bound)
