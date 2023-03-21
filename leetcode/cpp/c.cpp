#include <cstdlib>
#include <functional>
#include <string>
#include <type_traits>
#include <unordered_map>
#include <stdexcept>
#include <iostream>

class Solution{
public:
    int lengthOfLongestSubstring(std::string s)
    {
        if (s.length() == 0) return 0;
        std::unordered_map<char, int> lastIndex;
        int result = 0, current = 0;
        for (size_t i = 0; i != s.size(); ++i)
        {
            const char& c = s.at(i);
            try {
                const int& lastI = lastIndex.at(c);
                if (lastI < i - current)
                    current++;
                else
                {
                    if (current > result)
                        result = current;
                    current = i - lastI;
                }
            } catch (const std::out_of_range &e) {
                current++;
            }
            lastIndex[c] = i;
        }
        if (current > result)
            result = current;
        return result;
    }
};
