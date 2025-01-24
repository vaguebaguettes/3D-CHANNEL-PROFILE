import math

def calculate_T(x, y, z, To, Po, fact, k, U, alpha, to, tau, series):
    # Calculate r
    r = math.sqrt(x**2 + y**2 + z**2)

    # Compute the second phase
    phase2 = (Po / (fact * math.pi * k * r)) * math.exp(U * (x - r) / (2 * alpha))

    # Compute the third phase
    phase3 = (Po * to / ((math.pi**2) * (fact / 2) * k * r * tau)) * series

    # Calculate the overall T
    T = To + phase2 + phase3

    return T

