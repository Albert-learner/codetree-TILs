#include <iostream>
#include <vector>
#include <algorithm>
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

    vector<Student> students;
    students.reserve(N);

    for (int i = 1; i <= N; i++) 
    {
        int h, w;
        cin >> h >> w;
        students.push_back({h, w, i});
    }

    sort(students.begin(), students.end(), [](const Student& a, const Student& b) 
    {
        if (a.height != b.height) return a.height > b.height;  
        if (a.weight != b.weight) return a.weight > b.weight;  
        return a.idx < b.idx;                                  
    });

    for (const auto& s : students) 
    {
        cout << s.height << " " << s.weight << " " << s.idx << "\n";
    }

    return 0;
}
