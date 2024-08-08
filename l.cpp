#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

#define endl "\n"

int C(int n, int r)
{
    r = min(n - r, r);
    long long numerator = 1;
    for (int i = 0; i < r; i++)
    {
        numerator *= (n - i);
    }

    long long  denominator = 1;
    for (int i = 2; i <= r; i++)
    {
        denominator *= i;
    }

    return numerator / denominator;
}

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main()
{
    fastIO();
    int n;
    cin >> n;
    
    deque<deque<int>> grid(n, deque<int>(n));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            grid[i][j] = C(i, j);
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            if (i>=j){
                cout<<grid[i][j]<<" ";
            }
        }
        cout<<endl;
    }

    

    return 0;
}
