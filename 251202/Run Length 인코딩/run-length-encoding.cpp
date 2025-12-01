#include <iostream>
#include <string>
#include <vector>
using namespace std;

string run_length_encoding(const string& input_str) {
    string ret_str;

    int n = input_str.length();
    if (n == 0) return ret_str;  // 빈 문자열 처리 (혹시 모를 경우)

    vector<int> indices;
    indices.push_back(-1);

    // 인접한 문자들이 다를 때마다 인덱스 기록
    for (int i = 0; i < n - 1; i++) {
        if (input_str[i] != input_str[i + 1]) {
            indices.push_back(i);
        }
    }
    indices.push_back(n - 1);

    // 구간 길이(연속된 문자 개수) 계산
    vector<int> cnts_lst;
    for (int i = 0; i < (int)indices.size() - 1; i++) {
        int diff = indices[i + 1] - indices[i];
        cnts_lst.push_back(diff);
    }

    // 인덱스에 해당하는 문자와 개수를 붙여서 결과 문자열 생성
    for (int i = 0; i < (int)cnts_lst.size(); i++) {
        int chr_idx = indices[i + 1];
        int cnts = cnts_lst[i];
        ret_str += input_str[chr_idx];
        ret_str += to_string(cnts);
    }

    return ret_str;
}

int main() {
    string input_str;
    getline(cin, input_str);  // 공백 포함 문자열 입력

    string answer = run_length_encoding(input_str);
    cout << answer.length() << "\n";
    cout << answer << "\n";

    return 0;
}
