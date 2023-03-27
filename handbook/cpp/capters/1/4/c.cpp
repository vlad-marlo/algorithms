#include <iostream>

int main() {
    int num;
    std::cin >> num;
    if (num % 400 == 0 || (num % 100 != 0 && num % 4 == 0)) {
        std::cout << "YES";
    } else {
        std::cout << "NO";
    }
    std::cout << std::endl;
    return 0;
}

