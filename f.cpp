#include <iostream>
#include <vector>

#define endl "\n"

using namespace std;

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main()
{
    fastIO();

    // Reading dimensions and elements of the first matrix
    int ra, ca;
    cin >> ra >> ca;
    vector<vector<int>> arrA(ra, vector<int>(ca));
    for (int i = 0; i < ra; i++)
    {
        for (int j = 0; j < ca; j++)
        {
            cin >> arrA[i][j];
        }
    }

    // Reading dimensions and elements of the second matrix
    int rb, cb;
    cin >> rb >> cb;
    vector<vector<int>> arrB(rb, vector<int>(cb));
    for (int i = 0; i < rb; i++)
    {
        for (int j = 0; j < cb; j++)
        {
            cin >> arrB[i][j];
        }
    }

    vector<vector<int>> result(ra, vector<int>(cb, 0));

    for (int i = 0; i < ra; i++)
    {
        for (int j = 0; j < cb; j++)
        {
            long long res = 0;
            for (int k = 0; k < ca; k++)
            {
                res += arrA[i][k] * arrB[k][j];
            }
            result[i][j] = res;
        }
    }

    for (int i = 0; i < ra; i++)
    {
        for (int j = 0; j < cb; j++)
        {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}