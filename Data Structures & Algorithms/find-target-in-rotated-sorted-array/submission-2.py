class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_increasing(a,b):
            if a<b:
                return True
            return False
        def find_smallest(start_index, end_index, arr):
            #print("-----start_index-----",start_index,"-----end_index-----",end_index,"--------------------------------")
            if start_index == end_index:
                return start_index
            if end_index-start_index==1:
                if is_increasing(arr[start_index],arr[end_index]):
                    return start_index
                else:
                    return end_index
                
            middle_index = (start_index+end_index)//2 
            val_start = arr[start_index]
            val_end = arr[end_index]
            val_mid = arr[middle_index]


            if is_increasing(val_start,val_mid) and is_increasing(val_mid,val_end):
                return start_index

            elif  is_increasing(val_start,val_mid) and not is_increasing(val_mid,val_end):
                return find_smallest(middle_index, end_index, arr)
            elif not is_increasing(val_start,val_mid) and is_increasing(val_mid,val_end):
                return find_smallest(start_index, middle_index, arr)

        def binary_search(start_index, end_index, arr, target):
                if start_index==end_index:
                    if arr[start_index]==target:
                        return start_index
                    else:
                         return -1

                if len(arr)==1:
                    if arr[start_index]==target:
                        return start_index     
                mid_index = (start_index+end_index)//2 
                val_mid = arr[mid_index]
                if target == val_mid:
                    return mid_index
                elif target < val_mid:
                    return binary_search(start_index, mid_index, arr, target)
                else:
                    return binary_search(mid_index+1, end_index, arr, target)
        arr = nums
        pos_smallest = find_smallest(0, len(arr)-1, arr)
        #print("-----pos_smallest-----",pos_smallest,"--------------------------------")
        if target == arr[pos_smallest]:
            return pos_smallest
        if target < arr[pos_smallest]:
            return -1
        elif target >= arr[pos_smallest] and target <= arr[-1]:
            return binary_search(pos_smallest+1, len(arr)-1, arr, target)
        elif pos_smallest>0 and target >= arr[0]:
            return binary_search(0, pos_smallest-1, arr, target)
        else:
            return -1
    


            




        

        