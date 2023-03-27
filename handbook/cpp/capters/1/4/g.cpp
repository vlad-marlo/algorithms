#include <iostream>
#include <cmath>

double log2(int n) {
    double ans = 0;
    for (int i = 0; i < n; i++) {
        ans += std::pow(-1, i) / (i + 1);
    }
    return ans;
}

int main() {
    int n;
    std::cin >> n;
    std::cout << log2(n) << std::endl;
    return 0;
}
