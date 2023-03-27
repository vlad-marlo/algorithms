#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <string>
#include <iostream>

std::vector<int> read_data(const std::string& s)
{
    std::fstream file (s);
    size_t n;
    file >> n;
    std::vector<int> data (n);
    for (size_t i = 0; i != n; ++i)
        file >> data.at(i);
    return data;
}

int solution(const std::vector<int>& data)
{
    int local_sum = 0, sum = 0, max = 0;
    const size_t& n = data.size();
    std::vector<int> b (data.size());
    for (size_t i = 0; i != n; ++i)
    {
        const int& val = data.at(i);
        local_sum += val;
        sum += val;
        b.at(i) = local_sum;
    }
    for (size_t i = 0; i != n; ++i)
        local_sum += int(i) * data.at(i);
    max = local_sum;

    for (size_t i = 1; i != n; ++i)
    {
        const int& b_data = b.at(i - 1);
        local_sum = b_data - sum + b_data;
        max = std::max(local_sum, max);
    }

    return max;
}

int main()
{
    std::cout << "TEST: " << solution(read_data("test.txt")) << std::endl;
    std::cout << solution(read_data("27A_5644.txt")) << " ";
    std::cout << solution(read_data("27B_5644.txt")) << std::endl;
    return 0;
}
