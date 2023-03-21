#include <exception>
#include <tuple>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <stdexcept>

std::vector<std::vector<int>> read_data(std::string filename)
{
    std::fstream file (filename);
    std::vector<std::vector<int>> data(10001, std::vector<int>(10001));
    int n;
    file >> n;
    for (int i = 0; i < n; ++i)
    {
        int col, row;
        file >> col >> row;
        data.at(col).at(row)++;
    }
    return data;
}

std::pair<int, int> solution(const std::vector<std::vector<int>>& data)
{
    int min_row = 0, max_count = 0;
    for (size_t i = 0; i != data.size(); ++i)
    {
        const std::vector<int>& row = data.at(i);
        int local = 0;
        for (size_t j = 0; j != row.size(); ++j)
        {
            if (row.at(j) != 0)
                local++;
            else 
                local = 0;
            if (local > max_count)
            {
                max_count = local, min_row = i;
            }
        }
    }
    return std::pair<int, int> {min_row, max_count};
}

int main()
{
    std::pair<int, int> ans = solution(read_data("1.txt"));
    std::cout << ans.first << " "<< ans.second << std::endl;
    return 0;
}
