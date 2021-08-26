# viatrix
# list sorting visualizer using turtles
import random

def randomList(length=100, highest=999):
    LIST = []
    while len(LIST) < length:
        LIST.append(random.randint(1,highest))
    return LIST

try:
 import turtle # turtle does not work on all systems (notably mine)

 def drawlist(LIST,t,color=0): # draws a given list, in given colour
    for item in LIST: # for each item
        t.right(90)
        t.pencolor("white")
        t.pd()
        t.fd(999-item)
        if color == 0:
            # need to convert item to a colour (gonna use it as the hue, using Wikipedia's HSV model article)
            h2 = item/167
            x = (1 - abs((h2%2)-1))
            if h2 > 5:
                rgbTuple = (1,0,x)
            elif h2 > 4:
                rgbTuple = (x,0,1)
            elif h2 > 3:
                rgbTuple = (0,x,1)
            elif h2 > 2:
                rgbTuple = (0,1,x)
            elif h2 > 1:
                rgbTuple = (x,1,0)
            else:
                rgbTuple = (1,x,0)
            t.pencolor(rgbTuple)
        else:
            t.pencolor(color)
        t.fd(item)
        t.pu()
        t.bk(999)
        t.left(90)
        t.fd(1)
    t.bk(len(LIST)) # move turtle back to where it started
 
 def visualiseSort(sort,turt,length): # draw a list getting sorted
    turt.clear() # clear screen
    turt.getscreen().setworldcoordinates(0,0,length,999) #set coordinates so it's easy to draw
    turt.pu()
    turt.goto(0,999) # top left
    turt.width((turt.getscreen().window_width()/length)-2) # set pen width so each item has a tiny gap between them
    turt.speed("fastest") # gotta do this here, doesn't work outside of the function for some reason
    unsorted = randomList(length)
    drawlist(unsorted,turt)
    sort(unsorted,turt)
 
 t = turtle.Turtle()
 s = t.getscreen()
except:
 import time
 class SsyntaxPreserve: # create dummy classes so all that turtle syntax doesn't have to be rewritten
  def textinput(self,title,description):
   print(description)
   return input()
  def numinput(self,title,description,default,minimum,maximum):
   number = self.textinput(title,description)
   while type(number)==str:
    try:
     number = int(number)
    except:
     print("No, it has to be a number! Try again")
     number = self.textinput(title,description)
   if number < minimum or number > maximum:
    number = default
   return number
  def bye(self):
   exit()
 s = SsyntaxPreserve()
 class TsyntaxPreserve:
  def __init__(self):
   self.cachedList = []
   self.listIndex = 0
  def fd(self,dist):
   self.listIndex+=dist
  def bk(self,dist):
   self.listIndex-=dist
 t = TsyntaxPreserve()
 def drawlist(LIST,t,color=0):
  t.cachedList[t.listIndex:t.listIndex+len(LIST)] = LIST
  out=""
  for row in reversed(range(24)):
   for item in t.cachedList:
    if item//8 == row:
     out+=" ▁▂▃▄▅▆▇"[item%8]
    elif item//8 > row:
     out+="█"
    else:
     out+=" "
   out+="\n"
  print(out)
  time.sleep(0.005*len(LIST))
 def visualiseSort(sort,t,length):
  unsorted = randomList(length,192)
  t.cachedList = unsorted
  drawlist(unsorted,t)
  sort(unsorted,t)

# here's the sorting algorithms from my sorting file
def quicksort(LIST,t): # quicksort: a more efficient sorting algorithm (yes I learned about sorting algorithms once and retained the information about quicksort)
    if len(LIST)<2:
        return LIST # if LIST has fewer than 2 items it is already sorted
    pivot = LIST.pop(random.randrange(0,len(LIST))) # pick a random element to be pivot, remove it from list
    lessThanPivot = [] # initialize a list to put the numbers less than pivot in, and numbers greater than pivot
    greaterThanPivot = []
    for item in LIST:
        if item < pivot:
            lessThanPivot.append(item) # compare every item to pivot and sort into one of the two lists
        else:
            greaterThanPivot.append(item)
    drawlist(lessThanPivot,t) # draw everything before pivot
    t.fd(len(lessThanPivot))
    drawlist([pivot],t,"black") # draw pivot
    t.fd(1)
    drawlist(greaterThanPivot,t) # draw everything after pivot
    t.bk(len(lessThanPivot)+1)
    lessThanPivot = quicksort(lessThanPivot,t) # sort each of those two lists (recursion!)
    t.fd(len(lessThanPivot)+1)
    greaterThanPivot = quicksort(greaterThanPivot,t)
    t.bk(1)
    drawlist([pivot],t)
    t.bk(len(lessThanPivot))
    return lessThanPivot + [pivot] + greaterThanPivot # put together the sorted lists

def selectionSort(LIST,t):
    for sortedItems in range(len(LIST)):
        smallestItem = sortedItems
        for item in range(sortedItems,len(LIST)): # find the index of the smallest unsorted item
            if LIST[smallestItem] > LIST[item]:
                smallestItem = item
        LIST.insert(sortedItems,LIST.pop(smallestItem)) # move it to the end of sorted items
        drawlist(LIST[sortedItems:smallestItem+1],t) # draw moved items
        t.fd(1)
    t.bk(len(LIST))
    return LIST

