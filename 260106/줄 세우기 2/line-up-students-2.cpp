#include <bits/stdc++.h>
using namespace std;

struct Student
{
    int height;
    int weight;
    int idx;
};

int main() 
{
    int N;
    cin >> N;
    vector<Student> students(N);

    for (int i = 0; i < N; i++) 
    {
        cin >> students[i].height >> students[i].weight;
        students[i].idx = i + 1;
    }

    // Please write your code here.
    sort(students.begin(), students.end(), [](const Student& a, const Student& b)
                                            {if(a.height != b.height)
                                                return a.height < b.height;
                                             return a.weight > b.weight;});

    for(const auto& s: students)
        cout << s.height << ' ' << s.weight << ' ' << s.idx << endl;
    return 0;
}