import random
global jing
jing = 0
global death
death = 0

before_lottery_crystal = 52766
after_lottery_crystal = 52766

treasury = 0


global n1
n1 = 0
global n2
n2 = 0
global n3
n3 = 0
global n4
n4 = 0
global n5
n5 = 0
global n6
n6 = 0
global n7
n7 = 0
global n8
n8 = 0
global n9
n9 = 0
global n10
n10 = 0
global n11
n11 = 0
global n12
n12 = 0
global n13
n13 = 0
global n14
n14 = 0
global n15
n15 = 0
global n16
n16 = 0
global n17
n17 = 0
global n18
n18 = 0
global n19
n19 = 0
global n20
n20 = 0


def find_body():
    global period
    if period == 1:
        global n1
        n1 = n1+1
        #print("local n1",n1)
    if period == 2:
        global n2
        n2 = n2+1
        #print("local n2",n2)
    if period == 3:
        global n3
        n3 = n3+1
       # print("local n3",n3)
    if period == 4:
        global n4
        n4 = n4+1
       # print("local n4",n4)
    if period == 5:
        global n5
        n5 = n5+1
       # print("local n5",n5)
    if period == 6:
        global n6
        n6 = n6+1
       # print("local n6",n6)
    if period == 7:
        global n7
        n7 = n7+1
       # print("local n7",n7)
    if period == 8:
        global n8
        n8 = n8+1
       # print("local n8",n8)
    if period == 9:
        global n9
        n9 = n9+1
       # print("local n9",n9)
    if period == 10:
        global n10
        n10 = n10+1
       # print("local n10",n10)
    if period == 11:
        global n11
        n11 = n11+1
       # print("local n11",n11)
    if period == 12:
        global n12
        n12 = n12+1
       # print("local n12",n12)
    if period == 13:
        global n13
        n13 = n13+1
       # print("local n13",n13)
    if period == 14:
        global n14
        n14 = n14+1
       # print("local n14",n14)
    if period == 15:
        global n15
        n15 = n15+1
       # print("local n15",n15)
    if period == 16:
        global n16
        n16 = n16+1
       # print("local n16",n16)
    if period == 17:
        global n17
        n17 = n17+1
       # print("local n17",n17)
    if period == 18:
        global n18
        n18 = n18+1
       # print("local n18",n18)
    if period == 19:
        global n19
        n19 = n19+1
       # print("local n19",n19)
    if period == 20:
        global n20
        n20 = n20+1
       # print("local n20",n20)


def lottery():
    i = 0
    draw = 0
    global jing
    global crystal_spending
    global after_lottery_crystal
    global before_lottery_crystal
    global death
    global period
    global green
    global incarnation
    while i == 0:
        luck = random.randint(1, 1000)
        if luck < 8:
            draw = draw+1
            crystal_spending = crystal_spending+150
            after_lottery_crystal = after_lottery_crystal-150
            if after_lottery_crystal < 0:
                if period == 4 or period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
                    incarnation = 1
                    death = death+1
                    find_body()
                    break
                else:
                    break
            i = 1
        elif draw > 298:
            draw = draw+1
            crystal_spending = crystal_spending+150
            after_lottery_crystal = after_lottery_crystal-150
            if after_lottery_crystal < 0:
                if period == 4 or period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
                    incarnation = 1
                    death = death+1
                    find_body()
                    break
                else:
                    break
            jing = jing+1
            i = 1
        else:
            draw = draw+1
            crystal_spending = crystal_spending+150
            after_lottery_crystal = after_lottery_crystal-150
            if after_lottery_crystal < 0:
                if period == 4 or period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
                    incarnation = 1
                    death = death+1
                    find_body()
                    break
                else:
                    break

    green = int(green)
    if period > 1:
        global g1
        if g1 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 28:
                    green = green+1
                    g1 = 1
    if period > 2:
        global g2
        if g2 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 26:
                    green = green+1
                    g1 = 1
    if period > 8:
        global g8
        if g8 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 23:
                    green = green+1
                    g8 = 1
    if period > 10:
        global g10
        if g10 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 22:
                    green = green+1
                    g10 = 1
    if period > 11:
        global g11
        if g11 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 21:
                    green = green+1
                    g11 = 1
    if period > 14:
        global g14
        if g14 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 18:
                    green = green+1
                    g14 = 1
    if period > 18:
        global g18
        if g18 == 0:
            for i in range(draw):
                luck = random.randint(1, 25000)
                if luck < 16:
                    green = green+1
                    g18 = 1


# strategies=============================================================================================
def only_rs():
    subtotal_crystal_spending = 0
    global total_crystal_spending
    global crystal_spending
    total_crystal_spending = 0
    if period == 4 or period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
        lottery()
        total_crystal_spending = total_crystal_spending+crystal_spending
        #print("crystal_spending", crystal_spending)
    else:
        crystal_spending = 0
        subtotal_crystalspending = 0
# =========================================================================================================


def rs_and_MVCs():
    subtotal_crystal_spending = 0
    global total_crystal_spending
    global crystal_spending
    total_crystal_spending = 0
    # drawing 1 pool per month
    if period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    if period == 6 or period == 9 or period == 13 or period == 17:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    # drawing 2 pool per month
    if period == 4:
        local_crystal_spending = 0
        lottery()
        # subtotal_crystal_spending=subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        # subtotal_crystal_spending=subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    else:
        crystal_spending = 0
        subtotal_crystal_spending = 0
    # print("total_crystal_spending",total_crystal_spending)
