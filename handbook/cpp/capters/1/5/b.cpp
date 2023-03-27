#include <iostream>
#include <string>

char get_group_of_char(char c) {
    char append = '0';
    switch (c) {
        case 'b':
        case 'f':
        case 'p':
        case 'v':
            append = '1';
            break;
        case 'c':
        case 'g':
        case 'j':
        case 'k':
        case 'q':
        case 's':
        case 'x':
        case 'z':
            append = '2';
            break;
        case 'd':
        case 't':
            append = '3';
            break;
        case 'l':
            append = '4';
            break;
        case 'm':
        case 'n':
            append = '5';
            break;
        case 'r':
            append = '6';
            break;
    }
    return append;
}

int main() {
    std::string before, after = "";
    std::cin >> before;
    after.push_back(before.at(0));
    for (size_t i = 0; i != before.size(); ++i) {
        if (after.size() >= 4) {
            break;
        }
        char c = before.at(i);
        if (i == 0 || c == 'a' || c == 'e' || c == 'h' || c == 'i' || c == 'o' || c == 'u' || c == 'w' || c == 'y') {
            continue;
        }
        char append = get_group_of_char(c);
        if (after.at(after.size()-1) != append && '0' != append) {
            after.push_back(append);
        }
    }
    while (after.size() < 4) {
        after.push_back('0');
    }
    std::cout << after << std::endl;

    return 0;
}
