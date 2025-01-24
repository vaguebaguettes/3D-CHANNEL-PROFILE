import math

def compute_series(x, y, z, n, Si, tau, t,  to, U, alpha):
    # Calculate r
    r = math.sqrt(x**2 + y**2 + z**2)

    # Calculate Sn
    Sn = math.sqrt((1 + math.sqrt(1 + (n**2) * (Si**2))) / 2)

    # Calculate the entire series expression
    series = (
        (1 / n) * math.sin(n * math.pi * tau / to) *
        math.exp(U * (x - r * Sn) / (2 * alpha)) *
        math.cos((2 * n * math.pi * t / to) - (U * r * n * Si) / (4 * alpha * Sn))
    )

    return series


