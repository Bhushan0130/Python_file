def func(rows,cols):
    new_list = []

    for i in range(rows):
        l = []
        for j in range(cols):
            l.append(0)
        new_list.append(l)

    top = 0
    bottom = rows-1
    left = 0
    right = cols-1
    count =1

    while top <= bottom and left <=right:
        
        for col in range(left, right+1):
            new_list[top][col] = count
            count+=1
        top +=1

        for row in range(top,bottom+1):
            new_list[row][right] = count
            count+=1
        right-=1

        if top<=bottom:
            for col in range(right,left-1, -1):
                new_list[bottom][col]=count
                count+=1
            bottom -=1
            
        if left<=right:
            for row in range(bottom, top-1, -1):
                new_list[row][left] = count
                count+=1
            left +=1


    for row in new_list:
        print(row)

# func(3,4)

m = int(input('Enter number of rows: '))
n = int(input('Enter number of columns: '))
func(m,n)

