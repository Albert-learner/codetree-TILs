#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;

    vector<pair<char, int>> changes;
    for (int i = 0; i < N; i++) 
    {
        char c;
        int s;
        cin >> c >> s;
        changes.push_back({c, s});
    }

    int a_score = 0, b_score = 0;
    int change_cnts = 0;
    string prev_winner = "AB", winner = "AB";

    for (int ch_idx = 0; ch_idx < N; ch_idx++) 
    {
        char player = changes[ch_idx].first;
        int ch_score = changes[ch_idx].second;

        if (player == 'A') 
        {
            a_score += ch_score;
        } 
        else if (player == 'B') 
        {
            b_score += ch_score;
        }

        if (ch_idx != 0) 
        {
            if (a_score > b_score) 
            {
                winner = "A";
            } 
            else if (a_score < b_score) 
            {
                winner = "B";
            } 
            else 
            {
                winner = "AB";
            }
        } 
        else 
        {
            if (a_score < b_score) 
            {
                winner = "B";
            } 
            else if (a_score > b_score) 
            {
                winner = "A";
            }
        }

        if (prev_winner != winner) 
        {
            change_cnts++;
            prev_winner = winner;
            winner = "";
        }
    }

    cout << change_cnts << '\n';
    return 0;
}
