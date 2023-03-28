#include <iostream>
#include <vector>

int main()
{
    std::vector<int> data {1, 2, 3, 4};
    for (auto i = data.begin(); i != data.end(); ++i)
    {
        std::cout << *i << std::endl;
    }
    return 0;
}
