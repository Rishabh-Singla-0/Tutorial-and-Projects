#include<bits/stdc++.h>
using namespace std;

int main() {

    int marks = 0;

    cout << "Enter Your Marks: ";
    cin >> marks;

    if (marks < 0) {
        cout << "Invalid Marks";
    } else if (marks < 33) {
        cout << "Fail";
    } else if (marks < 40) {
        cout << "F-Rank";
    } else if (marks < 50) {
        cout << "E-Rank";
    } else if (marks < 60) {
        cout << "D-Rank";
    } else if (marks < 70) {
        cout << "C-Rank";
    } else if (marks < 80) {
        cout << "B-Rank";
    } else if (marks < 90) {
        cout << "A-Rank";
    } else if (marks <= 100) {
        cout << "Out-Standing";
    } else {
        cout << "Invalid Marks";
    }

    return 0;
}