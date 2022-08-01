import re


def getMixMax(arr):
    n=len(arr)
    if(n%2==0):
        mx=max(arr[0],arr[1])
        mn=min(arr[0],arr[1])
        i=2
    else:
        mx=mn=arr[0]
        i=1

    while(i < n-1):
        if(arr[i] < arr[i+1]):
            mx=max(mx,arr[i+1])
            mn=min(mn,arr[i])
        else:
            mx=max(mx,arr[i])
            mn=min(mn,arr[i+1])
        i=+2
    
    return(mx,mn)

arr=[100,12,35,68,500,200]
mx,mn=getMixMax(arr)
print("Minimum element is", mn)
print(f"Max element is {mx}")
#if __name__ == '__main__':
   # arr=[100,12,35,68,500,200]
 #   mx,mn=getMixMax(arr)
  #  print("Minimum element is", mn)
    #print(f"Max element is {mx}")