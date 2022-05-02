import facebook
import time
access_token = "EAACEdEose0cBADcfRkZByOClvtg04F3t15lBi9B45aAIPE3MpZBfM9nvy3IpZBDnvi8wcbUqTZCgpKBAD5n0Nhe16vwFVEYlfAbBZClrNwZC3PnAF9Xone7vNZCACJjqUGZAVK7tYYWOSToWVVbnYWWTNrYBF4yTlSaob2BHZCR1rqfZCq9sT1WYpW4gUGX2bHqrNzgL6xniKo4wZDZD"
graph = facebook.GraphAPI(access_token=access_token, version='2.10')
fb_page_dict = {}

with open('hackathon-uiowa-17/biz_name5.txt') as file:
	for line in file:
		#data = line.split('|')
		#print(data)
		#print(type(line.strip()))

		'''
		name = data[0].strip()
		city = data[1].strip()
		state = data[2].strip()
		print(name + " " + city + " " + state)
		'''
		name = line.strip()
		print(name)
		pages = graph.search(type='page', q=line)
		
		#print(pages)

		
		for page in pages['data']: 
			if page['name'] == name:
				if (name in fb_page_dict) and (fb_page_dict.get(name) == 1):
					break
				else:
					fb_page_dict[name] = 1
			else:
				if (name in fb_page_dict):
					if(fb_page_dict[name] == 1):
						break
				else:
					fb_page_dict[name] = 0
		time.sleep(2)
			

dest_file = open('hackathon-uiowa-17/business_fb_presence5.txt', 'w')

count=1
for key, value in fb_page_dict.items():
	#print('%s: %s'%(key, value))
	dest_file.write("|" + key + "|" + str(value) + "|\n")
	print("done line " + str(count))
	count += 1
dest_file.close()

	

'''
biz_name = ['Richmond Town Square', 'South Florida Style Chicken & Ribs', 'The Tea Emporium', 'TRUmatch', 'Blimpie', 'Boxter\'s Cigars', 'Back-Health Chiropractic', 'Auto Bathouser', 'JAB Jewelry Designs', 'Mark Zuckerberg', 'Steam']
for name in biz_name:
	pages = graph.search(type='page', q=name, )

	for page in pages['data']:
		if (page['name'] == name):
			print(page['name'])
			print(page['id'])

		#if user['data'] == name:
			#print(name)
			#print('%s %s' %(user['id'], user['name']))
'''