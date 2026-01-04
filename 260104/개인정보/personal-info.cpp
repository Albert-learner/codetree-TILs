#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Person 
{
    string name;
    double height;
    double weight;
};

int main() 
{
    vector<Person> people;
    people.reserve(5);

    for (int i = 0; i < 5; i++) 
    {
        string name;
        double height;
        double weight;
        cin >> name >> height >> weight;
        people.push_back({name, height, weight});
    }

    vector<Person> name_sort = people;
    sort(name_sort.begin(), name_sort.end(),
         [](const Person& a, const Person& b) 
         {
             return a.name < b.name;
         });

    cout << "name\n";
    for (const auto& p : name_sort) 
    {
        cout << p.name << " " << p.height << " " << p.weight << "\n";
    }

    cout << "\n";

    // 키 기준 내림차순 정렬
    vector<Person> height_sort = people;
    sort(height_sort.begin(), height_sort.end(),
         [](const Person& a, const Person& b) {
             return a.height > b.height;
         });

    cout << "height\n";
    for (const auto& p : height_sort) {
        cout << p.name << " " << p.height << " " << p.weight << "\n";
    }

    return 0;
}
