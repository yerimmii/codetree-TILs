#include <iostream>
using namespace std;

int main() {
    int age1, age2;
    char sex1, sex2;
    int ans;

    cin >> age1 >> sex1 >> age2 >> sex2;

    if ((sex1 == 'M' && age1 >= 19) || (sex2 == 'M' && age2 >= 19)) {
        ans = 1;
    } else {
        ans = 0;
    }

    cout << ans;

    return 0;
}