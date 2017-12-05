def handle_mutil_exception():
    """
    handle mutil exception at once
    use .__mro__ to view the hierachy of a particular exception
    """
    file_name = "resdafadme.md"
    try:
        f = open(file_name)
    except (FileNotFoundError, PermissionError):
        print("file not found or no permission to acess it")


def catch_all_exception():
    """
    catch all exception
    """
    n = 'a'
    try:
        n = int(n)
    except Exception as e:
        print("can not conver n to int")
        print("reason:", e)


class CustomError(Exception):
    """
    define custom error
    """
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status


def use_custom_error():
    """
    try custom error defined above
    """
    try:
        raise CustomError('error', 22)
    except CustomError as e:
        print(e.args)


def raise_muti_exception():
    """
    raise exception in response to another exception
    """
    try:
        int('n/a')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e


def handle_final_error():
    """
    handle final error in mutil exception
    """
    try:
        raise_muti_exception()
    except RuntimeError as e:
        print("handle final error")


def reraising_last_exception():
    """
    reraising last exception
    """
    try:
        int('n/a')
    except ValueError:
        print('did not work')
        raise

def main():
    handle_mutil_exception()
    catch_all_exception()
    use_custom_error()
    handle_final_error()
    reraising_last_exception()
    pass

if __name__ == '__main__':
    main()