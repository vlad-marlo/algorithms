#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <iostream>

std::vector<int> read_data(std::string file_name)
{
    std::fstream file (file_name);
    size_t n;
    file >> n;
    std::vector<int> data (n);
    for (size_t i = 0; i != n; ++i)
        file >> data.at(i);
    std::sort(data.begin(), data.end());
    return data;
}

std::pair<int, int> solution(const std::vector<int>& data)
{
    int div17odd = 0, div17even = 0, even = 0, odd = 0;
    for (const int& i : data)
    {
        if (i % 34 == 0 && i > div17even)
            even = std::max(even, div17even), div17even = i;
        else if (i % 17 == 0 && i > div17odd)
            odd = std::max(odd, div17odd), div17odd = i;
        else if (i % 2 == 0)
            even = std::max(i, even);
        else 
            odd = std::max(i, odd);
    }
    return (div17odd + odd > even + div17even) ? std::pair<int, int> { std::max(div17odd, odd), std::min(div17odd, odd) } : std::pair<int, int> { std::max( div17even, even), std::min(div17even, even) };
}

int main()
{
    const std::pair<int, int>& a = solution(read_data("27991_A.txt")), b = solution(read_data("27991_B.txt"));
    std::cout << a.first << " " << a.second << std::endl << b.first << " " << b.second << std::endl;
}
