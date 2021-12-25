dc={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"fourty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",

}

def nm(num):
    if num == 0:
        return 'zero'
    def two():
        digit=[x for x in str(num)]
        if digit[1]=='0':
            return dc[num]
        if num>20:
            return dc[int(digit[0])*10]+" "+dc[int(digit[1])]
        if num<20 and num>9:
            return dc[int(num)]
    if len(str(num)) == 2:
        return two()
    if len(str(num))==3:
        digit=[x for x in str(num)]
        if digit[1]=='0' and digit[2]=='0':
            return dc[int(digit[0])] +" " + "hundred"
        if digit[1]=='0':
            del digit[1]
            return dc[int(digit[0])]+ " hundred " + dc[int(digit[1])]
        else:
            num=int(digit[1]+digit[2])
            return dc[int(digit[0])]+ " hundred " +two()

