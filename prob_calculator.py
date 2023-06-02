import copy
import random
from collections import Counter

# Consider using the modules imported above.


class Hat:
    def __init__(self, **colors):
        self.colors = colors
        self.contents = list()

        for key, value in colors.items():
            p = [key] * value
            self.contents.extend(p)

    def draw(self, n_draw):
        # return a list and remove random elements from contents
        c_contents = copy.copy(self.contents)
        if n_draw > len(self.contents):
            return c_contents
        # create a set of index to delete
        to_del = set(random.sample(range(len(c_contents)), n_draw))
        # idx stands for index
        result = [item for idx, item in enumerate(c_contents) if idx in to_del]
        self.contents = [
            item for idx, item in enumerate(c_contents) if idx not in to_del
        ]
        return sorted(result)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = num_experiments
    m = 0
    while i > 0:
        c_hat = copy.copy(hat)
        # draw balls and count the result
        balls_drawn = Counter(c_hat.draw(num_balls_drawn))
        # check if there are enough balls in the current draw
        enough = {
            key: value
            for key, value in expected_balls.items()
            if key in balls_drawn and value <= balls_drawn[key]
        }
        # check if is correct:
        if len(enough) == len(expected_balls):
            m += 1
        i -= 1
    probability = m / num_experiments
    return probability
