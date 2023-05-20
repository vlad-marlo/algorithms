#include <iostream>


int main()
{
    for (int num = 45'000'000; num <= 50'000'000; ++num)
    {
        int count_of_prime_divs = 0;
        for (int div = 1; div * div <= num; ++div)
        {
            if (num % div == 0)
            {
                count_of_prime_divs += div % 2 + (num / div) % 2;
                if (div * div == num && div % 2 == 1)
                    --count_of_prime_divs;
            }
            if (count_of_prime_divs > 5)
                break;
        }
        if (count_of_prime_divs == 5)
            std::cout << num << std::endl;
    }
    return 0;
}
