#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> vec1;
    for (int i = 0; i < 28; i++){
        int temp;
        cin >> temp;
        vec1.push_back(temp);
    }
    for (int i = 1; i <= 30; i++){
        bool flag = false; 
        for (auto val : vec1){
            if (i == val){
                flag = true;
                break;
            }
        }
        if (flag != true) cout << i << endl;
    }
}