import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([5, 6, 7], [0.049, 0.125, 0.127], label="Uma falha")
ax.plot([5, 6, 7], [0.904, 2.707, 3.161], label="Duas falhas")
ax.plot([5, 6, 7], [10.463, 38.062, 46.613], label="Três falhas")

plt.ylabel('Tempo em segundos')
plt.xlabel("Número de portas")
plt.xticks([5, 6, 7])
ax.legend(loc="center right", shadow=True, fontsize='large')
plt.show()