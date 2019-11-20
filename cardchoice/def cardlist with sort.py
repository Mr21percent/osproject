import copy

<<<<<<< HEAD

a=['우리체크', 0 ,'x*0.8',0]
b=['우리신용', 10000 ,'x-3000.0',0]
c=['CU·배달의민족 삼성카드 taptap', 1500, 'x-(x//1500)*200',0]
소지카드=['우리체크','CU·배달의민족 삼성카드 taptap']
편의점=[a,b,c]
스팅=[a,b,c]
주유소=[a,b,c]
가맹점명=["편의점", "주유소", "스팅"]
가맹점=[편의점, 주유소, 스팅]
x=10000

=======
>>>>>>> 5260af700a082e7bf629b88f0f4ac6cdbf339c4f
def where(place):
    for i in range(len(가맹점명)):
        if 가맹점명[i]==place:
            return 가맹점[i]
    return "가맹점이 아닙니다."

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][3]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num[3] < pivot:
            lesser_arr.append(num)
        elif num[3] > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

def card_sort(store, cost):        
    x=cost
    for i in range(len(store)):
        if x>=store[i][1]:
            realcost=eval(store[i][2])
        else:
            realcost=x
        store[i][3]=realcost
    sortcard=copy.deepcopy(store)
    return quick_sort(sortcard)

def doihave(sortedcard,mycard):
    for i in range(len(sortedcard)):
        if sortedcard[i][0] in mycard:
            x = i
            break
    return sortedcard[i][0]

<<<<<<< HEAD

=======
>>>>>>> 5260af700a082e7bf629b88f0f4ac6cdbf339c4f
#start
imin="편의점"
ls=card_sort(where(imin),12000)
print(ls)
a=doihave(ls,소지카드)
print(a)
<<<<<<< HEAD
=======

>>>>>>> 5260af700a082e7bf629b88f0f4ac6cdbf339c4f
