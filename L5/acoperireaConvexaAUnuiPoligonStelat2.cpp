// Graham’s scan, varianta Andrew (algoritm)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Punct {
    int x, y;
    bool operator<(const Punct& p) const {
        return (x < p.x) || (x == p.x && y < p.y);
    }
};

long long determinant(int xp, int yp, int xq, int yq, int xr, int yr) {
    return static_cast<long long>(xq) * yr + static_cast<long long>(xr) * yp + static_cast<long long>(xp) * yq
           - static_cast<long long>(xq) * yp - static_cast<long long>(xr) * yq - static_cast<long long>(xp) * yr;
}

int distantaLaPatrat(int x1, int y1, int x2, int y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

int main() {
    int n;
    cin >> n;
    vector<Punct> P(n);
    for (int i = 0; i < n; i++) {
        cin >> P[i].x >> P[i].y;
    }

    sort(P.begin(), P.end());

    vector<Punct> Li;
    Li.push_back(P[0]);
    Li.push_back(P[1]);

    for (int i = 2; i < n; i++) {
        Li.push_back(P[i]);
        while (Li.size() > 2 && determinant(Li[Li.size() - 3].x, Li[Li.size() - 3].y, Li[Li.size() - 2].x, Li[Li.size() - 2].y, Li[Li.size() - 1].x, Li[Li.size() - 1].y) <= 0) {
            Li.erase(Li.end() - 2);
        }
    }

    vector<Punct> Ls;
    Ls.push_back(P[n - 1]);
    Ls.push_back(P[n - 2]);

    for (int i = n - 3; i >= 0; i--) {
        Ls.push_back(P[i]);
        while (Ls.size() > 2 && determinant(Ls[Ls.size() - 3].x, Ls[Ls.size() - 3].y, Ls[Ls.size() - 2].x, Ls[Ls.size() - 2].y, Ls[Ls.size() - 1].x, Ls[Ls.size() - 1].y) <= 0) {
            Ls.erase(Ls.end() - 2);
        }
    }

    vector<Punct> L = Li;
    for (vector<Punct>::size_type i = 1; i < Ls.size() - 1; ++i) {
        L.push_back(Ls[i]);
    }

    cout << L.size() << endl;
    for (const auto& Punct : L) {
        cout << Punct.x << " " << Punct.y << endl;
    }

    return 0;
}
