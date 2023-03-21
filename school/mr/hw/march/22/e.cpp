#include <tuple>
#include <utility>
#include <vector>
#include <fstream>
#include <string>
#include <iostream>
#include <stdexcept>
#include <algorithm>

std::tuple<int, int, std::vector<int>> read_data()
{
    int n, k, m;
    std::fstream f ("5.txt");
    f >> n >> k >> m;
    std::vector<int> data (n);
    for (size_t i = 0; i != data.size(); ++i)
        f >> data.at(i);
    std::sort(data.begin(), data.end());
    return std::tuple<int, int, std::vector<int>> { k, m, data };
}

std::pair<int, int> solution(const int& k, const int& m, const std::vector<int>& data)
{
    int min_high = 1000000;
    int avg_cheap = 0;
    for (size_t i = 0; i != k; ++i)
    {
        const int& item = data.at(i);
        avg_cheap += item;
    }
    for (size_t i = data.size() - m; i != data.size(); ++i)
        min_high = std::min(min_high, data.at(i));
    return std::pair<int, int> { min_high, avg_cheap / k };
}

int main()
{
    std::tuple<int, int, std::vector<int>> vec = read_data();
    int k = std::get<0>(vec), m = std::get<1>(vec);
    std::vector<int> data = std::get<2>(vec);
    std::pair<int, int> answer = solution(k, m, data);
    std::cout << answer.first << " " << answer.second << std::endl;
    return 0;
}
