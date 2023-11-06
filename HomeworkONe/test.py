import numpy as np

# Create a 200x200 matrix with random values (replace this with your data)
matrix = np.random.rand(10, 10)

# Calculate the total number of entries in the matrix
total_entries = 10 * 10

# Calculate the number of entries to choose (10% of the total entries)
entries_to_choose = int(0.10 * total_entries)

# Generate a random mask with True values for the selected entries
random_mask = np.zeros((10, 10), dtype=bool)
random_indices = np.random.choice(total_entries, entries_to_choose, replace=False)
random_mask.flat[random_indices] = True

# Apply the mask to select the entries
selected_entries = matrix[random_mask]

print(selected_entries)
