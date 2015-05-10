import sys
import urllib2
from sgmllib import SGMLParser

class DeveloperList(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_div = ""
		self.name = []
		self.is_a = ""
		self.div_counter = 0
		self.a_counter = 0

	def start_div(self, attrs):
		for k, v in attrs:
			if k == 'class' and v == 'repo':
				self.is_div = 1
				self.div_counter += 1
				self.a_counter = 0

	def end_div(self):
		self.is_div = ""

	def start_a(self, attrs):
		self.is_a = 1
		self.a_counter += 1

	def end_a(self):
		self.is_a = ""

	def handle_data(self, text):
		if self.div_counter == 1:
			return
		if self.a_counter == 2:
			return
		if self.is_div == 1 and self.is_a == 1:
			self.name.append(text)

class ProfileDetails(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_li = ""
		self.name = ""
		self.is_li = ""

	def start_li(self, attrs):
		for k, v in attrs:
			if k == 'itemprop' and v == 'worksFor':
				self.is_li = 1

	def end_li(self):
		self.is_li = ""

	def handle_data(self, text):
		if self.is_li == 1:
			self.name = text

def process_org_name(pre_org_name):
        pre_org_name = pre_org_name.lower()

        index = pre_org_name.find(',')
        if index != -1:
        	return pre_org_name[0:index].strip()

        index = pre_org_name.find('-')
        if index != -1:
        	return pre_org_name[0:index].strip()
        		
        index = pre_org_name.find(' inc')
        if index != -1:
        	return pre_org_name[0:index].strip()

        return pre_org_name.strip()

org_list = {'unknown':0}

#eg. https://github.com/GoogleCloudPlatform/kubernetes
developers_content = urllib2.urlopen(sys.argv[1].rstrip('/') + '/network/members').read()
developer_list = DeveloperList()
developer_list.feed(developers_content)
for item in developer_list.name:
	profile_url = "https://github.com/" + item
	developer_profile_content = urllib2.urlopen(profile_url).read()
	developer_profile = ProfileDetails()
	developer_profile.feed(developer_profile_content)

	print item

	if developer_profile.name == '':
		developer_profile.name = 'unknown'
	
	org_name = process_org_name(developer_profile.name)

	if org_name not in org_list:
		org_list[org_name] = 1
	else:
		org_list[org_name] += 1

f1 = open('result.csv','w')
for (k, v) in org_list.items():
        f1.write(k + "," + str(v) + "\n")
f1.close()