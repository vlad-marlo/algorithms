#include <cmath>
#include <unordered_map>
#include <vector>
#include <string>
#include <tuple>
#include <fstream>
#include <algorithm>
#include <stdexcept>
#include <iostream>

std::unordered_map<int, std::vector<int>> read_data()
{
    std::fstream f ("2.txt");
    std::unordered_map<int, std::vector<int>> data;
    unsigned int n;
    f >> n;
    for (int i = 0; i != n; ++i)
    {
        int row, col;
        f >> row >> col;
        try {
            data.at(row).push_back(col);
        } catch (const std::out_of_range &e) {
            data[row] = std::vector<int>{col};
        }
    }
    for (std::pair<int, std::vector<int>> key : data) {
        std::sort(data.at(key.first).begin(), data.at(key.first).end());
    }
    return data;
}

std::pair<int, int> solution(std::unordered_map<int, std::vector<int>> data)
{
    int max_row = 0, min_place = 0;
    for (const std::pair<int, std::vector<int>>& item : data)
    {
        for (size_t i = 0; i != item.second.size() - 1; ++i)
        {
            const int& a = item.second.at(i), b = item.second.at(i + 1);
            if (b - a - i == 13 && max_row < item.first)
            {
                max_row = item.first;
                min_place = a + 1;
            }
        }
    }
    return std::pair<int, int> { min_place, max_row };
}

int main()
{
    std::pair<int, int> ans = solution(read_data());
    std::cout << ans.first << " " << ans.second << std::endl;
    return 0;
}
