#include <algorithm>
#include <iostream>
#include <string>
#include <fstream>
#include <bits/stdc++.h>
#include <vector>

int main()
{
    std::ifstream file ("26.txt");
    int len; file >> len;
    std::vector<int> data;
    for (int i = 0; i < len; i++)
    {
        int n;
        file >> n;
        data.push_back(n);
    }

    std::sort(data.begin(), data.end());
    std::reverse(data.begin(), data.end());
    std::vector<int> ans;

    ans.push_back(data[0]);
    for (int i = 0; i < len - 1; i++)
    {
        if (abs(ans.at(ans.size()-1) - data.at(i)) >= 3)
        {
            ans.push_back(data.at(i));
        }
    }
    std::cout << data.size() << " " << data.at(data.size()-1) << std::endl;
}
