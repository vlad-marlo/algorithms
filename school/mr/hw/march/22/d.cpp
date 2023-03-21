#include <iterator>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <stdexcept>
#include <iostream>

int main()
{
    std::fstream f ("4.txt");
    int count, day_limit;
    f >> count >> day_limit;
    std::vector<int> data (count, 0);
    try {
        for (size_t i = 0; i != data.size(); ++i)
            f >> data.at(i);
    } catch (const std::out_of_range &e) {
    
    }
    std::sort(data.rbegin(), data.rend());
    int min = 10000000, sum = 0;
    for (size_t i = 0; i != day_limit; ++i)
    {
        try {
            const int& item = data.at(i);
            sum += item;
            min = std::min(min, item);
        } catch (const std::out_of_range &e) {
            std::cerr << "Got error: " << e.what() << std::endl;
        }
    }
    std::cout << sum << " " << min << std::endl;
}
