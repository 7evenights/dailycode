first_input = input().split()
order = int(first_input[0])
dont_cal = int(first_input[1])
bill = list(map(int, input().rstrip().split()))
charge = int(input())
bill.remove(bill[dont_cal])
sumbill = sum(bill)
if sumbill/2 == charge:
    print("Bon Appetit")
else:
    print(charge-int(sumbill/2))
