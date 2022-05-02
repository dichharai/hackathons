def get_biz_name_review(source, dest):
    total = 0
    with open(source) as biz_file:
        for line in biz_file:
            data = line.split(":")
            biz_name = data[2].split(",")[0].replace('"', '')
            #print(biz_name)
            stars = data[10].split(",")[0]
            #print(stars)
            review_count = data[11].split(',')[0]
            #print(review_count)
            dest.write("|" + biz_name + "|" + stars + "|" + review_count + "|"'\n')
            total += 1

    print("Done!")
    print(total)
    dest.close()

if __name__ == '__main__':
    biz_dest = open('../../Downloads/hackathon/biz_name_review.txt', 'w')
    get_biz_name_review('../../Downloads/dataset/business.json', biz_dest)
