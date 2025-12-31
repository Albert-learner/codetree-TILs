#include <iostream>
#include <string>

using namespace std;

class game_info 
{
    public:
        string person_id;
        string level;

        // 생성자 (기본값 포함)
        game_info(string pid = "codetree", string lvl = "10") {
            person_id = pid;
            level = lvl;
        }

        void print_info() {
            cout << "user " << person_id << " lv " << level << '\n';
        }
};

int main() 
{
    string person_id, level;
    cin >> person_id >> level;

    game_info games;
    games.print_info();

    games = game_info(person_id, level);
    games.print_info();

    return 0;
}
