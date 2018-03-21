import bs4 as bs
import urllib.request
import pymysql
sauce = urllib.request.urlopen("Enter the link here").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

connection = pymysql.connect(host='localhost', user='root', passwd='yourpassword', db='crsbis', use_unicode=True, charset="utf8")
cursor = connection.cursor();


# print(soup.td)

# for paragraph in soup.find_all('p'):
# 	print(paragraph.text)

# for url in soup.find_all('a'):
# 	print(url.get('href'))


# table = soup.find('table')	#same as table=soup.table
# print(table.find_all('tr'))

# for row in table.find_all('tr'):
# 	print(row.text)

table = soup.table
table_rows = table.find_all('tr')

i=0
for tr in table_rows:
	i = i+1
	td = tr.find_all('td')

	row = [i.text for i in td]

	if i>2 and len(row)==14:
		# print("===========================================================================================================")
		# print(row[5], "\n")
		sql = ('insert into products(registration_number, application_id, brand_name, organization, manufacturing_unit_address, country, product_category, indian_standard, models, reg_date, surveillance_status, status, remarks) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13] ))
		cursor.execute(sql)
		# print("INSERTED")
	else:
		print("FAILED", "\n")


connection.commit()
print("DATA INSERTED SUCCESSFULLY")
print(i)