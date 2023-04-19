class Node:

    def __init__(self, giatri, mu):
        self.giatri = giatri
        self.mu = mu
        self.next = None

class Link:

    def __init__(self):
        self.head = None

    def printList(self):
        # temp = self.head
        # while (temp):
        #     strl = str(temp.giatri)+str(temp.mu)+"+"
        #     temp = temp.next
        # print(strl[:-1])
        temp = self.head
        while (temp):
            print(temp.giatri, temp.mu)
            temp = temp.next
#Tao eq1
eq1 = Link()
eq1.head = Node(2,3)
eq12 = Node(1,2)
eq1.head.next = eq12
#Tao eq2
eq2 = Link()
eq2.head = Node(1,4)
eq22 = Node(10,3)
eq23 = Node(3,2)
eq24 = Node(4,0)
eq2.head.next = eq22
eq22.next = eq23
eq23.next = eq24
#Tao eq tong eq1 va eq 2
eqtong = Link()
if (eq1.head.mu > eq2.head.mu):
    eqtong.head = Node(eq1.head.giatri,eq1.head.mu)
    eq1.head = eq1.head.next
    eqtong.next = Node
    print(eqtong.head.giatri, eqtong.head.mu)
elif (eq1.head.mu < eq2.head.mu):
    eqtong.head = Node(eq2.head.giatri,eq2.head.mu)
    eq2.head = eq2.head.next
    eqtong.next = Node
    print(eqtong.head.giatri, eqtong.head.mu)
else:
    eqtong.head = Node(eq1.head.giatri+eq2.head.giatri, eq1.head.mu)
    eq1.head = eq1.head.next
    eq2.head = eq2.head.next
    eqtong.next = Node
    print(eqtong.head.giatri, eqtong.head.mu)
while (eq1.head != None):
    if (eq1.head.mu > eq2.head.mu):
        nut1 = Node(eq1.head.giatri, eq1.head.mu)
        eqtong.next = nut1
        eq1.head = eq1.head.next
        print(eqtong.next.giatri, eqtong.next.mu)
    elif (eq1.head.mu < eq2.head.mu):
        nut1 = Node(eq2.head.giatri, eq2.head.mu)
        eqtong.next = nut1
        eq2.head = eq2.head.next
        print(eqtong.next.giatri,eqtong.next.mu)
    elif (eq1.head.mu == eq2.head.mu):
        nut1 = Node(eq1.head.giatri + eq2.head.giatri, eq1.head.mu)
        eqtong.next = nut1
        eq1.head = eq1.head.next
        eq2.head = eq2.head.next
        print(eqtong.next.giatri, eqtong.next.mu)
    if eq2.head != None:
        eqtong.next = Node(eq2.head.giatri,eq2.head.mu)
        eq2.head = eq2.head.next
        print(eqtong.next.giatri, eqtong.next.mu)
