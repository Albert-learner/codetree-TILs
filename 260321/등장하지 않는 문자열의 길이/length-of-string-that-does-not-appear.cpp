#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int n;
string str;

int main() {
    // 입력
    cin >> n;
    
    cin >> str;

    int ans = 1;

    // 1씩 늘려가면서 어느 길이까지 2번 등장하지는지 모두 시도해봅니다.
    for(int i = 1; i < n; i++) {
        // 모든 길이가 i인 부분 문자열에 대해 쌍을 짓고
        // 둘이 완전히 똑같은지 확인합니다.

        // twice : i 길이의 2회 이상 등장하는 부분 문자열이 존재하면 true
        bool twice = false;

        for(int j = 0; j <= n - i; j++) {
            for(int k = j + 1; k <= n - i; k++) {
                // issame : j부터 i길이의 부분 문자열과
                // k부터 i길이의 부분 문자열이 완전히 같으면 true
                bool issame = true;

                for(int l = 0; l < i; l++) {
                    if(str[j + l] != str[k + l])
                        issame = false;
                }

                if(issame) twice = true;
            }
        }

        if(twice)
            ans = i + 1;
        else
            break;
    }

    cout << ans;
    
    return 0;
}
