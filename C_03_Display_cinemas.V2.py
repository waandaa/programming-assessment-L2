import pandas

# lists to hold pass details
all_cinemas = [" Event Tauranga Crossing", "Event Tauranga Central", "Luxe Tauranga Central", "Luxe Papamoa", "United Bayfair"]

mini_cinema_dict = {
    'Cinemas': all_cinemas
}

# Importing pandas package
import pandas as pd

# Importing numpy package
import numpy as np

# Creating a dictionary
d = {
    'Cinemas': all_cinemas
}

# Creating DataFrame
df = pd.DataFrame(d)

# Rearranging index
df.index = np.arange(1, len(df) + 1)

# Display modified DataFrame
print("\n",df)

print()

cinema_selection = input("Type in your cinema selection ")

print(f"You selected {cinema_selection}")
