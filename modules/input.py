
def get_input_1(options):
    for option in options:
        option == input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    return option

def get_input_2(enter_text):
    for text in enter_text:
        text == input("Enter task description to search for: ")
    return text

def get_input_3(enter_int):
    for int_1 in enter_int:
        int_1 == int(input("Enter task duration: "))
    return int_1

def get_input_4(enter_text_2):
    for text in enter_text_2:
        text == input("Enter description: ")
    return text

def get_input_5(enter_int_2):
    for int_1 in enter_int_2:
        int_1 == int(input("Enter time taken: "))
    return int_1
