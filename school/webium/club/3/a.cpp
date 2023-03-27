#include <algorithm>
#include <stdexcept>
#include <type_traits>
#include <unordered_map>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>

std::vector<int> read_data(std::string filename)
{
    std::fstream file (filename);
    int n;
    file >> n;
    std::vector<int> data(300, 0);
    for (int i = 0; i < n; ++i)
    {
        int num;
        file >> num;
        ++data.at(num);
    }
    return data;
}

int solution(std::vector<int> data)
{
    int ans = 0;
    for (int a = 1; a != 100; ++a)
    {
        for (int b = a; b != 101; ++b)
        {
            for (int c = b; c != 102; ++c)
            {
                int data_a = data.at(a);
                int data_b = data.at(b);
                if (b == a ){
                    if (data_b < 2)
                        continue;
                    --data_b;
                    --data_a;
                }
                int data_c = data.at(c);
                if (c == b)
                {
                    if (data_b < 2)
                        continue;
                    if (c == a)
                    {
                        if (data_a < 2)
                            continue;
                        --data_a;
                    }
                    --data_b;
                    --data_c;
                }
                if ((data_a + data_b + data_c) % 11 == 0 && data_c == 2 * data_b - data_a)
                    ans += data_a * data_b * data_c;
            }
        }
    }
    return ans;
}

void test_data()
{
    std::cout << "TEST DATA: " << solution(read_data("test.txt")) << std::endl;
}

int main()
{
    test_data();
    std::cout << "27 A: " << solution(read_data("27-A.txt")) << std::endl;
    std::cout << "27 B: " << solution(read_data("27-B.txt")) << std::endl;
}
