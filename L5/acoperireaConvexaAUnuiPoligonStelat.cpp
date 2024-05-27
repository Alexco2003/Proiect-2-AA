// Jarvis’ march / Jarvis’ wrap [1973]

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

using namespace std;

struct Punct {
    int x, y;
    bool operator<(const Punct& p) const {
        return (x < p.x) || (x == p.x && y < p.y);
    }
    bool operator==(const Punct& p) const {
        return x == p.x && y == p.y;
    }
};

int determinant(int xp, int yp, int xq, int yq, int xr, int yr) {
    return xq * yr + xr * yp + xp * yq - xq * yp - xr * yq - xp * yr;
}

int distantaLaPatrat(int x1, int y1, int x2, int y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

int main() {
    int n;
    cin >> n;
    vector<Punct> P(n);
    for (int i = 0; i < n; ++i) {
        cin >> P[i].x >> P[i].y;
    }

    Punct A1 = *min_element(P.begin(), P.end());
    int k = 1;
    bool valid = true;
    vector<Punct> answer;
    answer.push_back(A1);
    Punct S = A1;

    while (valid) {
        for (const auto& Pi : P) {
            if (!(Pi == answer[k - 1])) {
                S = Pi;
                break;
            }
        }
        for (int i = 0; i < n; i++) {
            int xp = answer[k - 1].x;
            int yp = answer[k - 1].y;
            int xq = S.x;
            int yq = S.y;
            int xr = P[i].x;
            int yr = P[i].y;
            int det = determinant(xp, yp, xq, yq, xr, yr);
            if (det < 0 || (det == 0 && distantaLaPatrat(xp, yp, xr, yr) > distantaLaPatrat(xp, yp, xq, yq))) {
                S = P[i];
            }
        }
        if (!(S == A1)) {
            k++;
            answer.push_back(S);
        } else {
            valid = false;
        }
    }

    cout << k << endl;
    for (const auto& Pi : answer) {
        cout << Pi.x << " " << Pi.y << endl;
    }

    return 0;
}
