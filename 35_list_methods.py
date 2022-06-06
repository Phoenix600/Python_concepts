
'''
----------------------------------------------------------------------------------
                            STRING METHODS
----------------------------------------------------------------------------------
Read these atleast Twice a day 
----------------------------------------------------------------------------------
[SN]    [Methods]                       [Description]
----------------------------------------------------------------------------------
[01]    @append()                   Adds an element to the end of the list
----------------------------------------------------------------------------------
[02]    @extend()                   Adds all element of a list to another list
----------------------------------------------------------------------------------
[03]    @insert()                   Inserts an item at the defined index
----------------------------------------------------------------------------------
[04]    @remove()                   Removes an item from the list
----------------------------------------------------------------------------------
[05]    @pop()                      Returns and removes an element at the given
                                    index.
----------------------------------------------------------------------------------
[06]    @clear()                    Removes all items friom the list
----------------------------------------------------------------------------------
[07]    @index()                    Returns the index of first matched item
----------------------------------------------------------------------------------
[08]    @sort()                     Sort items in a list ascending order 
----------------------------------------------------------------------------------
[09]    @reverse()                  Reverse the order of items in the list
----------------------------------------------------------------------------------
[10]    @count()                    Returns the count of the number passed as an
                                    argument
----------------------------------------------------------------------------------
[11]    @copy()                     Returns a shallow copy of the list
----------------------------------------------------------------------------------
[99]    More..
----------------------------------------------------------------------------------
'''
# sample list to perform operations 

sample_list = [1,2,3,4,5,6,7,8,9,10]

print('''Learning the append() method ''')
print(f"[+] The orignal list is as follows : {sample_list}")
print("Using append() method to add 11 after 10")
sample_list.append(11)
print(f"[+] List Elements  : {sample_list}")


print('''\nLearning the extend() method ''')
ext_list = [12,13,14,15]
print(f"Adding list {ext_list} to new list {sample_list} ")
sample_list.extend(ext_list)
print(f"[+] List after using exted method is {sample_list}")


print('Learning the sort() method')
jumbled_list = [99,56,45,77,86,23,-1,35,0]
print(f"Jumbled List : {jumbled_list}")
# sorting the list
jumbled_list.sort()
print(f"[+] Sorted List : {jumbled_list}")


print('Understanding the insert() method')
investment_list = ["Bitcoin","Ethereum","Bit-Torrent","SHIBU","Dodge Coin","UniCorn","PanCake","Cardano"]
print(f"BIT-GO > Investments >  {investment_list}")
investment_list.insert(-1,input("BIT-GO > Investments > [+]Enter Block-chain name to buy the dip of 10$ : "))
print("[~] Updating your Investments .....")
print(f"BIT-GO > Investments >  {investment_list}")

print('Learning the remove() method')
investment_list.remove(input('Would you like to sell any one of your crypto HODL : '))
print("[~] Updating the crypto HODL ....")
print(f"BIT-GO > Investments >  {investment_list}")


print("Learning the pop() method")
love_intrests = ["Emma Mackey","Sharon Wilsion","Shakira","Katty Perry","Emma Stone","Emma Watson","Zendaya","Rihana"]
print(f"Jhon Don's Love Intrests : {love_intrests}")
dumped_girl = love_intrests.pop(int(input("[+] Enter the index number to dump your girl > ")))
print(f"You dumped {dumped_girl},so bad :(, well ....")
print(f"Congrats, Now there is more room for your libido : {love_intrests} ")


print('Learning the clear() method')
if input("Showing your love intrests publically is not a good act ,would you like to erase them Y/N > ") == 'Y' :
    love_intrests.clear()
print(f"Now there is no-one see > {love_intrests}")


print("Learning the index() method")
Lottery_Numbers = [13,56,12,34,67,32,43,91,46,12,1,666,999,34]
print(f"Todays Lottery Number : {Lottery_Numbers}")
Person_number = Lottery_Numbers.index(int(input("[+]First Person To Won Price / Search Number : ")))
print(f"Person Number : {Person_number+2} : Won, First ")

print("Learning the sort() method")
sample_list = [100,54,23,65,12,78,34]
print(f"Unsoretd List : {sample_list}")
sample_list.sort()
print(f"Sorted List : {sample_list}")
sample_letters = ["A","C","B","Y","E","Z"]
print(f"Jumbled_words : {sample_letters}")
sample_letters.sort()
print(f"Sorted Words : {sample_letters}")

print("Learning the reverse() method : ")
reverse_list = ["Hello","World","!!!"]
print(reverse_list)
reverse_list.reverse()
print(reverse_list)


print("Learning the count() method : ")
count_list = [12,45,56,67,34,12,56,78,90,12,45,64,47,27,21,12,31,12]
print(count_list)
print(f"{count_list.count(int(input('Enter number to fnd the number ocurrance : ')))} times reapted")


print("[+]Learning the copy() method ")
sample_list1 = ["D***","Pranay","Ramteke"]
sample_list2 =  sample_list1.copy()
print(f"The memory address of sample_list1 = {id(sample_list1)}")
print(f"The memory address of sample_list2 = {id(sample_list2)}")
''' ---------------------- EOF-----------------------------------'''
