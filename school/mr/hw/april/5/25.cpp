#include <iostream>
#include <cmath>

int main() 
{
    for (int i = 101000000; i < 102000000; ++i)
    {
        int c = 0;
        for (int div = 1; div < int(std::sqrt(i)) + 1; ++div)
        {
            if (i % div != 0) continue;
            int div2 = i / div;
            if (div % 2 == 0) ++c;
            if (div2 % 2 == 0 && div2 != div) ++c;
            if (c > 3) break;
        }
        if (c == 3)
            std::cout << i << std::endl;
    }
    return 0;
}
