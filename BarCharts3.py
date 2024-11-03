import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

countries = ('Brunei', 'cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
cases = (135430, 135714, 6018048, 181967, 4219395, 611674, 3678968, 1101438, 3684755, 9716282)

df = pd.DataFrame ({
    'Country':countries,
    'Case': cases,
})
df.sort_values(by='Case', inplace=True)

x_coords = np.arange(len(df))
plt.bar(x_coords, df['Case'], tick_label = df['Country'])
plt.xticks(rotation=90)
plt.ylabel('Total Covid Cases')
plt.title('Covid Cases in ASEAN')
plt.show()