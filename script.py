import time

repeat_times = 1000000
arr = [1, 2, 3]
n = 3
time.time()

start2 = time.time()
for i in range(repeat_times):
    print(n)
end2 = time.time()

start1 = time.time()
for i in range(repeat_times):
    print(len(arr))
end1 = time.time()

print('len', end1 - start1)
print(end2 - start2)
