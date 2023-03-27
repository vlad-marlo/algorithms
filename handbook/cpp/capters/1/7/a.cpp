#include <cstddef>
#include <cstdint>
#include <utility>
#include <vector>
#include <string>
#include <iostream>
#include <tuple>

std::pair<size_t, size_t> MatrixArgMax(const std::vector<std::vector<int>>& matrix)
{
    std::pair<int, int> ans = {0, 0};
    int max = matrix[0][0];
    for (size_t i = 0; i != matrix.size(); ++i)
    {
        const std::vector<int>& row = matrix.at(i);
        for (size_t j = 0; j != row.size(); ++j)
        {
            const int& item = row.at(j);
            if (item > max){
                max = item;
                ans = {i, j};
            }
        }
    }
    return ans;
}

std::vector<std::vector<int>> read_data()
{
    size_t rows, cols;
    std::cin >> rows >> cols;
    std::vector<std::vector<int>> data (rows, std::vector<int>(cols));
    for (size_t row_idx = 0; row_idx != data.size(); ++row_idx)
        for (size_t col_idx = 0; col_idx != cols; ++col_idx)
            std::cin >> data.at(row_idx).at(col_idx);
    return data;
}
