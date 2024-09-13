#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    int ans;

    cin >> a >> b >> c;

    if (b > a && c > b) { ans = 1; }
    else { ans = 0; }

    cout << ans;

    return 0;
}