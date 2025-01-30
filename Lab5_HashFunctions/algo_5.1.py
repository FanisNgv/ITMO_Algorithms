from sys import stdin

string = input()
n = int(input())

M = 10**9 + 7
p = 256

p_powers = [1] * (len(string) + 1)
for i in range(1, len(string) + 1):
    p_powers[i] = (p_powers[i - 1] * p) % M

pref_hash = [0] * (len(string) + 1)

for i in range(1, len(string)+1):
    if i == 1:
        pref_hash[i] = ord(string[i-1])*pow(p, i - 1)
    else:
        pref_hash[i] = (pref_hash[i - 1]*p + ord(string[i-1])*pow(p, 0)) % M

def get_hash(L: int, R: int):
    return (pref_hash[R] - pref_hash[L] * p_powers[R - L]) % M



for input_data in stdin:
    input_data = input_data.split()
    if (get_hash(int(input_data[0])-1, int(input_data[1])) == get_hash(int(input_data[2]) - 1, int(input_data[3]))):
        print('Yes')
    else:
        print('No')