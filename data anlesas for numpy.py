import numpy as np
# عمل مصفوفة ذات بعدين
arr1 = np.arange(20).reshape(4,5)
print(arr1)
#استدغاء للقيم بطرق مختلفة
print(arr1[0,0])
print(arr1[1,1])
z=arr1[1:4 ,2:5]
print(z)
#التبديل في احد عناص المصفوفة

w=arr1[0 ,0] = 20
print(arr1)
#استدعاء لرنج محدد من القيم
g = arr1[:3 , 2:]
print(g)
#نسخة من المصفوفة قبل التعديل
s = np.copy(arr1)
print(s)
arr1[0,0] = 80
print(arr1)
print(s)