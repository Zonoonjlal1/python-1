import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-notebook')
dev_x =[25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,52752,59920,68272,
         77820,88564,100512,113664,128020]
Doc_dev_x =[25,26,27,28,29,30,31,32,33,34,35]
Doc_dev_y = [38306,58000,61752,72752,99920,10827,
         11082,121856,138051,140366,152802]

plt.title("salary for each age")
plt.xlabel("age")
plt.ylabel("salary")
#plt.bar(dev_x,dev_y , color="r", label = 'salary for each age' )
plt.plot(Doc_dev_x,Doc_dev_y , color="blue",linestyle='--', marker="*",linewidth=2,label = 'salary for Docter age')
plt.legend()
plt.grid()
plt.show()
print(plt.style.available)