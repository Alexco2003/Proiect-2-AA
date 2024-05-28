#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    Point(long long x, long long y) : x(x), y(y) {}
};

struct Operation {
    int type;
    long long y, a, b;
    Operation(int type, long long y, long long a, long long b) : type(type), y(y), a(a), b(b) {}
    bool operator<(const Operation& other) const {
        return y < other.y;
    }
};

const long long maxX = 1000005;
const long long SIZE = 2 * maxX;

class FenwickTree {
public:
    FenwickTree(long long size) : size(size), tree(size + 1, 0) {}

    void update(long long idx, long long val) {
        while (idx <= size) {
            tree[idx] += val;
            idx += idx & -idx;
        }
    }

    long long query(long long idx) {
        long long sum = 0;
        while (idx > 0) {
            sum += tree[idx];
            idx -= idx & -idx;
        }
        return sum;
    }

private:
    long long size;
    vector<long long> tree;
};

int main() {
    int n;
    cin >> n;
    vector<pair<Point, Point>> segments;

    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        segments.emplace_back(Point(x1, y1), Point(x2, y2));
    }

    vector<Operation> ops;
    for (const auto& seg : segments) {
        if (seg.first.x == seg.second.x) {
            ops.emplace_back(2, seg.first.y, seg.first.x + maxX, -1);
            ops.emplace_back(3, seg.second.y, seg.first.x + maxX, -1);
        } else {
            ops.emplace_back(1, seg.first.y, seg.first.x + maxX, seg.second.x + maxX);
        }
    }

    sort(ops.begin(), ops.end());

    FenwickTree fenwick_tree(SIZE);
    long long cnt = 0;

    for (const auto& op : ops) {
        if (op.type == 1) {
            cnt += fenwick_tree.query(op.b) - fenwick_tree.query(op.a - 1);
        } else if (op.type == 2) {
            fenwick_tree.update(op.a, 1);
        } else if (op.type == 3) {
            fenwick_tree.update(op.a, -1);
        }
    }

    cout << cnt << endl;

    return 0;
}
