print("输入原始数组：");

num = 0;
array = [];

while num < 10  :
    a = input("数字"+str(num+1)+":");
    array.append(int(a));
    num += 1;

print("排序开始");
print(array);
print(len(array));
for i in range(0,len(array)-1) :
    for k in range(i+1,len(array)) :
        if array[i] < array[k] :
            cache = 0;
            cache = array[k];
            array[k] = array[i];
            array[i] = cache;
print(array);



