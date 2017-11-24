def combine_two_array(a, b):
    """
    combine two array into one array that items is unique
    do not have any side effect
    """
    unique_in_a = [e for e in a if e not in b]
    return b + unique_in_a


def main():
    a_ids = ["123456", "674827", "764897", "888888", "999999"]
    b_ids = ["123456", "674827", "764897", "000000", "666666"]
    results = combine_two_array(a_ids, b_ids)
    print(results)
    print(b_ids)

if __name__ == '__main__':
    main()