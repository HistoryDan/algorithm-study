#include <iostream>
#include <map> 
using namespace std;
int main(){
    int rep, cowNum, roadNum;
    int answer = 0;
    map<int, int> cowCount;
    cin >> rep;
    for (int i = 0; i < rep; i++){
        cin >> cowNum >> roadNum;
        if (cowCount.find(cowNum) != cowCount.end()){
            int roadTemp = cowCount[cowNum];
            if (roadTemp != roadNum) answer++;
        }
        cowCount[cowNum] = roadNum;
    }
    cout << answer;
    return 0;
}