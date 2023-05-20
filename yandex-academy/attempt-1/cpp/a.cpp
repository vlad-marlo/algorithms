#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
#include <tuple>


struct DataCentre {
    std::vector<int> servers;
    int sum;
    int replaces;
    int index;
};

bool CompareMin(const DataCentre& lhs, const DataCentre& rhs) {
    return std::tie(lhs.sum * lhs.replaces, lhs.index) < std::tie(rhs.sum * rhs.replaces, rhs.index);
}

bool CompareMax(const DataCentre& lhs, const DataCentre& rhs) {
    return std::tie(lhs.sum * lhs.replaces, -lhs.index) < std::tie(rhs.sum * rhs.replaces, -rhs.index);
}

int main()
{
    int servers_per_centre, count_of_centres, q;
    std::cin >> count_of_centres >> servers_per_centre >> q;
    std::vector<DataCentre> centres (count_of_centres);
    for (int i = 0; i < count_of_centres; ++i) 
        centres[i] = DataCentre{std::vector<int>(servers_per_centre, 1), servers_per_centre, 0, i + 1};
    std::string cmd;
    for (int i = 0; i < q; ++i)
    {
        std::cin >> cmd;
        if (cmd == "GETMAX")
        {
            std::sort(centres.begin(), centres.end(), CompareMin);
            std::cout << centres.at(0).index;
        }
        else if (cmd == "GETMIN")
        {
            std::sort(centres.rbegin(), centres.rend(), CompareMax);
            std::cout << centres.at(0).index;
        }
        else if (cmd == "DISABLE")
        {
            int i, j;
            std::cin >> i >> j;
        }
    }
    return 0;
}
