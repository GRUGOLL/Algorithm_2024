def merge_sort(lst, start, end):
    if end - start <= 1 :
        return lst[start:end]

    middle = (start + end) // 2
    left = merge_sort(lst, start, middle)
    right = merge_sort(lst, middle, end)

    merged_lst = merge(left, right)
    print(f"{start + 1} {end} {merged_lst[0]} {merged_lst[-1]}")
    return merged_lst

def merge(left, right):
    i = 0
    j = 0
    sorted = [0] * (len(left) + len(right))
    for k in range(len(sorted)):
        if i == len(left):
            sorted[k] = right[j]
            j += 1
        elif j == len(right):
            sorted[k] = left[i]
            i += 1
        elif left[i] <= right[j]:
            sorted[k] = left[i]
            i += 1
        else:
            sorted[k] = right[j]
            j += 1
    return sorted

if __name__ == "__main__":
    a = int(input())
    if a == 1:
        lst = int(input())
        print(lst)
    else:
        lst = list(map(int, input().split()))
        sorted_lst = merge_sort(lst, 0, a)
        print(" ".join(map(str, sorted_lst)))