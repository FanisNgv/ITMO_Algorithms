#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> numbers;
    int input;
    while (cin >> input)
    {
        numbers.push_back(input);
    }

    int n = numbers[0];
    int m = numbers[1];
    
    vector<int> ancestors;
    

    while (cin >> input)
    {
        ancestors.push_back(input);
    }
    
    std::vector<std::vector<int>> matx(n); 
    
    for (int i {0}; i < n-1; i++)
    {
        int x = ancestors[i] - 1;
        int y = i + 2;
    
        matx[x].push_back(y);
    }
    
    // for (size_t i = 0; i < matx.size(); ++i) { // Перебираем строки
    //     for (size_t j = 0; j < matx[i].size(); ++j) { // Перебираем элементы в строке
    //         std::cout << matx[i][j] << " ";
    //     }
    //     std::cout << std::endl; // Переход на новую строку после вывода каждой строки
    // }

    return 0;
}