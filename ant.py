import numpy as np

X = [1, 0, -1, 0]
Y = [0, 1, 0, -1]


def FoundFood(x, y):
    return ((x - 2.5)/30.)**2 + ((y-2.5)/40.)**2 >= 1


def RandomTrajectory(x, y):
    """ Simulates an ant's movement till it reaches food.
    Args: 
      x, y - initial position of an ant.
    Returns: 
      Number of movements it took to reach food.
    """
    cnt = 0
    while not FoundFood(x, y):
        cnt += 1
        mv = np.random.randint(low=0, high=4)
        x += 10*X[mv]
        y += 10*Y[mv]
    return cnt


def CrudeMonteCarlo(x, y, max_num_simulations=1000000, eps=0.0001, verbose=False,):
    """ Computes an average time for an ant to reach food starting at x, y 
    by a crude Monte Carlo method.
    Args: 
      x, y - initial position of an ant.
      max_num_simulations.
      eps - desired precision for the result.
      verbose - prints debug information.
    Returns: 
      A tuple (e, cnt) where
        - e =  average number of movements it took to reach food.
        - cnt = number of simulations.
    """
    cnt = 0
    total = 0
    prev_estimate = -1
    for i in range(max_num_simulations):
        cnt += 1
        total += RandomTrajectory(x, y)
        if i % 10000 == 0:
            curr_estimate = total / cnt
            if verbose:
                print("Iter {0}: approximation = {1}".format(i, curr_estimate))
            if abs(prev_estimate - curr_estimate) < eps:
                break
            prev_estimate = curr_estimate
    return total / cnt, cnt


estimator, num_simulations = CrudeMonteCarlo(x=2.5, y=2.5, verbose=True)

print("Estimated food hitting time: {0} found in {1} simulations.".format(
    estimator, num_simulations))
