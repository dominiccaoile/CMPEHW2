

def increment_int_a(someval):
    someval += 1
 
def increment_int_b(someval):
    someval[0] += 1
def main():
    a = 32
    increment_int_a(a)
    print(a)
    b = [32]
    increment_int_b(b)
    print(b)
    return;

main()

a = [ '0','1','2',]

print(a[0:3:2])

print(a[3:0:2])