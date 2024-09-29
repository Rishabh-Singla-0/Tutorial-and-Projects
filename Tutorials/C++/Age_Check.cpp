#include<bits/stdc++.h>
using namespace std;

int main() {

    int age = 0;

    cout << "Enter Your Age: ";
    cin >> age;

    if (age < 18 && age >= 0) {
        cout << "Under Age";
    } else if (age >= 18) {
        cout << "Legal Age";
    } else {
        cout << "invalid Age";
    }

    return 0;
}