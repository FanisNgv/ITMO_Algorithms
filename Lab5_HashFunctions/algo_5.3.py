from sys import stdin

string_to_find = input()
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

pref_hash_string = get_pref_hash(string)
pref_hash_string_to_find = get_pref_hash(string_to_find)


def get_hash(L: int, R: int, pref_hash: list):
    return (pref_hash[R] - pref_hash[L] * p_powers[R - L]) % M

def find_substring(string, substring):

    m = len(substring)
    n = len(string)
    if(m > n):
        print(0)
        return
    occurence_index = []

    hash_sub = get_hash(0, m, pref_hash_string_to_find)

    for i in range(0, n - m + 1):
        hash_string = get_hash(i, i+m, pref_hash_string)
        if hash_sub == hash_string:
            occurence_index.append(i + 1)
        else:
            
            mismatches = 0
            for j in range(m):
                if string[i + j] != substring[j]:
                    mismatches += 1
                    if mismatches > 1:
                        break

            if mismatches == 1:
                occurence_index.append(i + 1)
                
    print(len(occurence_index))
    for index in occurence_index:
        print(index, end = ' ')


find_substring(string, string_to_find)