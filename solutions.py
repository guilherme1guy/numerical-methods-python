"""Methods for solutions of equations"""

import math


def bisection(f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Bisection method
    Parameters:
        f: Function f(x)
        a: Lower limit
        b: Upper limit
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        root: Root value
        iter: Used iterations
        converged: Found the root
    """

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise Exception("The function does not change signal at \
              the ends of the given interval.")

    delta_x = math.fabs(b - a) / 2

    x = 0
    converged = False
    i = 0
    for i in range(0, iter_max + 1):
        x = (a + b) / 2
        fx = f(x)

        print("i: {:03d}\t x: {:+.4f}\t fx: {:+.4f}\t dx: {:+.4f}\n"
              .format(i, x, fx, delta_x), end="")

        if delta_x <= tol and math.fabs(fx) <= tol:
            converged = True
            break

        if fa * fx > 0:
            a = x
            fa = fx
        else:
            b = x

        delta_x = delta_x / 2
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]


def fake_position(f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Fake Position method
    Parameters:
        f: Function f(x)
        a: Lower limit
        b: Upper limit
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        root: Root value
        iter: Used iterations
        converged: Found the root
    """

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise Exception("The function does not change signal at \
              the ends of the given interval.")

    delta_x = math.fabs(b - a) / 2

    x = 0
    converged = False
    i = 0

    for i in range(0, iter_max + 1):
        x = ((a * fb) - (b * fa)) / (fb - fa)
        fx = f(x)

        print("i: {:03d}\t x: {:+.4f}\t fx: {:+.4f}\t dx: {:+.4f}\n"
              .format(i, x, fx, delta_x), end="")

        if delta_x <= tol and math.fabs(fx) <= tol:
            converged = True
            break

        if fa * fx > 0:
            a = x
            fa = fx
        else:
            b = x
            fb = fx

        delta_x = math.fabs(b - a) / 2
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]

def fixed_point(f, g, x0, tol, iter_max):
    """
    Calculates the root of an equation by Fixed Point method
    Parameters:
        f: Function f(x)
        g: Iteraction Function g(x)
        x0: Initial point
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        root: Root value
        iter: Used iterations
        converged: Found the root
    """

    x = x0
    fx = f(x)
    converged = False

    for i in range(0, iter_max):
        
        print("i: {:03d}\t x{:02d}: {:+.4f}\t fx{:d}: {:+.4f}\t\n"
            .format(i, i, x, i, fx), end="")
        
        if math.fabs(fx) < tol:
            converged = True
            break

        x = g(x)
        fx = f(x)


    root = x
    return [root, i, converged]

def newton(f, df, x0, tol, iter_max):
    """
    Calculates the root of an equation by Newton method
    Parameters:
        f: Function f(x)
        df: Derivative of function f(x)
        x0: Initial guess
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        root: Root value
        iter: Used iterations
        converged: Found the root
    """

    x = x0
    fx = f(x)
    dfx = df(x)

    converged = False
    print("iter: 0 x: {:.4f}\t dfx: {:.4f}\t fx: {:.4f}\n"
          .format(x, dfx, fx), end="")

    i = 0
    for i in range(1, iter_max + 1):
        delta_x = -fx / dfx
        x += delta_x
        fx = f(x)
        dfx = df(x)

        print("i:{:03d}\t x: {:.4f}\t dfx: {:.4f}\t fx: {:.4f}\t dx: {:.4f}\n"
              .format(i, x, dfx, fx, delta_x), end="")

        if math.fabs(delta_x) <= tol and math.fabs(fx) <= tol or dfx == 0:
            converged = True
            break
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]


def secant(f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Secant method
    Parameters:
        f: Function f(x)
        a: Lower limit
        b: Upper limit
        tol: Tolerance
        iter_max: Maximum number of iterations
    Returns:
        root: Root value
        iter: Used iterations
        converged: Found the root
    """

    fa = f(a)
    fb = f(b)

    if fb - fa == 0:
        raise Exception("f(b)-f(a) must be nonzero.")

    if b - a == 0:
        raise Exception("b-a must be nonzero.")

    if math.fabs(fa) < math.fabs(fb):
        a, b = b, a
        fa, fb = fb, fa

    x = b
    fx = fb

    converged = False
    i = 0
    for i in range(0, iter_max + 1):
        delta_x = -fx / (fb - fa) * (b - a)
        x += delta_x
        fx = f(x)

        print("i: {:03d}\t x: {:+.4f}\t fx: {:+.4f}\t dx: {:+.4f}\n"
              .format(i, x, fx, delta_x), end="")

        if math.fabs(delta_x) <= tol and math.fabs(fx) <= tol:
            converged = True
            break

        a, b = b, x
        fa, fb = fb, fx
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]
