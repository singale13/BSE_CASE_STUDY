
import traceback
import requests
from bs4 import BeautifulSoup
import pd_zip

def zip_file_operations():
	headers = {
		'Access-Control-Allow-Origin': '*',
    		'Access-Control-Allow-Methods': 'GET',
    		'Access-Control-Allow-Headers': 'Content-Type',
    		'Access-Control-Max-Age': '3600',
    		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    	}
	r = requests.get("https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx",headers=headers)

	soup = BeautifulSoup(r.content)
	#to print zip files links
	print("scrapping the latest Bse Zip File")
	count=0
	for anchor in soup.select('a'):
		if count == 0:
			if anchor.has_attr('href'):
				link=anchor['href']
				print("Latest bse zip link",link)
				count+=1

	#code to pass the latest zip file link to extract the zip file
	target_path = 'bse.zip'
	print("Downloading Zip File")
	response = requests.get(link,headers=headers)
	print(response)
	handle = open(target_path, "wb")
	for data in response.iter_content(chunk_size=1000):
    		if data:
        		handle.write(data)
        
	handle.close()

	#extract the zip file
	from zipfile import ZipFile
	print("Extracting Zip File")
	with ZipFile('bse.zip', 'r') as zipObj:
   	# Extract all the contents of zip file in current directory
   		zipObj.extractall()
   	
if __name__ == '__main__':
    # test1.py executed as script
    # do something
    zip_file_operations()
    pd_zip.db_operation()






