def max_in_slicing_with_k_element(num_lst: list, k: int):
    lst_length = len(num_lst)
    result = []
    for i in range(lst_length - k + 1):
        result.append(max(num_lst[i:i + k]))
    return result


if __name__ == '__main__':
    num_lst = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    print(max_in_slicing_with_k_element(num_lst, 3))
