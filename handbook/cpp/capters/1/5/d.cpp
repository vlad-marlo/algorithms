#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<std::string> data;
    std::string temp;
    while (std::getline(std::cin, temp)){
        data.push_back(temp);
    }
    std::sort(data.rbegin(), data.rend());
    for (const std::string& i : data) {
        std::cout << i << std::endl;
    }
    return 0;
}
