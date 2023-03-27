#include <iostream>

int main() {
    int num;
    std::cin >> num;
    int ans = 0;
    while (num != 0) {
        ans += num % 10;
        num /= 10;
    }
    std::cout << ans << std::endl;
}
