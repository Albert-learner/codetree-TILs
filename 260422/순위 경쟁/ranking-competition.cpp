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

    int a_score = 0, b_score = 0, c_score = 0;
    int change_cnts = 0;
    string prev_winner = "ABC", winner = "ABC";

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
        else if (player == 'C') 
        {
            c_score += ch_score;
        }

        if (ch_idx != 0) 
        {
            if (a_score > b_score && a_score > c_score) 
            {
                winner = "A";
            } 
            else if (a_score < b_score && c_score < b_score) 
            {
                winner = "B";
            } 
            else if (a_score < c_score && b_score < c_score) 
            {
                winner = "C";
            } 
            else if (a_score < b_score || a_score < c_score) 
            {
                winner = "BC";
            } 
            else if (b_score < c_score || b_score < a_score) 
            {
                winner = "CA";
            } 
            else if (c_score < a_score || c_score < b_score) 
            {
                winner = "AB";
            } 
            else 
            {
                winner = "ABC";
            }
        } 
        else 
        {
            if (a_score < b_score && c_score < b_score) 
            {
                winner = "B";
            } 
            else if (a_score > b_score && a_score > c_score) 
            {
                winner = "A";
            } 
            else if (a_score < c_score && b_score < c_score) 
            {
                winner = "C";
            } 
            else if (a_score < b_score || a_score < c_score) 
            {
                winner = "BC";
            } 
            else if (b_score < c_score || b_score < a_score) 
            {
                winner = "CA";
            } 
            else if (c_score < a_score || c_score < b_score) 
            {
                winner = "AB";
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