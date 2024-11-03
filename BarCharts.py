import matplotlib.pyplot as plt
import numpy as np

countries = ('Brunei', 'cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
cases = (135430, 135714, 6018048, 181967, 4219395, 611674, 3678968, 1101438, 3684755, 9716282)
x_coords = np.arange(len(countries))
plt.bar(x_coords, cases, tick_label = countries)
plt.xticks(rotation=90)
plt.show()