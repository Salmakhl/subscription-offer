# Function to calculate the cost of different subscription offers based on monthly call duration
def co(c):
    tab= []
    print("cost for the 0DH offer (2DH per minute, no free minutes)")
    of0 = c* 2
    tab.append(of0)
    if c> 30:
        print("cost for the 20DH offer with 30 minutes of free calls and additional charges (1.5DH per minute)")
        of20 = 20 + (c-30) * 1.5
    tab.append(of20)
    if c> 60:
        print("cost for the 50DH offer with 60 minutes of free calls and additional charges (1DH per minute)")
        of50 = 50 + (c-60) * 1
    tab.append(of50)
    if c> 120:
        print("cost for the 100DH offer with 120 minutes of free calls and additional charges (0.5DH per minute)")
        of100 = 100 + (c-120) * 0.5
    tab.append(of100)

    return tab
c= float(input("Enter the total call duration for the month in minutes: "))
tab= co(c)
print("The total cost to pay at the end of the month for subscription offers 0DH, 20DH, 50DH, 100DH:")
print(tab)

Min = tab[0]
for i in range(0, 4):
    if Min > tab[i]:
        Min = tab[i]

# Check if the lowest cost offer (0DH, 20DH, 50DH, 100DH)offer or the 200DH offer
if Min > 200:
    print("The lowest cost offer is the 200DH monthly subscription.")
else :
    of = tab.index(Min) #of=offer
    print("The lowest cost offer is offer number",of+1)
