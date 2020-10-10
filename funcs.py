def contains_200(dictnr):
    """Function checks if 200 is in the dictionary"""
    contains = False
    for i in dictnr:
        if dictnr[i] == 200:
            contains = True
    print(contains)
    
    
def find_long_words(txt, num):
    words_arr = txt.split(" ")
    result = []
    for wrd in words_arr:
        if len(wrd) > int(num):
            result.append(wrd)
    print(result)
    
    
def divide_nums(a, b):
    if b == 0:
        print("You can't devide by 0")
        return None
    else:
        return a / b