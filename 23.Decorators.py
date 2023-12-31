import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time
        print(func.__name__+"took"+str(end-start)*1000+"mil sec")
        return result
    return wrapper
@time_it
def cal_squre(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def cal_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array=range(1,10000)
out_squre=cal_squre
out_cube=cal_cube
