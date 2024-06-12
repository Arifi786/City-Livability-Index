import numpy as np
import matplotlib.pyplot as plt

# Original data
data = np.array([[11060148, 84.53, 36.01, 83.00, 5.00, 6.00, 13759.00, 91.30],
                 [10009781, 84.06, 12.04, 18.00, 6.00, 6.00, 11847.00, 90.47],
                 [9621551, 87.67, 47.18, 40.00, 10.00, 10.00, 30000.00, 16.82],
                 [9429408, 86.15, 30.37, 10.00, 10.00, 10.00, 30000.00, 98.39],
                 [9356962, 89.91, 8.29, 10.00, 11.00, 10.00, 30000.00, 62.53],
                 [8161961, 77.51, 18.17, 73.00, 5.00, 4.00, 10638.00, 53.79],
                 [7717563, 76.21, 11.92, 41.00, 8.00, 7.00, 27838.00, 80.95],
                 [7214225, 85.31, 24.03, 38.00, 9.00, 9.00, 20000.00, 76.12],
                 [7103807, 66.59, 21.09, 16.00, 5.00, 5.00, 10342.00, 3.20],
                 [6626178, 75.51, 26.19, 62.00, 9.00, 9.00, 20000.00, 89.31],
                 [6107187, 82.31, 22.30, 19.00, 9.00, 9.00, 18000.00, 99.37]])

# Normalize data
normalized_data = data / np.linalg.norm(data, axis=0)

# Features
features = ['Population', 'Health', 'Education', 'Transportation', 'Crime', 'Pollution', 'Salary', 'Living Cost']

# Create scatter plots for pairs of features
fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # 2 rows, 2 columns

plot_counter = 0
for i in range(len(features)):
  for j in range(i+1, len(features)):
    if plot_counter >= 4:  # After 4 plots, move to the next figure
      fig, axes = plt.subplots(2, 2, figsize=(12, 12))
      plot_counter = 0
    axes[plot_counter // 2, plot_counter % 2].scatter(normalized_data[:, i], normalized_data[:, j], color='blue')
    axes[plot_counter // 2, plot_counter % 2].set_xlabel(features[i] + ' (Normalized)')
    axes[plot_counter // 2, plot_counter % 2].set_ylabel(features[j] + ' (Normalized)')
    axes[plot_counter // 2, plot_counter % 2].set_title(features[i] + ' vs ' + features[j])
    plot_counter += 1

plt.tight_layout()
plt.show()