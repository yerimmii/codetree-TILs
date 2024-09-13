#include <iostream>
using namespace std;

int main() {
    int a;
    string ans;

    cin >> a;

    if (a < 10 || a > 20) { ans = "yes"; }
    else { ans = "no"; }

    cout << ans;

    return 0;
}