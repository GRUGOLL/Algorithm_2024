def find_repeated_string(string):
    n = len(string)
    prefix = prefix_function(string)
    k = n - prefix[-1]
    if n % k == 0:
        return k
    return n

def prefix_function(string):
    result = [0] * len(string)
    result[0] = 0
    for i in range(len(string) - 1):
        j = result[i]
        while j > 0 and string[i + 1] != string[j]:
            j = result[j - 1]
        if string[i + 1] == string[j]:
            result[i + 1] = j + 1
        else:
            result[i + 1] = 0
    return result


def count_of_repeated_strings(string):
    len_of_repeated_string = find_repeated_string(string)
    return len(string) // len_of_repeated_string


if __name__ == "__main__":
    string = input()
    print(count_of_repeated_strings(string))