
import time

def timeme(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print('Total time', run_time)
        return value
    return wrapper_timer

#to test @timeme
#@timeme
#def operationmath(x,y):
    #print(int(x+y))
    #print(int(x-y))
    #print(int(x*y))
    #print(int(x/y))
    #time.sleep(2)
    #return;


#operationmath(10,5)
   


