
import os
import random



os.mkdir(test.output)
os.mkdir(test.log)
os.mkdir(test.error)

m1 = 5.0
m2 = 10.0




count = 0
vi1 = 0
vi2 = 0
while count < 11:
    vi1 = random.uniform(0, 299792458)
    vi2 = random.uniform(0, 299792458)
    v1 = (((m1 - m2)/(m1 + m2)) * vi1) + (((2 * m1)/(m1 + m2)) * vi2)
    v2 = (((2 * m1)/(m1 + m2)) * vi1) + (((m1 - m2)/(m1 + m2)) * vi2)
    count = count + 1

    print()
    print('vi1', vi1)
    print('vi2', vi2)
    print('v1', v1)
    print('v2', v2)
    print()
