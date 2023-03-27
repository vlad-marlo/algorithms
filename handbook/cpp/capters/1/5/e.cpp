#include <algorithm>
#include <cstddef>
#include <iostream>
#include <string>

std::string read_data() 
{
    std::string data;
    std::getline(std::cin, data);
    return data;
}

bool is_palindrome(const std::string& s)
{
    int i = 0, j = static_cast<int>(s.size()) - 1;
    while (i < j)
    {
        if (s[i] == ' ')
            ++i;
        else if (s[j] == ' ')
            --j;
        else if (s[j] != s[i])
            return false;
        else
        {
            ++i;
            --j;
        }
    }
    return true;
}

int main() 
{
    std::cout << ((is_palindrome(read_data())) ? "YES" : "NO") << std::endl;
    return 0;
}
