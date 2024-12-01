import itertools


class Range:
    def __init__(self, start, stop, step=1):
        self._start = start
        self._stop = stop
        self._step = step

    def _generate_range(self):
        current = self._start
        while (self._step > 0 and current < self._stop) or (self._step < 0 and current > self._stop):
            yield current
            current += self._step

    @property
    def min(self):
        return self._start if self._step > 0 else min(self._start, self._stop - 1, key=lambda x: x + (x % self._step))

    @min.setter
    def min(self, value):
        self._start = value

    @property
    def max(self):
        return max(self._start, self._stop - 1, key=lambda x: x + (x % self._step)) if self._step > 0 else self._start

    @max.setter
    def max(self, value):
        self._start = value

    @property
    def empty(self):
        if self._start is None or self._stop is None:
            return True
        return (self._step > 0 and self._start >= self._stop) or (self._step < 0 and self._start <= self._stop)

    def intersection(self, other):
        if self.empty or other.empty or self._step != other._step:
            return Range(0, 0, 1)

        new_start = max(self._start, other._start)
        new_stop = min(self._stop, other._stop)

        if new_start >= new_stop:
            return Range(0, 0, 1)

        return Range(new_start, new_stop, self._step)

    def __iter__(self):
        return self._generate_range()


def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                          list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page
