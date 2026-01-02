#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define MAX_N 10

using namespace std;

class PERSON
{
    public:
        string name, road, province;

        PERSON(string n, string r, string p): name(n), road(r), province(p) {}

        void print_info() const
        {
            cout << "name " << name << endl;
            cout << "addr " << road << endl;
            cout << "city " << province << endl;
        }
};

int main() 
{
    int n;
    string name[MAX_N], street_address[MAX_N], region[MAX_N];
    cin >> n;
    vector<PERSON> people;
    people.reserve(n);

    for (int i = 0; i < n; i++) {
        string name, road, province;
        cin >> name >> road >> province;
        people.emplace_back(name, road, province);
    }

    sort(people.begin(), people.end(),
         [](const PERSON& a, const PERSON& b) {
             return a.name > b.name;
         });

    people[0].print_info();

    return 0;
}
