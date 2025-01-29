'''
На вход поступают две функции f(x) и g(x). Нужно проверить следующие условия:

1) f(x) = O(g(x))
2) f(x) = Omega(g(x))
3) f(x) = Tetta(g(x))

Затем нужно вывести три строки по типу:
YES
YES
NO

Есть три случая:
1) Константа и константа - везде будет YES, степень икса 0
2) Константа VS что-то с иксом (в части, где икс, степень точно будет больше)
3) Что-то с иксом VS что-то с иксом (сравниваем степень)

1 <= k <= 10^3
2 <= p <= 20

kx^p
kx
k

'''

import re

def check_degree(expression):
    terms = expression.split(' + ')
    max_degree = 0

    for term in terms:
        match = re.search(r'x\^(\d+)', term)
        
        if (match != None and max_degree < int(match.group(1))):
            max_degree = int(match.group(1))
        elif (term.find('x') >=0 and max_degree == 0):
            max_degree = 1
        
    return max_degree
    
first_exp = input()
second_exp = input()

first_exp_degree = check_degree(first_exp)
second_exp_degree = check_degree(second_exp)

if (first_exp_degree == second_exp_degree):
    print('YES')
    print('YES')
    print('YES')
elif(first_exp_degree < second_exp_degree):
    print('YES')
    print('NO')
    print('NO')
else:
    print('NO')
    print('YES')
    print('NO')
