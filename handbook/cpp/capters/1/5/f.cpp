#include <iostream>
#include <vector>

struct Shift
{
    int x = 0;
    int y = 0;
};

const std::vector<Shift> SHIFTS = {
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, 1},
    {1, 1},
    {1, 0},
    {1, -1},
    {0, -1},
};

int main()
{
    size_t rows, cols, mines;
    std::cin >> rows >> cols >> mines;
    const int mineLabel = -1;
    std::vector<std::vector<int>> field(rows + 2, std::vector<int>(cols + 2));
    for (size_t i = 0; i != mines; ++i)
    {
        int row, col;
        std::cin >> row >> col;
        field[row][col] = mineLabel;
        for (auto shift: SHIFTS)
        {
            auto& cell = field[row + shift.x][col + shift.y];
            if (cell != mineLabel)
                ++cell;
        }
    }

    for (size_t row = 1; row <= rows; ++row)
    {
        for (size_t col = 1; col <= cols; ++col)
        {
            if (col > 1)
                std::cout << " ";
            if (field[row][col] == mineLabel)
                std::cout << "*";
            else
                std::cout << field[row][col];
        }
        std::cout << std::endl;
    }
    return 0;
}
