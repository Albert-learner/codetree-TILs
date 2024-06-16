#include <iostream>
#include <queue>
#include <tuple>

int n, gold_price;

int board[20][20];
int visited[20][20];

int dy[4] = { -1, 0, 1, 0 };
int dx[4] = { 0, 1, 0, -1 };

int answer;

void GetMaxGold(const int start_y, const int start_x)
{
       // 최대 시도해볼 수 있는 곳
	for (int k = 0; k < n; ++k)
	{
		for (int i = 0; i < n; ++i)
			std::fill(visited[i], visited[i] + n, false);

		visited[start_y][start_x] = true;
		std::queue<std::tuple<int, int, int>> bfs;
		bfs.push({ start_y, start_x, 0 });

		int total_gold_acquired = 0;
		while (bfs.size())
		{
			int y, x, step;
			std::tie(y, x, step) = bfs.front();
			bfs.pop();

			if (k < step)
				break;

			total_gold_acquired += board[y][x];

			for (int i = 0; i < 4; ++i)
			{
				int ny = y + dy[i];
				int nx = x + dx[i];

				if (ny < 0 || nx < 0 || n <= ny || n <= nx)
					continue;

				if (visited[ny][nx])
					continue;

				visited[ny][nx] = true;
				bfs.push({ ny, nx, step + 1 });
			}
		}

		int cost = k * k + (k + 1) * (k + 1);
		if (cost <= total_gold_acquired * gold_price)
			answer = std::max(answer, total_gold_acquired);
	}
}

int main()
{
	// 여기에 코드를 작성해주세요.
	std::cin >> n >> gold_price;
	for (int y = 0; y < n; ++y)
	{
		for (int x = 0; x < n; ++x)
			std::cin >> board[y][x];
	}

	for (int y = 0; y < n; ++y)
	{
		for (int x = 0; x < n; ++x)
			GetMaxGold(y, x);
	}

	std::cout << answer;

	return 0;
}