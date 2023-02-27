

def flat_generator(list_of_lists):
    counter = 0
    needed_list = []
    while counter < len(list_of_lists):
        needed_list += list_of_lists[counter]
        counter += 1
    for element in needed_list:
        yield element



