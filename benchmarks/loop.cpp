#include <iostream>
#include <vector>

int main() {
    const int N = 10'000'000;
    std::vector<int> a(N, 1);

    long long sum = 0;
    for (int i = 0; i < N; i++) {
        sum += a[i];
    }

    std::cout << sum << "\n";
}
