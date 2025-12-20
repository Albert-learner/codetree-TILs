#include <iostream>
#include <vector>
using namespace std;

vector<int> build_lps(const vector<int>& pat) 
{
    int m = (int)pat.size();
    vector<int> lps(m, 0);
    for (int i = 1, len = 0; i < m; ) 
    {
        if (pat[i] == pat[len]) 
        {
            lps[i++] = ++len;
        } 
        else if (len > 0) 
        {
            len = lps[len - 1];
        } 
        else 
        {
            lps[i++] = 0;
        }
    }
    return lps;
}

bool kmp_contains(const vector<int>& text, const vector<int>& pat) 
{
    int n = (int)text.size();
    int m = (int)pat.size();
    if (m == 0) return true;

    vector<int> lps = build_lps(pat);

    for (int i = 0, j = 0; i < n; ) 
    {
        if (text[i] == pat[j]) 
        {
            i++; j++;
            if (j == m) return true; // 매칭 완료
        } 
        else if (j > 0) 
        {
            j = lps[j - 1];
        } 
        else 
        {
            i++;
        }
    }
    return false;
}

int main() 
{
    int n1, n2;
    cin >> n1 >> n2;

    vector<int> a_seq(n1), b_seq(n2);
    for (int i = 0; i < n1; i++) cin >> a_seq[i];
    for (int i = 0; i < n2; i++) cin >> b_seq[i];

    cout << (kmp_contains(a_seq, b_seq) ? "Yes" : "No");
    return 0;
}
