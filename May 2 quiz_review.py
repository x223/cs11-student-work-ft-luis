list1 = [4,5,15,11,23,42]
list2 = [1,8,7,16,7,35]
#print list1.index(x)
def compare_lists(list1,list2):
    for x in list1:
        if x >list2[list1.index(x)]:
            print x
        else:
            print list2[list1.index(x)]
compare_lists(list1, list2)
#
def max_value(integer):
    for x in range(1, integer+1):
#

width = input("How Wide?")
length = input("How Tall?")

print width * "* -"
for x in range(1,length):
    print width * "- *"
