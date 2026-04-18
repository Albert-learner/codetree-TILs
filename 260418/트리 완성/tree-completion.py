#include <iostream>

#define MAX_N 100000

using namespace std;

// 변수 선언
int n, m;

// 번호별 그룹을 관리합니다.
int uf[MAX_N + 1];

// 사이클 없이 최대로 이용할 수 있는 간선의 수를 구합니다.
int max_cnt;

// x의 대표 번호를 찾아줍니다.
int Find(int x) {
    // x가 루트 노드라면 x값을 반환합니다.
    if(uf[x] == x)
        return x;
    // x가 루트 노드가 아니라면
    // x의 부모인 uf[x]에서 탐색을 더 진행한 뒤
    // 찾아낸 루트 노드를 uf[x]에 넣어줌과 동시에
    // 해당 노드값을 반환합니다.
    return uf[x] = Find(uf[x]);
}

// x, y가 같은 집합이 되도록 합니다.
void Union(int x, int y) {
    // x, y의 대표 번호를 찾은 뒤
    // 연결해줍니다.
    int X = Find(x);
    int Y = Find(y);

    uf[X] = Y;
}

int main() {
    // 입력:
    cin >> n >> m;

    // 초기 uf 값을 설정합니다.
    for(int i = 1; i <= n; i++)
        uf[i] = i;

    // m개의 간선 정보를 입력받습니다.
    // 사이클이 생기지 않도록 최대로 간선을 선택해줍니다.
    for(int i = 1; i <= m; i++) {
        int x, y;
        cin >> x >> y;

        // 두 정점이 아직 연결되어 있지 않다면
        // 해당 간선을 사용해도 사이클이 생기지 않습니다.
        if(Find(x) != Find(y)) {
            max_cnt++;
            Union(x, y);
        }
    }

	// 트리는 n - 1개의 간선으로 이루어져 있기에
    // m - max_cnt 만큼의 간선을 기존 그래프에서 잘라내고
    // n - 1 - max_cnt 만큼의 간선이 추가로 필요합니다.
	cout << n - 1 - max_cnt + (m - max_cnt);
    return 0;
}
