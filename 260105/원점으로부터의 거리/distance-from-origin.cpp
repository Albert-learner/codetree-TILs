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

    sort(points.begin(), points.end(),
         [](const Point& a, const Point& b) 
         {
             return abs(a.x) + abs(a.y) < abs(b.x) + abs(b.y);
         });

    for (const auto& p : points) 
    {
        cout << p.num << '\n';
    }

    return 0;
}
