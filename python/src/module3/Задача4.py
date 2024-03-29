def functin_z(string):
    Z = [0] * len(string)
    left = 0
    right = 0
    max_indx = 0
    for i in range(1, len(string)):
        if i <= right:
            Z[i] = min(right - i + 1, Z[i - left])
        while i + Z[i] < len(string) and string[Z[i]] == string[Z[i] + i]:
            Z[i] += 1

        if Z[i] > Z[max_indx]:
            max_indx = i

        if i + Z[i] - 1 > right:
            left = i
            right = i + Z[i] - 1

    return Z, max_indx


def min_len_length(string):
    z, max_indx = functin_z(string)
    if max_indx + z[max_indx] == len(string):
        return len(string) - z[max_indx]
    else:
        k = 0
        for i in range(len(string) - 1, -1, -1):
            if z[i] > k and z[i] < z[max_indx] and i + z[i] == len(string):
                k = z[i]             

        return len(string) - k


if __name__ == "__main__":
    string = input()

    print(min_len_length(string))