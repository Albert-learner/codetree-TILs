#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int a, b, c, d;
    cin >> a >> b;
    cin >> c >> d;

    // Please write your code here.
    if(a > c && b > d)
    {
        swap(a, c);
        swap(b, d);
    }

    if(b >= c)
    {
        vector<int> a_areas, b_areas;
        for(int i = a; i <= b; i++) a_areas.push_back(i);
        for(int i = c; i <= d; i++) b_areas.push_back(i);

        vector<int> total_areas = a_areas;
        total_areas.insert(total_areas.end(), b_areas.begin(), b_areas.end());

        sort(total_areas.begin(), total_areas.end());
        total_areas.erase(unique(total_areas.begin(), total_areas.end()), total_areas.end());

        cout << total_areas.back() - total_areas.front() << '\n';
    }
    else
    {
        vector<int> a_areas, b_areas;
        for (int i = a; i < b; i++) a_areas.push_back(i);
        for (int i = c; i < d; i++) b_areas.push_back(i);

        cout << (int)a_areas.size() + (int)b_areas.size() << '\n';
    }
    return 0;
}