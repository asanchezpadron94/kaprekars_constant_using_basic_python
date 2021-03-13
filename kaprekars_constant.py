
def find_6174():

    number_to_find = int(input('Insert any number from 1001 to 9998: '))
    print('')

    # Check if the number inserted by the user is valid.
    while number_to_find < 1001 or number_to_find > 9998:

        print('Please enter a valid number.')
        number_to_find = 0
        break
    if number_to_find == 0:

        find_6174()

    # Identify and show how many steps are needed to find the Kaprekar's constant.
    if number_to_find >= 1001 and number_to_find <= 9998:

        calculate_6174(number_to_find)

def calculate_6174(number_to_find):


    # Convert the number to find into a list with 4 values.
    str_number_to_find = str(number_to_find)
    map_str_number_to_find = map(int, str_number_to_find)
    list_map_str_number_to_find = list(map_str_number_to_find)
    
    # Copy the list and sort one in ascending and the other in descending.
    biggest_possible_outcome = list_map_str_number_to_find.copy()
    smalest_possible_outcome = list_map_str_number_to_find.copy()
    
    biggest_possible_outcome.sort(reverse = True)
    int_biggest_possible_outcome = int("".join([str(biggest_possible_outcome) for biggest_possible_outcome in biggest_possible_outcome]))

    smalest_possible_outcome.sort()
    int_smalest_possible_outcome = int("".join([str(smalest_possible_outcome) for smalest_possible_outcome in smalest_possible_outcome]))
    
    # Calculate next posible combination until it gets 6174:
    next_number_to_find = int_biggest_possible_outcome - int_smalest_possible_outcome
    print(f'{number_to_find} = {int_biggest_possible_outcome} - {int_smalest_possible_outcome} = {next_number_to_find}')
    
    # Check if next_number_to_find is already 6174:
    if next_number_to_find != 6174:

        calculate_6174(next_number_to_find)

    else:

        print("\n ¡You got it! \n")


if __name__ == '__main__':

    find_6174()