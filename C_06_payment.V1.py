# Functions go here
def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses
    :rtype: object"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# Main routine goes here
payment_ans = ('cash', 'credit')

while True:
    pay_method = string_check("payment method: ", payment_ans, 2)
    print(f"You chose {pay_method}")

    break

# pay_method = string_check("Payment method: ", payment_ans, 2)
# print(f"You chose {pay_method}")