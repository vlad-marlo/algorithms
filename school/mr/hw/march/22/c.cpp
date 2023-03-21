#include <unordered_map>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <stdexcept>
#include <algorithm>

std::unordered_map<int, std::vector<int>> read_data()
{
    std::fstream f ("3.txt");
    std::unordered_map<int, std::vector<int>> data;
    unsigned int n;
    f >> n;
    for (int i = 0; i != n; ++i)
    {
        int key, val;
        f >> key >> val;
        try {
            data.at(key).push_back(val);
        } catch (const std::out_of_range &e) {
            data[key] = std::vector<int>{val};
        }
    }
    for (const std::pair<int, std::vector<int>> item: data)
    {
        std::sort(data.at(item.first).begin(), data.at(item.first).end());
    }
    return data;
}

std::pair<int, int> solution(std::unordered_map<int, std::vector<int>> data)
{
    int max_row = 0, min_place = 0;
    int c = 0;
    for (const std::pair<int, std::vector<int>> item : data)
    {
        std::vector<int> row = item.second;
        if (row.size() <= 1)
        {
            continue;
        }
        for (size_t i = 0; i != row.size() - 1; ++i)
        {
            int a = row.at(i), b = row.at(i + 1);
            if (((b - a) == 3 || (b - a) == 3) && max_row < item.first)
            {
                max_row = item.first;
                min_place = a + 1;
            }
        }
    }
    return std::pair<int, int>{ max_row, min_place };
}

int main()
{
    std::pair<int, int> answer = solution(read_data());
    std::cout << answer.first << " " << answer.second << std::endl;
    return 0;
}
