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
        to_del = set(random.sample(range(len(c_contents)), n_draw))
        result = [item for index, item in enumerate(c_contents) if index in to_del]
        self.contents = [
            item for index, item in enumerate(c_contents) if not index in to_del
        ]
        return sorted(result)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = num_experiments
    m = 0
    while i > 0:
        c_hat = copy.copy(hat)
        # draw balls
        balls_drawn = Counter(c_hat.draw(num_balls_drawn))
        enough = {
            k: expected_balls[k]
            for k in expected_balls
            if k in balls_drawn and expected_balls[k] <= balls_drawn[k]
        }
        # check if is correct:
        if len(enough) == len(expected_balls):
            m += 1
        i -= 1
    return m / num_experiments
