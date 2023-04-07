#include <cstdlib>
#include <vector>
#include <iostream>

template<typename T>
std::vector<T> quick_sort(const std::vector<T>& vec)
{
    if (vec.size() < 2)
        return vec;
    const T& pivot = vec.at(0);
    std::vector<T> less, greater;
    for (size_t i = 1; i != vec.size(); ++i)
    {
        const T& item = vec.at(i);
        if (item < pivot)
            less.push_back(item);
        else
            greater.push_back(item);
    }
    std::vector<T> sorted_less = quick_sort(less);
    std::vector<T> sorted_grtr = quick_sort(greater);
    sorted_less.push_back(pivot);
    sorted_less.insert(sorted_less.begin(), sorted_grtr.begin(), sorted_grtr.end());
    return sorted_less;
}


int main()
{
    return 0;
}
