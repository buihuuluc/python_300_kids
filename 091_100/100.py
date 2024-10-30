def throw_error():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise e
    except TypeError as e:
        raise e
    
def log_error():
    try:
        throw_error()
    except Exception as e:
        with open('error.txt', 'a') as f:
            f.write(str(e) + '\n')