# =================================================================================================================


def rs_MVCs_and_VCs():
    subtotal_crystal_spending = 0
    global total_crystal_spending
    global crystal_spending
    global green
    global g1
    global g2
    global g8
    global g10
    global g11
    global g14
    global g18
    global extra
    total_crystal_spending = 0
    # drawing 1 pool per month
    if period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 6 or period == 9 or period == 13 or period == 17:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 1:
        lottery()
        g1 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 2:
        lottery()
        g2 = 1
        green = green+1
        extra = extra+5
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 11:
        lottery()
        g11 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 18:
        lottery()
        g18 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending

    # drawing 2 pool per month
    elif period == 4:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 8:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g8 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 10:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g10 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 14:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g14 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    else:
        crystal_spending = 0
        subtotal_crystal_spending = 0
    # print("total_crystal_spending",total_crystal_spending)
# ===========================================================================================================================


def mixed1():  # give up g1 and g2
    subtotal_crystal_spending = 0
    global total_crystal_spending
    global crystal_spending
    global green
    global g1
    global g2
    global g8
    global g10
    global g11
    global g14
    global g18
    total_crystal_spending = 0
    # drawing 1 pool per month
    if period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 6 or period == 9 or period == 13 or period == 17:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 11:
        lottery()
        g11 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 18:
        lottery()
        g18 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending

    # drawing 2 pool per month
    elif period == 4:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 8:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g8 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 10:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g10 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 14:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g14 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    else:
        crystal_spending = 0
        subtotal_crystal_spending = 0
# ============================================================================================================


def mixed2():  # give up g1 and g8
    subtotal_crystal_spending = 0
    global total_crystal_spending
    global crystal_spending
    global green
    global g1
    global g2
    global g8
    global g10
    global g11
    global g14
    global g18
    global extra
    total_crystal_spending = 0
    # drawing 1 pool per month
    if period == 7 or period == 8 or period == 10 or period == 14 or period == 16 or period == 20:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 6 or period == 9 or period == 13 or period == 17:
        lottery()
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 2:
        lottery()
        g2 = 1
        extra = extra+5
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 11:
        lottery()
        g11 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending
    elif period == 18:
        lottery()
        g18 = 1
        green = green+1
        # print("crystal_spending",crystal_spending)
        total_crystal_spending = total_crystal_spending+crystal_spending

    # drawing 2 pool per month
    elif period == 4:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 8:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 10:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g10 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    elif period == 14:
        local_crystal_spending = 0
        lottery()
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 1",subtotal_crystal_spending)
        lottery()
        green = green+1
        g14 = 1
        subtotal_crystal_spending = subtotal_crystal_spending+crystal_spending
        #print("subtotal 2",subtotal_crystal_spending)
        total_crystal_spending = total_crystal_spending+subtotal_crystal_spending
    else:
        crystal_spending = 0
        subtotal_crystal_spending = 0

    # print("total_crystal_spending",total_crystal_spending)
# strategies===================================================================================================


def play_pcr():
    global period
    global treasury
    global incarnation
    period = 0
    incarnation = 0
    month = period+5
    global before_lottery_crystal
    global after_lottery_crystal
    before_lottery_crystal = 52766
    after_lottery_crystal = 52766
    for period in range(20):
        if incarnation == 0:
            # print("period",period)
            if period == 4 or period == 10:
                monthly_revenue = 35000
            # must disable this session if you don't like mizi cat sabre
            else:
                monthly_revenue = 10000
            before_lottery_crystal = after_lottery_crystal+monthly_revenue
            after_lottery_crystal = before_lottery_crystal
# strategybase=====================================================================================================
            # only_rs()
            # rs_and_MVCs()
            rs_MVCs_and_VCs()
            # mixed1()
            # mixed2()
# strategybase=====================================================================================================
        else:
            break
    if after_lottery_crystal > 0:
        treasury = treasury+after_lottery_crystal
        #print("total_crystal_spending", total_crystal_spending)
        # print("after_lottery_crystal",after_lottery_crystal)
        # print("before_lottery_crystal",before_lottery_crystal)


# mainprogram
green = 0
totalgreen = 0
for n in range(10000):
    totalgreen = totalgreen+green
    green = 0
    g1 = 0
    g2 = 0
    g8 = 0
    g10 = 0
    g11 = 0
    g14 = 0
    g18 = 0
    extra = 0
    play_pcr()
print("n1", n1)
print("n2", n2)
print("n3", n3)
print("n4", n4)
print("n5", n5)
print("n6", n6)
print("n7", n7)
print("n8", n8)
print("n9", n9)
print("n10", n10)
print("n11", n11)
print("n12", n12)
print("n13", n13)
print("n14", n14)
print("n15", n15)
print("n16", n16)
print("n17", n17)
print("n18", n18)
print("n19", n19)
print("n20", n20)
print("P", death/10000)
utility = (1-(death/10000)**0.737)*(35+5*4+2*totalgreen/10000+extra)
print("utility", utility)
# print("g1",g1)
# print("g2",g2)
# print("g8",g8)
# print("g10",g10)
# print("g11",g11)
# print("g14",g14)
# print("g18",g18)
# print("green",green)
print("average green", totalgreen/10000)
#print("only RS")
#print("RS and MVC")
print("RS MVC and VC")
#print("mixed 1")
#print("mixed 2")
#print ("Treasury",treasury)
# print(jing)
