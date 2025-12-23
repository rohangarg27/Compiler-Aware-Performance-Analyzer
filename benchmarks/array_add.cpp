#include <vector>
#include <iostream>

int main() {
    const int N = 10'000'000;
    std::vector<float> a(N, 1.0f), b(N, 2.0f), c(N);

    for (int i = 0; i < N; i++) {
        c[i] = a[i] + b[i];
    }

    std::cout << c[0] << "\n";
    return 0;
}


