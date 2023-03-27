#include <algorithm>
#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <string>

std::pair<std::vector<int>, int> read_data(const std::string& filename)
{
    std::fstream file (filename);
    size_t n; int m;
    file >> n >> m;
    std::vector<int> data (2 * n);
    for (size_t i = 0; i != n; ++i)
        file >> data.at(i);
    return std::pair<std::vector<int>, int> {data, m};
}

int soluton(std::vector<int> data, int m)
{
    for (size_t i = 0; i != m; ++i)
        data.push_back(data.at(i));
    int sum = 0, ans;
    for (int i = 0; i < 2 * m + 1; ++i)
        sum += data.at(i);
    ans = sum;
    for (size_t i = m + 1; m + i != data.size(); ++i){
        sum = sum + data.at(i + m) - data.at(i - m - 1);
        ans = std::max(ans, sum);
    }
    return ans;
}

int main()
{
    std::cout << "TEST " << soluton(std::vector<int> {8,2,0,1,3,8,2,0,1,3}, 2) << std::endl;
    auto data_a = read_data("27A_6320.txt");
    auto data_b = read_data("27B_6320.txt");
    std::cout << soluton(data_a.first, data_a.second) << std::endl;
    std::cout << soluton(data_b.first, data_b.second) << std::endl;
    return 0;
}
