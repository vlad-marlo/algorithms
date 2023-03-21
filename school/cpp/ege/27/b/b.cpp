#include <cstddef>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

std::vector<std::vector<int>> read_data(std::string filename)
{
    int n;
    std::fstream file (filename);
    file >> n;
    std::vector<std::vector<int>> data(n);
    for (size_t i = 0; i != data.size(); ++i)
    {
        data.at(i) = std::vector<int> (3);
        for (size_t n = 0; n != data.at(i).size(); ++n)
        {
            file >> data.at(i).at(n);
        }
    }
    return data;
}

int solution(std::vector<std::vector<int>> data)
{
    int sum = 0, mindiff = 100000000;
    for (size_t i = 0; i != data.size(); ++i)
    {
        std::vector<int> triple = data.at(i);
        std::sort(triple.rbegin(), triple.rend());
        int diff1 = abs(triple.at(0) - triple.at(1)), diff2 = abs(triple.at(0) - triple.at(2));
        sum += triple.at(0);
        if (diff1 % 91 != 0)
        {
            mindiff = std::min(mindiff, diff1);
        } 
        else if (diff2 % 91 != 0)
        {
            mindiff = std::min(mindiff, diff2);
        }
    }
    if (sum % 91 == 0)
    {
        return sum - mindiff;
    }
    return sum;
}

int main()
{
    std::cout << solution(read_data("27_A_6057.txt")) << " " << solution(read_data("27_B_6057.txt")) << std::endl;
    return 0;
}
