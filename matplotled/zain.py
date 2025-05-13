import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-notebook')
dev_x =[25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,52752,59920,68272,
         77820,88564,100512,113664,128020]

plt.title("salary for each age")
plt.xlabel("age")
plt.ylabel("salary")
plt.plot(dev_x, dev_y, color="r", linestyle="--", marker="o", linewidth=2, label='salary for each age')
plt.legend()
plt.grid()
plt.show()




