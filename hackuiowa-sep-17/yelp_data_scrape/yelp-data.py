import linecache
import random

def parse_data(source1, dest_file1, dest_file2 ):
    total = 0
    with open(source1) as biz_file:
        for line in biz_file:
           data = line.split(":")
           biz_name = data[2].split(",")[0].replace('"', '')

           biz_address = data[4].split("city")[0].replace('"', '').replace(",", '')
           biz_city  = data[5].split("state")[0].replace('"', '').replace(",",'')
           biz_state = data[6].split("postal_code")[0].replace('"', '').replace(",",'')
           total += 1
           dest_file1.write(biz_name + "\n")
           dest_file2.write(biz_name + "|" + biz_address + "|" + biz_city + "|" +biz_state + "\n")


    print("DONE!")
    print(total) #156,639
    dest_file1.close()
    dest_file2.close()

def test_parse_data(test_source, test_dest):
    total = 0
    with open(test_source) as biz_file:
        for line in biz_file:
            data = line.split(":")
            biz_name = data[2].split(",")[0].replace('"', '')
            test_dest.write(biz_name + "\n")
            total += 1
    print("Done")
    print(total)
    test_dest.close()
def parse_data_name_location(source, dest_file):
    total = 0
    with open(source) as biz_file:
        for line in biz_file:
            data = line.split(":")
            biz_name = data[2].split(",")[0].replace('"', '')
            biz_city = data[5].split("state")[0].replace('"', '').replace(",", '')
            biz_state = data[6].split("postal_code")[0].replace('"', '').replace(",", '')
            dest_file.write(biz_name + "|" + biz_city + "|" + biz_state + "\n")
            total += 1
    print("Done!")
    print(total)
    dest_file.close()
def get_subset_data(source, dest, num):
    total =0
    with open(source) as file:
        for line in file:
            line_num = random.randint(1, 156639)
            line = linecache.getline(file, line_num)
            dest.write(line + "\n")
            total += 1

    print("Done")
    print(total)
    dest.close()




if __name__ == '__main__':
    '''
    biz_dest1 = open('../../Downloads/hackathon/biz_name.txt', 'w')
    biz_dest2 = open('../../Downloads/hackathon/biz_name_location.txt', 'w')
    parse_data('../../Downloads/dataset/business.json', biz_dest1, biz_dest2)

    biz_dest_test = open('../../Downloads/hackathon/biz_name_test.txt', 'w')
    test_parse_data('../../Downloads/dataset/biz_test.json', biz_dest_test)

    biz_dest = open('../../Downloads/hackathon/biz_name_location.txt', 'w')
    parse_data_name_location('../../Downloads/dataset/business.json', biz_dest)
    '''
    smaller_data = open('../../Downloads/hackathon/subset_biz_name.txt', 'w')
    file = open('../../Downloads/hackathon/biz_name.txt', 'r')
    lines = file.readlines()
    for i in range(0, 1000):
        line_num = random.randint(1, 156639)
        line = lines[line_num]
        smaller_data.write(line)
        print(i)
    smaller_data.close()

    #get_subset_data('../../Downloads/dataset/business.json', smaller_data, num=1000)