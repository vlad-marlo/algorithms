#include <string>
#include <vector>

std::string Join(const std::vector<std::string>& tokens, char delimiter)
{
    if (tokens.size() == 0)
        return "";
    else if (tokens.size() == 1)
        return tokens[0];
    std::string result = "";
    for (const std::string& token : tokens)
        result += token + delimiter;
    result.pop_back();
    return result;
}
