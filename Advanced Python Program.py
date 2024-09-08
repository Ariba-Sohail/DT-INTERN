#importing needed libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import statistics
import sympy
import matplotlib.pyplot as plt

# Ask the user for their name, age, and favorite number
name = input("What is your name?:")
age = int(input("How old are you?:"))
favorite_number = int(input("What is your favorite number?:"))

# Generate a random array of 10 numbers using NumPy and Calculate the mean, median, and standard deviation of the random array
random_array = np.random.rand(10)

mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

print(f"Mean: {mean:.2f}, Median: {median:.2f}, Standard Deviation: {std_dev:.2f}")

# Create a simple linear regression model using scikit-learn
X = np.array([[age], [favorite_number]])
y = np.array([age, favorite_number])
model = LinearRegression()
model.fit(X, y)

# Calculate the correlation coefficient between the user's age and favorite number
correlation_coefficient = statistics.correlation([age, favorite_number], [age, favorite_number])
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")

# Check the user's age using conditional statements
if age < 18:
    print("You're a Minor!")
elif age == 21:
    print("You're 21, Congratulations!")
else:
    print("You're an Adult!")

# Use a loop to generate a list of prime numbers up to 100 using 'sympy' library
prime_numbers = []
for i in range(2, 101):
    if sympy.isprime(i):
        prime_numbers.append(i)
print("Prime numbers up to 100:", prime_numbers)

# Create a simple plot of the user's age vs. favorite number using matplotlib
plt.scatter([age], [favorite_number])
plt.xlabel("Age")
plt.ylabel("Favorite Number")
plt.title("Age vs. Favorite Number")
plt.show()
