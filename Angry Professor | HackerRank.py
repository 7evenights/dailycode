for _ in range(int(input())):
    student_needstudent= [int(x) for x in input().split()]
    student = student_needstudent[0]
    needstudent = student_needstudent[1]
    time = [x for x in input().split() if int(x) <= 0]
    if len(time) < needstudent:
        print("YES")
    else:
        print("NO")
