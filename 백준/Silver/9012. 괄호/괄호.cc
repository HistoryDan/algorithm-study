#include <iostream>
#include <string>
#include <limits>
using namespace std;

#define MAX_SIZE 50

struct Stack {
    int top;
    char arr[MAX_SIZE];
};

void push(Stack *p, char value) {
    p->arr[++(p->top)] = value;
}

char pop(Stack *p) {
    if (p->top >= 0) {
        return p->arr[(p->top)--];
    } else {
        return '\0';
    }
}

int main() {
    int rep;
    cin >> rep;
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // 입력 버퍼 비우기

    for (int i = 0; i < rep; i++) {
        Stack stk;
        stk.top = -1;
        string line;
        cin >> line;

        bool balanced = true;

        for (int j = 0; j < line.length(); j++) {
            char t;
            if (line[j] == '(') {
                push(&stk, line[j]);
            } else if (line[j] == ')') {
                t = pop(&stk);
                if (t != '(') {
                    balanced = false;
                    break;
                }
            }
        }

        while (stk.top >= 0) {
            char t = pop(&stk);
            if (t == '(') {
                balanced = false;
                break;
            }
        }

        if (stk.top != -1 || !balanced) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
    return 0;
}
