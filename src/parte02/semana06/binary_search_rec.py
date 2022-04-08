def binary_search_recursive(lst, elem, start=0, end=None):
    if end is None:
        end = len(lst) - 1

    if start > end:
        return False

    mid = (start + end) // 2

    if elem == lst[mid]:
        return mid
    if elem < lst[mid]:
        return binary_search_recursive(lst, elem, start, mid - 1)
    # elem > lst[mid]
    return binary_search_recursive(lst, elem, mid + 1, end)


if __name__ == "__main__":
    a = [17, 20, 26, 31, 44, 54, 55, 77, 93]

    print(binary_search_recursive(a, 55))
