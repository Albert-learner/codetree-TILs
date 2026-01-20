#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    const int SIZE = 200001;
    vector<int> colored(SIZE, 0);          
    vector<int> white(SIZE, 0), black(SIZE, 0);

    int cur_dir = 100000;
    long long w = 0, b = 0, g = 0;

    for (int t = 0; t < N; t++) 
    {
        int size;
        char mv_dir;
        cin >> size >> mv_dir;

        if (mv_dir == 'R') 
        {
            for (int i = cur_dir; i < cur_dir + size; i++) 
            {
                colored[i] = 2;
                black[i] += 1;
            }
            cur_dir += size - 1;
        } 
        else 
        { 
            for (int i = cur_dir - size + 1; i <= cur_dir; i++) 
            {
                colored[i] = 1;
                white[i] += 1;
            }
            cur_dir -= size - 1;
        }
    }

    for (int i = 0; i < SIZE; i++) 
    {
        if (white[i] >= 2 && black[i] >= 2) g++;
        else if (colored[i] == 1) w++;
        else if (colored[i] == 2) b++;
    }

    cout << w << " " << b << " " << g << "\n";
    return 0;
}