#include <vector>
#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>

std::vector<std::vector<int>> read_data(const std::string& filename)
{
    size_t n;
    std::fstream file (filename);
    file >> n;
    std::vector<std::vector<int>> data (n, std::vector<int>(3));
    for (size_t i = 0; i != n; ++i)
        for (size_t j = 0; j != 3; ++j)
            file >> data.at(i).at(j);
    return data;
}

int solution(const std::vector<std::vector<int>>& data)
{
    int ans = 0;
    int min_diff = 10000000;
    for (const auto& triple : data)
    {
        int a, b, c;
        a = std::min(std::min(triple.at(0), triple.at(1)), triple.at(2));
        c = std::max(std::max(triple.at(0), triple.at(1)), triple.at(2));
        b = triple.at(0) + triple.at(1) + triple.at(2) - a - c;

        ans += c;
        if ((c - b) % 91 != 0)
            min_diff = std::min(min_diff, c - b);
        if ((c - a) % 91 != 0)
            min_diff = std::min(min_diff, c - a);
    }
    if (ans % 91 == 0)
        ans -= min_diff;
    return ans;
}

int main()
{
    std::cout << solution(read_data("27_A_6057.txt")) << " " << solution(read_data("27_B_6057.txt")) << std::endl;
    return 0;
}
