#include <iostream>

#define MAX_N 100
#define MAX_NUM 10

#define UNDEFINED -1

using namespace std;

int n;

// 움직인 비둘기 번호와, 움직인 방향을 기록합니다.
int pigeon[MAX_N + 1], move_dir[MAX_N + 1];

// 현재 비둘기의 위치를 기록합니다. 
// UNDEFINED이면 아직 미정인 상태입니다.
int pos[MAX_NUM + 1];

int main() {
    // 입력
    cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> pigeon[i] >> move_dir[i];

    // 처음 비둘기의 상태는 전부 미정입니다.
    for(int i = 1; i <= MAX_NUM; i++)
        pos[i] = UNDEFINED;
    
    int move_cnt = 0;
    // 입력으로 주어진 움직임에 따라
    // 비둘기 위치를 이동시켜줍니다.
    for(int i = 1; i <= n; i++) {
        // 해당 비둘기의 위치가 미정이라면
        if(pos[pigeon[i]] == UNDEFINED) {
            // 주어진 첫 번째 위치에서 시작한다고
            // 생각하는게 비둘기의 이동 횟수를 
            // 최소로 할 수 있는 방법입니다.
            pos[pigeon[i]] = move_dir[i];
        }
        // 이미 비둘기의 위치가 정해져 있는데
        // 옮겨간 위치와 다른 위치라면
        else if(pos[pigeon[i]] != move_dir[i]) {
            // 이동시켜준 뒤,
            pos[pigeon[i]] = move_dir[i];
            // 답을 갱신합니다.
            move_cnt++;
        }
    }

    cout << move_cnt;
    return 0;
}
