from multiprocessing import Pool

def items(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    return list(set_1.intersection(set_2))


if __name__ == '__main__':
    list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
    list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
    with Pool(5) as pool:
        result = [pool.apply(items, args=(list_a[i], list_b[i])) for i in range(len(list_a))]
        print(result)