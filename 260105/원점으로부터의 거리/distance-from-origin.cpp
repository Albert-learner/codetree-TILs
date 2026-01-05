#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Points
{
    int x;
    int y;
    int num;
};

int main() 
{
    int N;
    cin >> N;
    
    vector<Points> points;
    points.reserve(N);

    // Please write your code here.
    for(int i = 1; i <= N; i++)
    {
        int x, y;
        cin >> x >> y;
        points.push_back({x, y, i});
    }

    sort(points.begin(), points.end(), 
        [](const Points& a, const Points& b)
            {
                return abs(a.x) + abs(a.y) < abs(b.x) + abs(b.y);
            });

    for(const auto& p: points)
    {
        cout << p.num << endl;
    }
    return 0;
}
