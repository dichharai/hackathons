dest = open('ordered_fb_data.txt', 'w')

count = 0
ordered = open('first_1000_biz_name.txt', 'r')
unordered = open('unordered_fb_presence_data.txt', 'r')

ordered_lines = ordered.readlines()
unordered_lines = unordered.readlines()
for i in range(1000):
	oname = ordered_lines[i].strip()
	print(oname)
	for j in range(827):
		uname = unordered_lines[j].split('|')
		print(uname)
		name = uname[1].strip()
		presence = uname[2].strip()
		#print(oname == name)
		if(oname == name):
			#print("Found! " + name)
			dest.write(oname + "," + presence + "\n")
			count += 1
			break
print(count)


'''
with open('first_1000_ordered_test.txt') as of: 
	with open('business_fb_presence.txt') as uf:
		for ol in of: 
			o_name = ol.strip()
			print("o_name " + o_name)
			for ul in uf:
				data = ul.split("|")
				name = data[1].strip()

				presence = data[2].strip()
				print(name )
				if(o_name == name):
					print('ordered ' + name)
					
			
			count += 1

print("Total " + str(count))
'''