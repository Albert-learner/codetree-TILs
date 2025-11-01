#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    int size = 2 * N - 1;

    for (int i = 0; i < size; i++) {
        int distance = abs(N - 1 - i);

        string line(distance, ' ');                     
        line += string(size - 2 * distance, '*');      

        cout << line << endl;
    }

    return 0;
}
