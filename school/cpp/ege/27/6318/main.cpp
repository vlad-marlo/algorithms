#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

pair<vector<int>, int> read_data(const string& filename)
{
    size_t n, m;
    fstream file (filename);
    file >> n >> m;
    vector<int> data(n);
    for (size_t i = 0; i != n; ++i)
        file >> data.at(i);
    return pair<vector<int>, int> {data, m};
}

int solution(vector<int> data, int m)
{
    data.reserve(m);
    for (size_t i = 0; i != m; ++i)
        data.push_back(data.at(i));
    int sum = 0, ans = 0;
    for (size_t i = 0; i != 2 * m + 1; ++i)
        sum += data.at(i);
    ans = sum;
    for (size_t i = m + 1; i + m != data.size(); ++i)
    {
        sum += data.at(i + m) - data.at(i - m - 1);
        ans = max(sum, ans);
    }
    return ans;
}

int main()
{
    auto data_a = read_data("27A_6318.txt"), data_b = read_data("27B_6318.txt");
    cout << solution(data_a.first, data_a.second) << " " << solution(data_b.first, data_b.second) << endl;
    return 0;
}
