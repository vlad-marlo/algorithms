#include <cstddef>
#include <string>
#include <utility>
#include <vector>
#include <iostream>

std::vector<size_t> get_indexes_of_delimiter(const std::string& str, char delimiter)
{
    std::vector<size_t> indexes;
    indexes.push_back(-1);
    for (size_t i = 0; i != str.size(); ++i)
    {
        if (str.at(i) == delimiter){
            indexes.push_back(i);
        }
    }
    indexes.push_back(str.size());
    return indexes;
}

std::vector<std::string> Split(const std::string& str, char delimiter)
{
    std::vector<size_t> indexes = get_indexes_of_delimiter(str, delimiter);
    if (indexes.size() < 1)
        return std::vector<std::string>{str};

    std::vector<std::string> result;
    result.reserve(indexes.size());

    for (size_t index = 0; index + 1 != indexes.size(); ++index)
    {
        const size_t& start = indexes.at(index), end = indexes.at(index+1);
        result.push_back(str.substr(start+1, end-start-1));
    }

    return result;
}

std::pair<std::string, char> read_data()
{
    std::string string;
    char delimiter;
    std::getline(std::cin, string);
    std::cin >> delimiter;
    return std::pair<std::string, char>{string, delimiter};
}

int main()
{
    std::pair<std::string, char> params = read_data();
    std::vector<std::string> data = Split(params.first, params.second);
    for (const auto& str : data)
    {
        std::cout << str << std::endl;
    }
    return 0;
}
