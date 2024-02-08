#!/usr/bin/env python3
class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")

    def pmf(self, k):
        k = int(k)
        if k < 0:
            return 0
        else:
            pmf_value = self._poisson_formula(k)
            return pmf_value

    def _poisson_formula(self, k):
        if k == 0:
            return self._poisson_0()
        else:
            return self._poisson_recursive(k, self.lambtha)

    def _poisson_recursive(self, k, lambtha):
        if k == 1:
            return lambtha
        else:
            return (lambtha / k) * self._poisson_recursive(k - 1, lambtha)

    def _poisson_0(self):
        return math.exp(-self.lambtha)


# Test cases
try:
    p = Poisson(data=[1, 2, 3])
    print(p.pmf(2))  # Should print the PMF value for k = 2
    print(p.pmf(1.5))  # Should print the PMF value for k = 1
    print(p.pmf(5))  # Should print the PMF value for k = 5
    print(p.pmf(-1))  # Should print 0 as k is out of range
except Exception as e:
    print(e)
