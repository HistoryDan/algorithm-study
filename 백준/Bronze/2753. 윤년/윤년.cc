#include <iostream> 
using namespace std;

int main(){
    int year;
    int answer;
    cin >> year;
    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0){
        answer = 1;
    }
    else
        answer = 0;
    cout << answer << endl;
}