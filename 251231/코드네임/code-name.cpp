#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Members {
public:
    string name;
    int score;

    Members(string n, int s) : name(n), score(s) {}
};

int main() {
    vector<Members> members;

    for (int i = 0; i < 5; i++) {
        string name;
        int score;
        cin >> name >> score;
        members.emplace_back(name, score);
    }

    // score가 가장 작은 멤버 찾기
    auto min_member = min_element(
        members.begin(),
        members.end(),
        [](const Members& a, const Members& b) {
            return a.score < b.score;
        }
    );

    cout << min_member->name << " " << min_member->score << endl;

    return 0;
}
