def parse_welcome_message(input):
    decoded_input = input.decode('utf-8',"ignore")
    if decoded_input.__contains__('start_calculation'):
        return True,"start\n"
    return False,""

def check_finished(input):
    decoded_input = input.decode('utf-8', "ignore")
    if decoded_input.__contains__('END'):
        return True
    return False