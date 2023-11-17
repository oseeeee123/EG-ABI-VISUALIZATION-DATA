import matplotlib.pyplot as plt

# Year and corresponding temperature data for the hottest and coldest temperatures
years = [1992, 1997, 2002, 2007, 2012, 2017, 2020, 2022]
hottest_temperatures = [-1.0, -2.4, -2.4, -2.8, -0.5, -2.6, -0.3, -2.0]
coldest_temperatures = [-18.5, -21.1, -18.1, -19.0, -21.2, -20.1, -21.9, -20.0]

# Plotting the data for hottest temperatures
plt.plot(years, hottest_temperatures, marker='o', linestyle='-', color='red', label='Hottest Temperatures')

# Plotting the data for coldest temperatures
plt.plot(years, coldest_temperatures, marker='o', linestyle='-', color='blue', label='Coldest Temperatures')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Hottest and Coldest Temperatures Recorded in Antarctica (1992-2022)')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
