#include <cstddef>
#include <iostream>
#include <vector>
#include <algorithm>

struct Point{
    int x = 0;
    int y = 0;
};

bool operator < (const Point& left, const Point& right)
{
    return (left.x * left.x + left.y * left.y) < (right.x * right.x + right.y * right.y);
}

std::vector<Point> read_data()
{
    size_t n;
    std::cin >> n;
    std::vector<Point> data(n, {.x= 0, .y=0});
    for (size_t i = 0; i != data.size(); ++i)
    {
        std::cin >> data.at(i).x >> data.at(i).y;
    }
    return data;
}

int main()
{
    std::vector<Point> data = read_data();
    std::sort(data.begin(), data.end());

    for (const Point& p: data){
        std::cout << p.x << " " << p.y << std::endl;
    }

    return 0;
}

