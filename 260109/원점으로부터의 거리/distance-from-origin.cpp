#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

struct Point 
{
    int x;
    int y;
    int num; 
};

int main() 
{
    int N;
    cin >> N;

    vector<Point> points;
    points.reserve(N);

    for (int i = 1; i <= N; i++) 
    {
        int x, y;
        cin >> x >> y;
        points.push_back({x, y, i});
    }

    stable_sort(points.begin(), points.end(),
        [](const Point& a, const Point& b) {
            long long da = (long long)abs(a.x) + (long long)abs(a.y);
            long long db = (long long)abs(b.x) + (long long)abs(b.y);
            return da < db;
        }
    );

    for (const auto& p : points) 
    {
        cout << p.num << '\n';
    }

    return 0;
}

