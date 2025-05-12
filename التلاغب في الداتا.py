import numpy as np
#مصفوفة عبارة عن مجموعة ارقم  ثم عملها كمصفوفة ذات بعدين من الارقام الصحيحة
x = np.arange(10) .reshape(2,5)
print(x)

#مصفوفة عبارة عن مجموعة ارقم  ثم عملها كمصفوفة ذات بعدين من الارقام العشرية
y = np.linspace(0, 10, 10).reshape(2,5)
print(y)
#انشاء مصفوفه بعد واحد وحذ قيمتين منها
x_n = np.arange(5)
print(x_n)
b = np.delete(x_n, [0,1])
print(b)
#انشاء مصفوفة ذات بعدين وحذف صف واحدة منها
z = np.arange(10).reshape(2,5)
print(z)
c= np.delete(z, 0, axis=0)
print(c)
#انشاء مصفوفة ذات بعدين وحذف عمود واحدة منها
g = np.arange(10).reshape(2,5)
print(g)
d = np.delete(g, 1, axis=1)
print(d)
#عمل مصفوفة واضافة عنصر اخير لها
s = np.array([1,2,3,4,5])
print(s)
e = np.append(s,[6 ])
print(e)
#عمل مصفوفة ذات بعدين واضافة عنصر لها كصف
t = np.array([[1,2,3],[4,5,6]])
print(t)
f = np.append(t,[[7,8,9]] , axis=0)
print(f)

#عمل مصفوفة ذات بعدين واضافة عنصر لها كعمود

i = np.array([[10,20,30],[40,50,60]])
print(i)
h = np.append(i,[[7],[8],], axis=1)
print(h)
#عمل مضفوفة واضافة قيم لها في مكان مخصص

k = np.arange(6)
print(k)
l=np.insert(k,2,[7,8])
print(l)