def radix2Sort(LIST,t): # radix sort with base 2
    digits = 0
    for item in LIST: # need to find the number of bits to sort
        while item > 1 << digits:
           digits+=1
    for digit in range(digits): # start from least significant bit and iterate to most significant
        buckets=[[],[]] # make 2 buckets
        for item in LIST:
           buckets[item>>digit&1].append(item) # put each item in a bucket depending on the value of a bit
        LIST = buckets[0] + buckets[1] # concatenate buckets
        drawlist(LIST,t)
    return LIST # sorted

def mergeSort(LIST,t):
    if len(LIST)<2:
        return LIST # already sorted list
    half = len(LIST)//2 # halfway point in list
    firstHalf = LIST[:half] # divide list into two halves
    secondHalf = LIST[half:]
    firstHalf = mergeSort(firstHalf,t) # sort each half
    t.fd(half)
    secondHalf = mergeSort(secondHalf,t)
    t.bk(half)
    Sorted = []
    while len(firstHalf) > 0 and len(secondHalf) > 0: # merge two halves
        if firstHalf[0] < secondHalf[0]:
            Sorted.append(firstHalf.pop(0))
        else:
            Sorted.append(secondHalf.pop(0))
    Sorted += firstHalf + secondHalf # one of these will be empty at this point so it's just adding remaining elements
    drawlist(Sorted,t)
    return Sorted

def bubbleSort(LIST,t):
    for i in range(len(LIST)):
        for item in range(len(LIST)-1):
            if LIST[item] > LIST[item+1]: # if these two items are in wrong order:
                LIST.insert(item,LIST.pop(item+1)) #swap
                t.fd(item) # draw swap
                drawlist([LIST[item],LIST[item+1]],t)
                t.bk(item)
    return LIST

def heapSort(LIST,t):
    # need to define swap
    def swap(LIST,t,index1,index2):
        temp = LIST[index1]
        LIST[index1] = LIST[index2]
        LIST[index2] = temp
        t.fd(index1)
        drawlist([LIST[index1]],t)
        t.bk(index1)
        t.fd(index2)
        drawlist([temp],t)
        t.bk(index2)
        return LIST
    def siftDown(LIST,t,heapLen,item):
        while True:
            child = (item+1<<1)-1 # location of child
            if child<heapLen: # at least 1 child
                if child+1<heapLen: # 2 children
                    if LIST[child+1] > LIST[child]:
                        child += 1 # set address to whichever child is greater
                if LIST[child] > LIST[item]:
                    LIST = swap(LIST,t,item,child) # if child is greater than item, swap
                    item = child
                else:
                    break # if child is less than item, break
            else:
                break # if no children, break
        return LIST
    for i in reversed(range(len(LIST))): # iterate backward through list
        LIST = siftDown(LIST,t,len(LIST),i) # sift down every item starting at bottom
    for heapLen in reversed(range(len(LIST))): # gonna work until heap has length 0
        LIST = swap(LIST,t,0,heapLen) # swap first and last item
        LIST = siftDown(LIST,t,heapLen,0) # sift down first item
    return LIST
                
def insertionSort(LIST,t):
    for currentItem in range(1,len(LIST)):
        for item in range(currentItem):
            if LIST[item] > LIST[currentItem]:
                LIST.insert(item,LIST.pop(currentItem))
                t.fd(item)
                drawlist(LIST[item:currentItem+1],t)
                t.bk(item)
                break
    return LIST

sorts = {"s":selectionSort,"q":quicksort,"r":radix2Sort,"m":mergeSort,"b":bubbleSort,"h":heapSort,"i":insertionSort}
while True:
    sort = s.textinput("","Type \"s\" for Selectionsort, \"q\" for Quicksort, \"r\" for Radix sort, \"m\" for Mergesort, \"b\" for Bubblesort, \"h\" for Heapsort, \"i\" for Insertion sort, \"info\" for more information, or \"x\" to eXit.")
    if sort == "info":
        print("""Selection sort checks the entire list to find the smallest item, then the next smallest, then the next smallest, until the list is sorted.
Quicksort picks a random item (called a pivot), and compares everything else to the pivot to get two lists: all items less than the pivot, and all items greater than the pivot. Then it Quicksorts each of those lists.
Radix sort splits the items into 2 lists based on their last digit, then concatenates the lists. It does this with every digit in the numbers. This implementation uses base 2, so there are 2 digits.
Mergesort splits the list in half, mergesorts each half, and combines the two halves by merging: take the lower item from the beginning of the two lists each time.
Bubblesort compares two items at a time, swapping two adjacent items if they are in the worng order.
Heapsort uses a structure called a heap, and moves items through the heap, to sort the list.
Insertion sort moves every item backwards until it is greater than the item before it.""")
    elif sort == "x":
        break
    else:
        try:
            sort = sorts[sort]
        except:
            sort = quicksort
        length = s.numinput("","Length of list",50,10,200)
        visualiseSort(sort,t,int(length))
s.bye()
