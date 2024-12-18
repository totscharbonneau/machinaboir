import numpy as np
import math


def bezier_curve(t, control_points):
    n = len(control_points) - 1
    point = np.zeros(2)

    for j in range(n + 1):
        point += binomial_coeff(n, j) * (t ** j) * ((1 - t) ** (n - j)) * control_points[j]

    return point

def generate_bezier_curve(control_points, n_points=300):
    t_values = np.linspace(0, 1, n_points)
    bezier_points = np.array([bezier_curve(t, control_points) for t in t_values])
    return bezier_points

def get_y_for_x(x, bezier_points):
    # Find the closest x value in the Bezier points
    closest_index = np.argmin(np.abs(bezier_points[:, 0] - x))
    return bezier_points[closest_index, 1]


def binomial_coeff(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
