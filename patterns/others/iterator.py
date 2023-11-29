def count_to(count):
    """Iterator implementation"""
    german_numbers = ["eins", "zwei", "drei", "vier", "funf"]

    # built in iterator creating tuples e.g (1, "eins")
    iterator = zip(range(count), german_numbers)

    # iterate through list
    for position, number in iterator:
        yield number


for num in count_to(4):
    print(num)
