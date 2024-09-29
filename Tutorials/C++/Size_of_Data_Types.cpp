#include<bits/stdc++.h>
using namespace std;

int main() {

    string str;

    cin >> str;

    if (str == "Character") {
            return sizeof(char);
            
        } else if (str == "Integer") {
            return sizeof(int);
            
        } else if (str == "Long" ) {
            return sizeof(long);
            
        } else if (str == "Float") {
            return sizeof(float);
            
        } else if (str == "Double") {
            return sizeof(double);
            
        } else {
            return -1;
        }
    
    return 0;
}