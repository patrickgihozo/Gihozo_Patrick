import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig,ax = plt.subplots()

plt.bar(x, y)
plt.title("Basic line graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()