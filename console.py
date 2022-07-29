def gen_pass():
    import random
    # Generate a random password
    password = ''
    for i in range(0,8):
        password += chr(random.randint(33,126))
    print(password)

gen_pass()