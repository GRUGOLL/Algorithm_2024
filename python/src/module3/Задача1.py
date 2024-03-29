def get_hash(string, lenght, x, p):
    string_hash = 0
    for i in range(lenght):
        string_hash = (string_hash * x + ord(string[i])) % p
    return string_hash

def Rabin_Karp(string, substring, x, p):
    string_hash = get_hash(string, len(substring), x, p)
    substring_hash = get_hash(substring, len(substring), x, p)
    sliding_hash = 1
    for i in range(len(substring)):
        sliding_hash = (sliding_hash * x) % p

    list_of_index = []

    for i in range(len(string) - len(substring) + 1):
        if substring_hash == string_hash:
            list_of_index.append(i)
        if i + len(substring) < len(string):
            string_hash = (string_hash * x - ord(string[i]) * sliding_hash + ord(string[i + len(substring)])) % p
            string_hash = (string_hash + p) % p
    return list_of_index

if __name__ == "__main__":
    string = input()
    substring = input()
    p = 10**9 + 7
    x = 31
    result = Rabin_Karp(string, substring, x, p)
    print(*result)