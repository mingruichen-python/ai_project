heights=[]
while True:
    try:
        one_height=int(input("please input the height of your classmate(only put one and in cm)"))
        heights.append(one_height)
        print(max(heights),"cm")
    except Exception as e:
        print(e)
