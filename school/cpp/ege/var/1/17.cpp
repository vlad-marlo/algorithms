#include <vector>
#include <string>
#include <fstream>
#include <iostream>

struct Answer
{
    int count = 0;
    int max = 0;
};

std::vector<int> read_data(std::string file_name)
{
    size_t n;
    std::fstream file (file_name);
    file >> n;
    std::vector<int> data(n);
    for (size_t i = 0; i != n; ++i)
        file >> data.at(i);
    return data;
}

Answer solution(std::vector<int> data)
{
    int min_pair = 100000000;
    int count = 0, max = 0;
    int min = 40;
    for (size_t i = 1; i != data.size(); ++i)
    {
        const int& a = data.at(i), b = data.at(i - 1);
        if ((a % min == 0) && (b % min == 0))
        {
            ++count;
            if ((a + b) < min_pair)
            {
                max = std::max(a, b);
                min_pair = a + b;
            }
        }
    }
    return Answer{.count=count, .max=max };
}

int main()
{
    Answer ans = solution(read_data("17_4367.txt"));
    std::cout << ans.count << " " << ans.max << std::endl;
}
