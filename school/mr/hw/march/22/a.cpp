#include <exception>
#include <tuple>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <stdexcept>

std::vector<std::vector<int>> read_data(std::string filename)
{
    std::fstream file (filename);
    int n;
    file >> n;
    for (int i = 0; i < n; ++i)
    {
        try {
            int row, col;
            file >> row >> col;
        } catch (std::out_of_range) {
        
        }
    }
}

int main()
{
    return 0;
}
