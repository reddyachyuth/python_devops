def my_random_generator(iterable):
    import random
    indices_returned_so_far = set()
    while len(indices_returned_so_far) < len(iterable):
        rand = random.randint(0, len(iterable) - 1)
        while rand in indices_returned_so_far:
            rand = random.randint(0, len(iterable) - 1)

        indices_returned_so_far.add(rand)
        yield iterable[rand]
