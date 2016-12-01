guess_count = 0
upper_bound = 100
lower_bound = 1

def generate_user_number(upper_bound, lower_bound):
    """
    input: upper and lower bound as integers
    usage: ask user for number between bounds and confirm w/ if statement
    output: user's number as integer
    """


def computer_guess(upper_bound, lower_bound):
    """
    input: upper and lower bounds as integers
    usage: generate computer guess, starting at 1 and incrementing by 1
    output: computer's guess as integer, increments guess_count by 1
    """


def check_number(user_number, comp_number, upper_bound, lower_bound):
    """
    input: user_number, comp_number, upper and lower bounds as integers
    usage: compares user_number to comp_number and changes one boundary
    output: True if numbers match, false otherwise
    """
    if user_number == comp_number:
        return True
    else:
        if comp_number > user_number:
            upper_bound = comp_number
        elif comp_number < user_number:
            lower_bound = comp_number
        return False

def main(upper_bound, lower_bound):
    """
    input: upper and lower bounds
    usage: calls all functions necessary to execute guessing game
    output: print statement describing how many guesses the comp needed
    """
    generate_user_number(upper_bound, lower_bound)
    computer_guess(upper_bound, lower_bound)
    while check_number(user_number, comp_number, upper_bound, lower_bound):
        computer_guess(upper_bound, lower_bound)
    print("It took the computer {} guesses to find {}.".format(guess_count, user_number))

main(upper_bound, lower_bound)
