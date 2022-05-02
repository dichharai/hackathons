ordered_file = open('../../Downloads/hackathon/first_1000_biz_name.txt', 'r')
count = 1
with open('../../Downloads/hackathon/first_1000_biz_name.txt') as of:
    for line in of:
        print(line)
        count += 1
print("total " + str(count))