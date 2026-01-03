#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Student 
{
    public:
        string name;
        int first, second, third;

        Student(string name, int first, int second, int third)
            : name(name), first(first), second(second), third(third) {}
};

int main() 
{
    int N;
    cin >> N;

    vector<Student> students;
    students.reserve(N);

    for (int i = 0; i < N; i++) 
    {
        string name;
        int first, second, third;
        cin >> name >> first >> second >> third;
        students.emplace_back(name, first, second, third);
    }

    sort(students.begin(), students.end(),
         [](const Student& a, const Student& b) 
         {
             return (a.first + a.second + a.third) <
                    (b.first + b.second + b.third);
         });

    for (const auto& s : students) 
    {
        cout << s.name << " "
             << s.first << " "
             << s.second << " "
             << s.third << '\n';
    }

    return 0;
}
