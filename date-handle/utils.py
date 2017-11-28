import datetime

def time_in_range(start, end, date):
    """ return true if date is in the range [start, end] """
    if start <= end:
        return start <= date <= end
    else:
        return start <= date or date <= end

def create_time(hours, mins, second):
    """
    create time in hours:min:second
    """
    return datetime.time(hours, mins, second)


def main():
    start = create_time(13, 0, 0)
    end = create_time(23, 0, 0)
    time_to_check = create_time(10, 0, 0)

    print(time_in_range(start, end, time_to_check))
    pass

if __name__ == '__main__':
    main()