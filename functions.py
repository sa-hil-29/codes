def lesser_of_two_evens(a,b):
    if (a%2 == 1 or b%2 == 1):
        return max(a,b)
    return min(a,b)

def animal_cracker(text):
    str_list = text.lower().split()
    if str_list[0][0] == str_list[1][0]:
        return True
    return False

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or (n1+n2)==20:
        return True
    else:
        return False
    
def old_macdonald(name):
    new_str = ''
    new_str += name[:3].capitalize() + name[3:].capitalize()
    return new_str

def master_yoda(text):
    str_list = text.split()
    str_list.reverse()
    text = " ".join(str_list)
    return text

def almost_there(num):
    if (abs(100 - num)<=10) or (abs(200 - num)<=10):
        return True
    return False

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False

def paper_doll(text):
    new_text = ''
    for char in text:
        new_text += char*3
    return new_text

def blackjack(a,b,c):
    num_sum = a+b+c
    if a==11 or b == 11 or c == 11:
        num_sum -= 10
    if num_sum > 21 :
        return 'BUST'
    return num_sum

def summer_69(nums):
    total = 0
    flag = True
    for num in nums:
        while flag:
            if num != 6:
                total += num
                break
            else:
                flag = False
                break
        while not flag:
            if num != 9:
                break
            else:
                flag = True
                break
    return total

def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i:i+3] == [0,0,7]:
            return True
    return False


    
            








