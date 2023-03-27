#include <algorithm>
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>
#include <iostream>

std::string CommonPrefix(const std::vector<std::string>& words)
{
    std::string answer = "";
    size_t max_size = 1000000000;
    
        for (size_t i = 0; i != max_size; ++i)
        {
            try {
                const char& first = words.at(0).at(i);
                for (const auto&s : words)
                    if (s.at(i) != first)
                        return answer;
                answer.push_back(first);
            } catch (std::out_of_range) {
                return answer;
            }
        }
    return answer;
}
