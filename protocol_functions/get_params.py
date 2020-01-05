def get_params(input):
    decoded_input = input.decode().rstrip()
    return decoded_input.split(',')
