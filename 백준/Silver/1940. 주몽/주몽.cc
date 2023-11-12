#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;  // 첫 번째 라인은 무시합니다.
    
    int m;
    std::cin >> m;  // 두 번째 라인에서 m을 읽습니다.

    std::vector<int> ingreds(n);
    
    for (int i = 0; i < n; ++i) {
        std::cin >> ingreds[i];
    }

    int cnt = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (ingreds[i] + ingreds[j] == m) {
                cnt++;
            }
        }
    }

    std::cout << cnt << std::endl;

    return 0;
}
