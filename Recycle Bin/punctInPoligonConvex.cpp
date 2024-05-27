#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Point {
    long long x, y;

    Point() : x(0), y(0) {}
    Point(long long _x, long long _y) : x(_x), y(_y) {}

    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }

    Point operator-(const Point& p) const {
        return Point(x - p.x, y - p.y);
    }

    long long cross(const Point& p) const {
        return x * p.y - y * p.x;
    }

    long long dot(const Point& p) const {
        return x * p.x + y * p.y;
    }

    long long cross_product(const Point& a, const Point& b) const {
        return (a - *this).cross(b - *this);
    }

    long long dot_product(const Point& a, const Point& b) const {
        return (a - *this).dot(b - *this);
    }

    long long sqr_len() const {
        return this->dot(*this);
    }
};

long long determinant(long long xp, long long yp, long long xq, long long yq, long long xr, long long yr) {
    return xq * yr + xr * yp + xp * yq - xq * yp - xr * yq - xp * yr;
}

bool lex_comp(const Point& p1, const Point& p2) {
    return (p1.x < p2.x) || (p1.x == p2.x && p1.y < p2.y);
}

int sgn(long long val) {
    return val > 0 ? 1 : (val == 0 ? 0 : -1);
}

bool point_in_triangle(const Point& a, const Point& b, const Point& c, const Point& p) {
    long long s1 = abs(a.cross_product(b, c));
    long long s2 = abs(p.cross_product(a, b)) + abs(p.cross_product(b, c)) + abs(p.cross_product(c, a));
    return s1 == s2;
}

bool point_on_segment(const Point& a, const Point& b, const Point& p) {
    if (determinant(a.x, a.y, b.x, b.y, p.x, p.y) == 0) {
        return min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
    }
    return false;
}

vector<Point> seq;
Point translation;
int n;

void prepare(vector<Point>& points) {
    n = points.size();
    int pos = 0;
    for (int i = 1; i < n; i++) {
        if (lex_comp(points[i], points[pos])) {
            pos = i;
        }
    }

    rotate(points.begin(), points.begin() + pos, points.end());

    n--;
    seq.resize(n);
    for (int i = 0; i < n; i++) {
        seq[i] = points[i + 1] - points[0];
    }
    translation = points[0];
}

string point_in_convex_polygon(Point point) {
    point = point - translation;

    if (point_on_segment(Point(0, 0), seq[0], point)) {
        return "BOUNDARY";
    }
    if (point_on_segment(seq[n - 1], Point(0, 0), point)) {
        return "BOUNDARY";
    }

    if (sgn(determinant(0, 0, seq[0].x, seq[0].y, point.x, point.y)) != sgn(determinant(0, 0, seq[0].x, seq[0].y, seq[n - 1].x, seq[n - 1].y)) ||
        sgn(determinant(0, 0, seq[n - 1].x, seq[n - 1].y, point.x, point.y)) != sgn(determinant(0, 0, seq[n - 1].x, seq[n - 1].y, seq[0].x, seq[0].y))) {
        return "OUTSIDE";
    }

    if (determinant(0, 0, seq[0].x, seq[0].y, point.x, point.y) == 0) {
        return seq[0].sqr_len() >= point.sqr_len() ? "BOUNDARY" : "OUTSIDE";
    }

    int l = 0, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        if (determinant(0, 0, seq[mid].x, seq[mid].y, point.x, point.y) >= 0) {
            l = mid;
        } else {
            r = mid;
        }
    }

    if (point_on_segment(seq[l], seq[l + 1], point)) {
        return "BOUNDARY";
    }
    return point_in_triangle(seq[l], seq[l + 1], Point(0, 0), point) ? "INSIDE" : "OUTSIDE";
}

int main() {
    int n;
    cin >> n;
    vector<Point> P(n);
    for (int i = 0; i < n; i++) {
        cin >> P[i].x >> P[i].y;
    }

    int m;
    cin >> m;
    vector<Point> R(m);
    for (int i = 0; i < m; i++) {
        cin >> R[i].x >> R[i].y;
    }

    prepare(P);

    for (const auto& r : R) {
        cout << point_in_convex_polygon(r) << endl;
    }

    return 0;
}
