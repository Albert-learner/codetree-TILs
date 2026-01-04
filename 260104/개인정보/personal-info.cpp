#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Person 
{
    string name;
    int height;
    double weight;
};

int main() 
{
    vector<Person> people;
    people.reserve(5);

    for (int i = 0; i < 5; i++) 
    {
        string name;
        int height;
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

    vector<Person> height_sort = people;
    sort(height_sort.begin(), height_sort.end(),
         [](const Person& a, const Person& b) 
         {
             return a.height > b.height;
         });

    cout << "height\n";
    for (const auto& p : height_sort) 
    {
        cout << p.name << " " << p.height << " " << p.weight << "\n";
    }

    return 0;
}
