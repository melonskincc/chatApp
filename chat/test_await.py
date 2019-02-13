import asyncio
def a():
    i=0
    while i<4:
        x = yield i
        print(x)
        i+=1

if __name__ == '__main__':
    a = a()
    print(a.send(1))