dest = open('../../Downloads/hackathon/first_1000_biz_name.txt', 'w')
file = open('../../Downloads/hackathon/biz_name.txt', 'r')

lines = file.readlines()
for i in range(0, 1000):
    line = lines[i]
    dest.write(line)
    print(i)
dest.close()
