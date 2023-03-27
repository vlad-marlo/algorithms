#include <iostream>
#include <vector>

std::vector<int> read_data() {
    int n;
    std::cin >> n;
    std::vector<int> data;
    data.reserve(n);
    for (int i = 0; i < n; ++i) {
        int temp;
        std::cin >> temp;
        data.push_back(temp);
    }
    return data;
}

std::vector<int> solution(std::vector<int> data) {
    std::vector<int> answer(data.size(), 0);
    for (size_t i = 0; i != data.size(); ++i) {
        answer[data.at(i) - 1] = i + 1;
    }
    return answer;
}

int main() {
    std::vector<int> data = solution(read_data());
    for (int item : data) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
}
