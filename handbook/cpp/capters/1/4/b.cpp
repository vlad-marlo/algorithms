#include <algorithm>
#include <iostream>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    for (;a > b || b > c;) {
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        if (b > c) {
            int temp = b;
            b = c;
            c = temp;
        }
    }
    if (a == 0 || b == 0 || c == 0 || !(a + b > c && a + c > b && b + c > a)) {
        std::cout << "UNDEFINED" << std::endl;
    } else if (a * a + b * b == c * c || a * a == b * b + c * c || b * b == a * a + c * c) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }
    return 0;
}
