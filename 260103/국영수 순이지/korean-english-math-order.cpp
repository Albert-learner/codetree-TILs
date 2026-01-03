#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class STUDENT 
{
    public:
        string name;
        int kor, eng, math;

        STUDENT(string name, int kor, int eng, int math)
            : name(name), kor(kor), eng(eng), math(math) {}
};

int main() 
{
    int N;
    cin >> N;

    vector<STUDENT> students;
    students.reserve(N);

    for (int i = 0; i < N; i++) 
    {
        string name;
        int kor, eng, math;
        cin >> name >> kor >> eng >> math;
        students.emplace_back(name, kor, eng, math);
    }

    sort(students.begin(), students.end(),
         [](const STUDENT& a, const STUDENT& b) 
         {
             if (a.kor != b.kor) return a.kor > b.kor;
             if (a.eng != b.eng) return a.eng > b.eng;
             return a.math > b.math;
         });

    for (const auto& student : students) 
    {
        cout << student.name << " "
             << student.kor << " "
             << student.eng << " "
             << student.math << '\n';
    }

    return 0;
}
