#include <iostream>
#include <vector>
#include <limits>
#include <tuple>
#include <cmath>
#include <iomanip>

using namespace std;

class Point {
public:
    double x, y;
    Point(double x, double y) : x(x), y(y) {}
};

class Equation {
public:
    double a, b, c;
    Equation(double a, double b, double c) : a(a), b(b), c(c) {}
};

tuple<double, double, double, double> find_interesting_rectangle(const vector<Equation>& equations, const Point& point) {
    double min_x = -numeric_limits<double>::infinity();
    double max_x = numeric_limits<double>::infinity();
    double min_y = -numeric_limits<double>::infinity();
    double max_y = numeric_limits<double>::infinity();

    for (const auto& eq : equations) {
        if (eq.a != 0 && eq.b == 0) {
            double x_value = -eq.c / eq.a;
            if (eq.a > 0) {
                if (point.x < x_value) {
                    max_x = min(max_x, x_value);
                }
            } else {
                if (point.x > x_value) {
                    min_x = max(min_x, x_value);
                }
            }
        } else if (eq.a == 0 && eq.b != 0) {
            double y_value = -eq.c / eq.b;
            if (eq.b > 0) {
                if (point.y < y_value) {
                    max_y = min(max_y, y_value);
                }
            } else {
                if (point.y > y_value) {
                    min_y = max(min_y, y_value);
                }
            }
        }
    }

    if (min_x >= max_x || min_y >= max_y) {
        return {nan(""), nan(""), nan(""), nan("")};
    }
    return {min_x, max_x, min_y, max_y};
}

bool is_point_inside_rectangle(const Point& point, const tuple<double, double, double, double>& rect) {
    double min_x, max_x, min_y, max_y;
    tie(min_x, max_x, min_y, max_y) = rect;
    return min_x < point.x && point.x < max_x && min_y < point.y && point.y < max_y;
}

void process_points(const vector<Equation>& equations, const vector<Point>& points) {
    for (const auto& point : points) {
        double min_area = numeric_limits<double>::infinity();
        bool found = false;

        for (size_t r = 1; r <= equations.size(); ++r) {
            for (size_t i = 0; i < (1 << equations.size()); ++i) {
                vector<Equation> subset;
                for (size_t j = 0; j < equations.size(); ++j) {
                    if (i & (1 << j)) {
                        subset.push_back(equations[j]);
                    }
                }
                if (subset.size() == r) {
                    auto rect = find_interesting_rectangle(subset, point);
                    if (!isnan(get<0>(rect)) && is_point_inside_rectangle(point, rect)) {
                        double area = (get<1>(rect) - get<0>(rect)) * (get<3>(rect) - get<2>(rect));
                        if (area < min_area) {
                            min_area = area;
                            found = true;
                        }
                    }
                }
            }
        }

        if (found) {
            cout << "YES\n";
            cout << fixed << setprecision(6) << min_area << "\n";
        } else {
            cout << "NO\n";
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<Equation> equations;

    for (int i = 0; i < n; ++i) {
        double ai, bi, ci;
        cin >> ai >> bi >> ci;
        equations.emplace_back(ai, bi, ci);
    }

    int m;
    cin >> m;
    vector<Point> points;

    for (int i = 0; i < m; ++i) {
        double xi, yi;
        cin >> xi >> yi;
        points.emplace_back(xi, yi);
    }

    process_points(equations, points);
    return 0;
}
