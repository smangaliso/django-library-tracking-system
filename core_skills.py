import random
rand_list = random.sample(range(1,21), 10)

list_comprehension_below_10 = [x for x in rand_list if x<10]

def below_10(nums):
    num_below_10 =[]
    for num in nums:
        if num < 10:
            num_below_10.append(num)
    return num_below_10

filter_below_10 = filter(below_10,rand_list)