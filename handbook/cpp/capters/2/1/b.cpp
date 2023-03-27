#include <iostream>
#include <deque>
#include <string>

int main()
{
    int n, count;
    std::deque<std::string> res;
    std::cin >> n;
    for (int i = 0; i != n; ++i)
    {
        std::string name, layer;
        std::cin >> name >> layer;
        if (layer == "top")
            res.push_front(name);
        else
            res.push_back(name);
    }
    std::cin >> count;
    for (int i = 0; i != count; ++i)
    {
        size_t now;
        std::cin >> now;
        --now;
        std::cout << res.at(now) << std::endl;
    }
    return 0;
}
