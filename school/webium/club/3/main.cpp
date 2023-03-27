#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>

std::vector<int> read_data(std::string filename)
{
    std::fstream file (filename);
    size_t n;
    file >> n;
    std::vector<int> data(n);
    for (size_t i = 0; i != n; ++i)
        file >> data.at(i);
    std::sort(data.begin(), data.end());
    return data;
}

int solution(const std::vector<int>& data)
{
    int ans = 0;
    const int& max = data.at(data.size()-1);
    for (size_t i = 0; i != data.size() - 2; ++i) 
    {
        const int& a = data.at(i);
        const int diff_a = a % 11;
        for (size_t j = i + 1; j != data.size() - 1; ++j)
        {
            const int& b = data.at(j);
            if (2 * b - a >= max)
                break;
            const int want_c = 2 * b - a;
            const int want_diff = 11 - (b + a) % 11;
            for (size_t k = j + 1; k != data.size(); ++k) {
                const int& c = data.at(k);
                if (c > want_c)
                    break;
                if (c == want_c && c % 11 != want_diff)
                    ++ans;
            }
        }
    }
    return ans;
}

void test()
{
    std::cout << "TEST DATA: " << solution(std::vector<int>{1, 3, 7, 14}) << std::endl;
}

int main()
{
    test();
    std::cout << "27 A: " << solution(read_data("27-A.txt")) << std::endl;
    std::cout << "27 B: " << solution(read_data("27-B.txt")) << std::endl;
    return 0;
}
