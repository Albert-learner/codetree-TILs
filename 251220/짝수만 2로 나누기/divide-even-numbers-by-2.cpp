#include <iostream>
#include <vector>
using namespace std;

vector<int> modify(vector<int> lst) {
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] % 2 == 0) {
            lst[i] /= 2;
        }
    }
    return lst;
}

int main() {
    int N;
    cin >> N;

    vector<int> n_lst(N);
    for (int i = 0; i < N; i++) {
        cin >> n_lst[i];
    }

    vector<int> result = modify(n_lst);

    for (int x : result) {
        cout << x << " ";
    }

    return 0;
}
