#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""AFN for time series from the Ikeda map.

E1 saturates near an embedding dimension of 4.  E2 != 1 at many values
of d.  Thus, this series is definitely deterministic.  Compare with
Fig. 2 of Cao (1997).
"""

from nolitsa import data, dimension
import matplotlib.pyplot as plt
import numpy as np

# Generate data.
x = data.ikeda()[:, 0]

# AFN algorithm.
dim = np.arange(1, 10 + 2)
E, Es = dimension.afn(x, tau=1, dim=dim, window=5)
E1, E2 = E[1:] / E[:-1], Es[1:] / Es[:-1]

plt.title(r'AFN for time series from the Ikeda map')
plt.xlabel(r'Embedding dimension $d$')
plt.ylabel(r'$E_1(d)$ and $E_2(d)$')
plt.plot(dim[:-1], E1, 'bo-', label=r'$E_1(d)$')
plt.plot(dim[:-1], E2, 'go-', label=r'$E_2(d)$')
plt.legend()

plt.show()
