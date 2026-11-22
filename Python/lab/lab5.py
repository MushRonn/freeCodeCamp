# Debugging an ISBN Validator


def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # The check digit is the final character; the preceding characters are
    # the main digits used to calculate the expected check digit.
    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    # Multiply each of the first 9 digits by its corresponding weight
    # (10 to 2) and sum the results.
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Multiply the first 12 digits by 1 and 3 alternately, then calculate
    # the check digit from the sum.
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')

    try:
        isbn = values[0]
        length_text = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return

    try:
        length = int(length_text)
    except ValueError:
        print('Length must be a number.')
        return

    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)


# Keep this call commented out so freeCodeCamp can run its tests.
# main()
