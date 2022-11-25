import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [i**2 for i in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
# ax.plot(x_values, y_values, linewidth=3)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)
# ax.axis([0, 1100, 0, 1100000])

# To save fig automatically.
# plt.savefig("squares_plt.png", bbox_inches="tight")
plt.show()
