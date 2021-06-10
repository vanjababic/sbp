

import numpy as np
import matplotlib.pyplot as plt
data = [
    [24.2, 24, 29.4, 29, 31.2, 63.4, 32.7, 24.9, 28.4, 35.6],
    [1.72, 1.66, 0.957, 1.19, 0.933, 2.9, 3.42, 1.64, 1.63, 1.54]
    ]

X = np.arange(10)
fig, ax = plt.subplots()
v1_bar = ax.bar(X       , data[0], color = 'r', width = 0.2)
v2_bar = ax.bar(X + 0.2, data[1], color = 'g', width = 0.2)

ax.set_ylabel('Seconds')
ax.set_xlabel('Questions')
ax.set_xticks(X + 0.50 / 2)
ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))

ax.legend((v1_bar[0], v2_bar[0]), ('v1', 'v2'))
plt.show()
