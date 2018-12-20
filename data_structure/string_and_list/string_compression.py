def string_comp(strings):

    empty_string = ""
    string_length= len(strings)

    print string_length

    # check the edge point

    if string_length == 0 :

        return "empty string"

    if string_length == 1:
        print (strings+"1")

    i=1
    cnt =1
    while i < string_length:

        if strings[i] == strings[i-1]:
            cnt +=1
        else:
            empty_string = empty_string+strings[i-1]+str(cnt)
            cnt = 1
        i +=1
    empty_string = empty_string+strings[i-1]+str(cnt)

    print empty_string

if __name__ == "__main__":

    s = "Abbcc"
    print(string_comp(s))

    s1 = ""
    print(string_comp(s1))


