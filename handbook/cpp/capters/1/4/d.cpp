#include <iostream>

int main() {
    int month, num;
    std::cin >> month >> num;
    if ((num % 400 == 0 || (num % 100 != 0 && num % 4 == 0)) && month == 2) {
        std::cout << 29 << std::endl;
        return 0;
    } else if (month == 2) {
        std::cout << 28 << std::endl;
        return 0;
    }
    switch (month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            std::cout << 31 << std::endl;
            break;
        default:
            std::cout << 30 << std::endl;
            break;
    }
    return 0;
}
