#include <algorithm>
#include <cmath>
#include <cstddef>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>

std::vector<std::vector<int>> read_data(std::string filename) {
    size_t n;
    std::fstream file (filename);
    file >> n;
    std::vector<std::vector<int>> data(n);
    for (size_t i = 0; i != data.size(); ++i) {
        data.at(i) = std::vector<int> (2);
        file >> data.at(i).at(0) >> data.at(i).at(1);
    }
    return data;
}

int solution(std::vector<std::vector<int>> data) {
    int sum = 0, diff = 100000;
    for (std::vector<int> pair: data) {
        sum += std::max(pair.at(0), pair.at(1));
        if (std::abs(pair.at(0) - pair.at(1)) % 5 != 0) {
            diff = std::min(diff, std::abs(pair.at(0) - pair.at(1)));
        }
    }
    if (sum % 5 == 0) {
        return sum - diff;
    }
    return sum;
}

int main() {
    std::cout << "A: " << solution(read_data("27-A_1.txt")) << std::endl;
    std::cout << "B: " << solution(read_data("27-B_1.txt")) << std::endl;
}
