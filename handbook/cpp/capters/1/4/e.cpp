#include <iostream>

int main() {
    int n, k;
    std::cin >> n >> k;
    for (int i = 1; i < n; ++i) {
        std::cout << "   ";
    }

    for (int i = 1; i <= k; ++i) {
        ++n;
        if (i < 10) {
            std::cout << " ";
        }

        std::cout << i << " ";
        if (n % 7 == 1 || k == i) {
            std::cout << std::endl;
        }
    }
    return 0;
}
