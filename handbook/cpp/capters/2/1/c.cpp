#include <algorithm>
#include <deque>
#include <iostream>
#include <string>

void MakeTrain()
{
    std::deque<int> train;
    std::string command;
    int wagon;
    size_t k;
    while (std::cin >> command)
    {
        if (command == "+left")
        {
            std::cin >> wagon;
            train.push_front(wagon);
        }
        else if (command == "+right")
        {
            std::cin >> wagon;
            train.push_back(wagon);
        }
        else if (command == "-right")
        {
            std::cin >> k;
            k = std::min(k, train.size());
            train.erase(train.end()-k, train.end());
        }
        else if (command == "-left")
        {
            std::cin >> k;
            k = std::min(k, train.size());
            train.erase(train.begin(), train.begin() + k);
        }
    }
    for (const auto& wagon: train)
        std::cout << wagon << " ";
    std::cout << std::endl;
}

int main()
{
    MakeTrain();
}
