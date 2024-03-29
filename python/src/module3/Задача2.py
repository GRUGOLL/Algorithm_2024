def get_hash(string_t, lenght, x, p):
    hashik_of_string = 0
    for i in range(lenght):
        hashik_of_string = (hashik_of_string * x + ord(string_t[i])) % p
    return hashik_of_string

def minimum_cyclic_shift(string_t, string_s, x, p):
    hashik_of_string = get_hash(string_t, len(string_s), x, p)
    substring_hash = get_hash(string_s, len(string_s), x, p)
    sliding_hash = 1
    for i in range(len(string_s)):
        sliding_hash = (sliding_hash * x) % p


    for i in range(len(string_t) - len(string_s) + 1):
        if substring_hash == hashik_of_string:
            return i
        if i + len(string_s) < len(string_t):
            hashik_of_string = (hashik_of_string * x - ord(string_t[i]) * sliding_hash + ord(string_t[i + len(string_s)])) % p
            hashik_of_string = (hashik_of_string + p) % p
    return -1

if __name__ == "__main__":
    string_s = input()
    string_t = input()
    string_t = string_t * 2
    p = 10**9 + 7
    x = 31
    print(minimum_cyclic_shift(string_t, string_s, x, p))