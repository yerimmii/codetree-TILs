#include <iostream>
using namespace std;

int main() {
    int a;
    int ans;

    cin >> a;

    if (a % 3 == 0 || a % 5 == 0) { ans = 1; }
    else { ans = 0; }

    cout << ans;

    return 0;
}