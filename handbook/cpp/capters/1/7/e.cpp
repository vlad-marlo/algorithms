#include <vector>
#include <string>

std::vector<std::vector<int>> Transpose(const std::vector<std::vector<int>>& matrix)
{
    std::vector<std::vector<int>> result(matrix[0].size(), std::vector<int>(matrix.size()));
    for (size_t i = 0; i != matrix.size(); ++i)
    {
        const std::vector<int>& row = matrix.at(i);
        for (size_t j = 0; j != row.size(); ++j)
        {
            result.at(j).at(i) = row.at(j);
        }
    }
    return result;
}
