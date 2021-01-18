def merge_sort(arr):
    fir = arr[:len(arr)//2]
    las = arr[len(arr)//2:]
    #print(fir, las)
    if min(len(fir), len(las)) == 1:
        # print([min(int(fir[0]), int(las[0]))])
        li = []
        while (any(fir) and any(las)):
            if fir[0] < las[0]:
                li.append(fir.pop(0))
            else:
                li.append(las.pop(0))

        else:
            li.extend(fir)
            li.extend(las)
        return li
    else:
        fir = merge_sort(fir)
        las = merge_sort(las)
        li = []
        while (any(fir) and any(las)):
            if fir[0] < las[0]:
                li.append(fir.pop(0))
            else:
                li.append(las.pop(0))
                #print(fir, las)
        else:
            li.extend(fir)
            li.extend(las)
    return li

print(merge_sort([3,2,6,1,5,4,16,11,13,14,12,20,18,17,19,15,8,7,9]))