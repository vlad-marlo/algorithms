#include <vector>
#include <iostream>

template<typename T>
int binary_search(const std::vector<T>& data, const T& find)
{
    std::size_t start = 0, end = data.size() - 1;
    while (start <= end)
    {
        std::size_t mid = (start + end) / 2;
        const T& got = data.at(mid);
        if (got == find)
            return mid;
        if (got > find)
            end = mid - 1;
        else
            start = mid + 1;
    }
    return -1;
}

template<typename T>
const T* binary_search2(const std::vector<T>& data, const T& item)
{
    const T* low = &data.front();
    const T* high = &data.back();
    while (low <= high)
    {
        const T* guess = low + ((high - low) / 2);
        if (*guess == item)
            return guess;
        if (*guess > item)
            high = guess - 1;
        else
            low = guess + 1;
    }
    return nullptr;
}

int main()
{
    std::vector<int> data {1, 2, 4, 6, 7, 8, 9};
    for (std::size_t i = 0; i != data.size(); ++i)
    {
        printf("first algo: want: %lu; got: %d\n", i, binary_search(data, data.at(i)));
        printf("second algo: want: %i; got: %i\n", data.at(i), *binary_search2<int>(data, data.at(i)));
    }
}
