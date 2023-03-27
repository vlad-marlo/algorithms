#include <iostream>
#include <string>

template<typename T1>
void Print(const T1& t1, const std::string& t2)
{
    int now = 0;
    for (auto iter = t1.begin(); iter != t1.end(); ++iter)
    {
        if (now != 0)
            std::cout << t2;
        std::cout << *iter;
        ++now;
    }
    std::cout << std::endl;
}
