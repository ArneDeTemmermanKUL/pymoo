import numpy as np


def max_alpha(point, direction, xl, xu):
    bounds = []

    if xl is not None:
        bounds.append(xl)

    if xu is not None:
        bounds.append(xu)

    if len(bounds) == 0:
        return np.inf

    # the bounds in one array
    bounds = np.column_stack(bounds)

    # if the direction is too small we can not divide by 0 - nan will make it being ignored
    dir = direction.copy()
    dir[dir == 0] = np.nan

    # calculate the max factor to be not out of bounds
    val = (bounds - point[:, None]) / dir[:, None]

    # remove nan and less than 0 values
    val = val[np.logical_not(np.isnan(val))]
    val = val[val >= 0]

    # if no value there - no bound exist
    if len(val) == 0:
        return np.inf
    # otherwise return the minimum of values considered
    else:
        return val.min()
