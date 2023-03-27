#include <cctype>
#include <iostream>
#include <string>

bool valid(std::string string) {
    int lower = 0, upper = 0, num = 0, other = 0;
    for (size_t i = 0; i != string.size(); ++i) {
        char c = string.at(i);
        if (!(int(c) >= 33 && 126 >= int(c))) { return false; }
        if (isupper(int(c))) { ++upper; } else if (isdigit(int(c))) { ++num; } else if (islower(int(c))) { ++lower; } else { ++other; }
    }
    int counter = 0;
    if (lower == 0) { ++counter; }
    if (upper == 0) { ++counter; }
    if (num == 0) { ++counter; }
    if (other == 0) { ++counter; }
    return counter <= 1;
}

int main() {
    std::string pass;
    std::cin >> pass;
    if (pass.size() >= 8 && pass.size() <= 14 && valid(pass)) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }
    return 0;
}
