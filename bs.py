def binarysearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
l=[7,8,9,10,11]
low=0
h=len(l)-1
key=int(input("enter the key element"))
result=binarysearch(l,low,h,key)
if result==-1:
    print("element not found")
else:
    print("element found at index:",result)
        
