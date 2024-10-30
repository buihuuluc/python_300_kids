class CustomException(Exception):
    pass

def raise_custom_exception():
    try:
        raise CustomException("This is a custom exception!")
    except CustomException as e:
        print(e)

raise_custom_exception()