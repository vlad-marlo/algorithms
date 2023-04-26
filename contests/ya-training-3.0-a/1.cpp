#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

std::string read_data(const std::string& filename)
{
    std::fstream file (filename);
    std::string res = "", temporary;
    while (file >> temporary)
        res += temporary;
    return res;
}

std::string read_data()
{
    std::string res = "", temporary;
    while (std::cin >> temporary)
        res += temporary;
    return res;
}
