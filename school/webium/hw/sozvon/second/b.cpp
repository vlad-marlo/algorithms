#include <utility>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <fstream>
#include <string>

std::vector<int> read_data()
{
    int n;
    std::cin >> n;
    std::vector<int> data(n);
    for (size_t i = 0; i != data.size(); ++i)
        std::cin >> data.at(i);
    std::sort(data.begin(), data.end());
    return data;
}

std::vector<int> read_file(std::string filename)
{
    std::fstream file (filename);
    int n;
    file >> n;
    std::vector<int> data(n);
    for (size_t i = 0; i != data.size(); ++i)
        file >> data.at(i);
    std::sort(data.begin(), data.end());
    return data;
}

std::pair<double, double> strategy1(const std::vector<int>& data)
{
    int first_half = 0, second_half = 0;
    double sum = 0, max = 0;
    for (size_t i = 0; i != data.size(); ++i){
        const int& price = data.at(i);
        if (i < data.size() * 0.7)
        {
            first_half += price;
            max = std::max(price * 0.7, max);
        } else
        {
            max = std::max(price * 0.6, max);
            second_half += price;
        }
    }
    return std::pair<double, double> {first_half * 0.7 + int(second_half * 0.6), max};
}

std::pair<double, double> strategy2(const std::vector<int>& data)
{
    int first_half = 0, second_half = 0;
    double sum = 0, max = 0;
    for (size_t i = 0; i != data.size(); ++i){
        const int& price = data.at(i);
        if (i < data.size() * 0.5)
        {
            first_half += price;
            max = std::max(price * 0.6, max);
        } else
        {
            max = std::max(price * 0.65, max);
            second_half += price;
        }
    }
    return std::pair<double, double> {first_half * 0.6 + second_half * 0.65, max};
}

std::pair<double, double> solution(const std::vector<int>& data)
{
    std::pair<double, double> first = strategy1(data), second = strategy2(data);
    if (first.first < second.first)
        return std::pair<double, double>{second.first - first.first, second.second};
    return std::pair<double, double>{first.first - second.first, first.second};
}

void test_data()
{
    std::vector<int> data = {4, 13, 4, 23, 22, 20, 8, 6, 5, 12, 48, 22, 50, 12, 63, 23, 4, 8, 9, 11};
    std::pair<double, double> ans = solution(data);
    std::cout << "TEST DATA: " << ans.first << " " << ans.second << std::endl;
}

int main()
{
    test_data();
    std::pair<double, double> data = solution(read_file("26_6.txt"));
    std::cout << data.first << " " << data.second << std::endl;
    return 0;
}
