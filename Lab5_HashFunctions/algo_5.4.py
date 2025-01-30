from sys import stdin

string = input()
M = 10**9 + 7
p = 256


p_powers = [1] * (len(string) + 1)
for i in range(1, len(string) + 1):
    p_powers[i] = (p_powers[i - 1] * p) % M

def get_pref_hash(string):
    pref_hash = [0] * (len(string) + 1)

    for i in range(1, len(string)+1):
        if i == 1:
            pref_hash[i] = ord(string[i-1])*pow(p, i - 1)
        else:
            pref_hash[i] = (pref_hash[i - 1]*p + ord(string[i-1])*pow(p, 0)) % M

    return pref_hash

def get_pref_hash_reversed(string):
    pref_hash = [0] * (len(string) + 1)

    for i in range(len(string), 0, -1):
        if i == len(string):
            pref_hash[len(string) - i + 1] = ord(string[i-1])*pow(p, len(string) - i)
        else:
            pref_hash[len(string) - i + 1] = (pref_hash[len(string) - i]*p + ord(string[i-1])*pow(p, 0)) % M

    return pref_hash

pref_hash_string = get_pref_hash(string)
pref_hash_string_reversed = get_pref_hash_reversed(string)
# print(pref_hash_string)



def get_hash(L: int, R: int, pref_hash: list):
    return (pref_hash[R] - pref_hash[L] * p_powers[R - L]) % M

def find_palindromes(string):
    n = len(string)
    count_of_palindromes = 0

    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            # print(pref_hash_string_reversed[j:j+i+1])
            # print()
            # print(pref_hash_string[n-j-i+1:n-j+2])
            # print()
            r_hash = get_hash(j-1, j+i-1, pref_hash_string_reversed)
            s_hash = get_hash(n-j-i, n-j, pref_hash_string)
            # ноль индексация включая правую границу
            if r_hash == s_hash:
                count_of_palindromes +=1
            # print(j-1, j+i-1)
            # print(n-j-i, n-j)
            # print(r_hash, s_hash)
    print(count_of_palindromes)

find_palindromes(string)