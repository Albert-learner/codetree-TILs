#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class PERSON 
{
    public:
        string name;
        int height;
        int weight;

        PERSON(string name, int height, int weight)
            : name(name), height(height), weight(weight) {}

        void print_person() const 
        {
            cout << name << " " << height << " " << weight << '\n';
        }
};

int main() 
{
    int N;
    cin >> N;

    vector<PERSON> people;
    people.reserve(N);

    for (int i = 0; i < N; i++) 
    {
        string name;
        int height, weight;
        cin >> name >> height >> weight;
        people.emplace_back(name, height, weight);
    }

    sort(people.begin(), people.end(),
         [](const PERSON& a, const PERSON& b)
         {
             return a.height < b.height;
         });

    for (const auto& person : people) 
    {
        person.print_person();
    }

    return 0;
}
