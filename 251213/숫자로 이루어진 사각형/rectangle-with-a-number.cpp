#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

void print_rect_numbers(int n)
{
	int quota = (n * n) / 9;
	int rest = (n * n) % 9;

	vector<int> nums_lst;
	for (int i = 1; i <= quota; ++i)
	{
		for (int j = 1; j <= 9; ++j)
			nums_lst.push_back(j);
	}

	for (int i = 1; i <= rest; ++i)
	{
		nums_lst.push_back(i);
	}

	for (int i = 0; i < nums_lst.size(); ++i)
	{
		if ((i + 1) % n == 0)
			cout << nums_lst[i] << endl;
		else
			cout << nums_lst[i] << ' ';
	}
}

int main()
{
	int N;
	cin >> N;

	print_rect_numbers(N);
	return 0;
}
