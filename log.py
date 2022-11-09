import time


def timestamp(func):
    def wrapper(*args, **kwargs):
        x = time.ctime()
        print(x)
        value = func(*args, **kwargs)
        return value;
    return wrapper;

        



#@timestamp
#def hello(x):
 #   print('Hello', x)
 #
 #
   # return;


#hello('Mom')


