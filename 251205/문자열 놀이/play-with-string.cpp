#include <iostream>
#include <string>
using namespace std;

int main() {
    string s_str;
    int questions;
    cin >> s_str >> questions;

    // 문자열을 직접 수정해 나감
    for (int qi = 0; qi < questions; qi++) {
        string n, a, b;
        cin >> n >> a >> b;

        if (n == "1") {
            // 인덱스 a, b 위치를 서로 교환 (1-based → 0-based)
            int a_int = stoi(a);
            int b_int = stoi(b);
            swap(s_str[a_int - 1], s_str[b_int - 1]);
        } else if (n == "2") {
            // 문자 a를 모두 b로 변경
            char from = a[0];
            char to = b[0];
            for (int i = 0; i < (int)s_str.size(); i++) {
                if (s_str[i] == from) {
                    s_str[i] = to;
                }
            }
        }

        cout << s_str << '\n';
    }

    return 0;
}
