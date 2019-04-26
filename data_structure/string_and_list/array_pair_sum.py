def pair_sum(arr,k):

    if len(arr)<2:
        return 0
    seen = set()
    out = set()

    for num in arr:
        tar = k-num
        if tar not in seen:
            seen.add(num)
        else:
            out.add( ( (min(num,tar)),max(num,tar) ) )
    print (len(out))
    print("\n".join(map(str,list(out))))

if __name__ == "__main__":

    arr = [2,3,1,2,4,3]
    k=7
    pair_sum(arr,k)