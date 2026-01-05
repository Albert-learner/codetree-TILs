#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Person
{
    public:
        string name;
        int height;
        int weight;
};

int main() 
{
    int N;
    cin >> N;

    vector<Person> people;
    people.reserve(N);

    for(int i = 0; i < N; i++)
    {
        string name;
        int height, weight;
        cin >> name >> height >> weight;
        people.push_back({name, height, weight});
    }

    // Please write your code here.
    sort(people.begin(), people.end(), 
        [](const Person& a, const Person& b)
            {
                if(a.height != b.height)
                    return a.height < b.height;
                return a.weight > b.weight;
            });

    for(const auto& p: people)
    {
        cout << p.name << " " << p.height << " " << p.weight << endl;
    }
    return 0;
}