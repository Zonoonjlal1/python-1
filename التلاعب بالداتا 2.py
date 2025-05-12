import numpy as np
#مصفوفة ذات بعدين اضف اليها صف جديد
arr1 =np.array([[1,2,3],[4,5,6]])
x = np.insert(arr1,2,[7,8,9], axis=0)
print(x)
#غمود جديد
arr2 =np.array([[1,2,3],[4,5,6]])
y = np.insert(arr2,2,[7,8], axis=1)
print(y)
#دمج مصفوفتين تحت بعض
arr3 =np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[7,8,9]])
z = np.vstack((arr3,arr4))
print(z)
#دمج مصفوفتين جمب بعض
arr5 = np.array([[1,2,3],[4,5,6]])
arr6 = np.array([[7,8],[9,10]])

w = np.hstack((arr5, arr6))
print(w)

#فصل المصفوفة الواحدة الى عدة مصفوفات
arr7 =np.arange(1,10).reshape(3,3)
print(arr7)
s = np.split(arr7,3)
print(s)
#عمل تنظبف للداتا واكتشاف المكان الفارغ في المصفوفة
arr8 = np.array([[1,2,3,np.nan,5,6,7]])
print(arr8)
print(np.nan_to_num(arr8))
d = np.isnan(arr8)
print(d)
#عمل تنظبف للداتا واكتشاف القيم المالا نهاية في المصفوفة
arr9 = np.array([[1,2,3,np.inf,5,6,7]])
f = np.isinf(arr9)
#دمج مصفوفتين مع بعض
arr10 = np.array([1,2,3,5,6,7])
arr11 = np.array([8,9,10])
g = np.concatenate((arr10,arr11))
print(g)
#فحص تساوي المصفوفات بطريقتين
arr12 = np.array([1,2,3])
arr13 = np.array([1,2,6])
h = np.array_equal(arr12,arr13)
print(h)
t = np.equal(arr12,arr13)
print(t)
#فحص عدم تساوي المصفوفات
arr14 = np.array([1,2,3])
arr15 = np.array([1,2,6])
i = np.not_equal(arr14,arr15)
print(i)
