import matplotlib.pyplot as plt

# Data (you can adjust later)
time = [0, 6, 48, 144]  # hours (0h, 6h, 2d, 6d)

low_glycerine = [12, 9, 5, 3]
high_glycerine = [18, 14, 10, 7]

plt.figure()

plt.plot(time, low_glycerine, marker='o', label='Low glycerine (2g)')
plt.plot(time, high_glycerine, marker='o', label='High glycerine (6g)')

plt.xlabel("Immersion time (hours)")
plt.ylabel("Deflection (mm)")
plt.title("Evolution of bioplastic rigidity under seawater exposure")

plt.legend()

plt.savefig("rigidity_evolution.png")
plt.show()
