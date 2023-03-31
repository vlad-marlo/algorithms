#include <cstddef>
#include <cstdio>
#include <vector>
#include <iostream>


template<typename T>
size_t getMinIndex(const std::vector<T>& data)
{
    if (data.size() == 0) 
        return 0;
    size_t min_idx = 0;
    T min_item = data.at(min_idx);
    for (size_t i = 1; i != data.size(); ++i)
    {
        const T& item = data.at(i);
        if (item < min_item)
        {
            min_item = item;
            min_idx = i;
        }
    }
    return min_idx;
}

template<typename T>
std::vector<T> selectionSort(std::vector<T> data)
{
    std::vector<T> newArr;
    newArr.reserve(data.size());
    size_t min_idx;
    while (!data.empty())
    {
        min_idx = getMinIndex(data);
        newArr.push_back(data.at(min_idx));
        data.erase(data.begin() + min_idx);
    }
    return newArr;
}

int main()
{
    std::vector<int> data = {5, 2, 9, 12, 3};
    std::vector<int> sorted = selectionSort(data);
    for (const auto& item: sorted)
    {
        printf("%d\n", item);
    }
    return 0;
}
