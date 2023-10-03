
def outer_function(func):
    def inner_function(*args,**kwrgs):
        r=func(*args,**kwrgs)
        return r
    return inner_function




#how can you change the behaviour of this function without touching source code
@outer_function
def get_square(item_list):
    new_item_list=[]
    for item in item_list:
        new_item_list.append(item*item)
    return new_item_list

if __name__=='__main__':
    input_list = [2,4,6,8,9]
    result = get_square(input_list)
    print(result)