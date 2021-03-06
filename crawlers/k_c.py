import re
import ssl
import tempfile
import threading
import time
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.files.base import ContentFile, File
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from findit.models import Products

ssl._create_default_https_context = ssl._create_unverified_context

folder = 'konga/'

def konga_crawler():
	# konga_shirts()
	# konga_televisions()
	# konga_men_watches()
	# konga_womens_watches()
	konga_phones()


def konga_gaming():
		# https://www.konga.com/playstation-4
	for urls in range(1,2):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
				'Accept-Encoding': 'none',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection': 'keep-alive'}
		html = Request('https://www.konga.com/playstation-4?page=%s'%urls,headers=hdr)
		htmll = urlopen(html).read()
		print(html)
		bsObj = BeautifulSoup(htmll,'html.parser')
		product_list = bsObj.findAll('div',{'class':'product-block'})
		for product in product_list:
			product_name = product.find('div',{'class':'product-name'})
			product_link = 'https://www.konga.com'+product.a.attrs['href']
			images = product.img.attrs['src']
			request = requests.get(images, stream=True)

			if product.find('div',{'class':'special-price'}) != None:
				# If it does exist it find the price
				price = product.find('div',{'class':'special-price'})
			else:
				# If does not exist it finds the original price
				price = product.find('div',{'class':'original-price'})
			e_price = bytes(str(price.text),'UTF-8')
			e_price = e_price.decode('ascii','ignore')
			namelst = bytes(str(product_name.text), 'UTF-8')
			namelst = namelst.decode('ascii','ignore').replace('\n','')
			namelst = str(namelst)
			if Products.objects.filter(name=namelst,shop='konga').exists():
				
				produc = Products.objects.get(name=namelst,shop='konga')
				# Checks the price
				if produc.price != e_price:
					produc.old_price = produc.price
					produc.source_url = product_link
					produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
					# Updates the price
					produc.price = e_price
					# Saves the price
					
					produc.save()
			else:
				request = requests.get(images, stream=True)
				if request.status_code != requests.codes.ok:
					continue
				randd_ne = get_random_string(length=10)
				file_name = folder + images.split('/')[-1]
				point_finder = file_name.find('.')
				file_name = file_name[:point_finder] + randd_ne
				lf = tempfile.NamedTemporaryFile()
				for block in request.iter_content(1024*8):
					if not block:
						break
					lf.write(block)
				lf = ContentFile(httl)
				product = Products(name=namelst,price=e_price,source_url=product_link,genre='gaming',shop='konga')
				product.image.save(file_name[:20],File(lf))
		# subject = 'Crawler Error'
		# from_email = settings.EMAIL_HOST_USER
		# message = 'The following exception occured %s' % e        
		# recipient_list = ['johnsonoye34@gmail.com']
		# html_message = '<p>Bros there\'s something went wrong : %s konga crawler %s </p>'%(e,'gaming')
		# sent_mail = send_mail(
		#                 subject, 
		#                 message, 
		#                 from_email, 
		#                 recipient_list,  
		#                 html_message=html_message)
def konga_shirts():
	try:
		for urls in range(1,10):
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			       'Accept-Encoding': 'none',
			       'Accept-Language': 'en-US,en;q=0.8',
			       'Connection': 'keep-alive'}
			html = Request('https://www.konga.com/mens-shirts?page=%s'%urls,headers=hdr)
			htmll = urlopen(html).read()
			bsObj = BeautifulSoup(htmll,'html.parser')
			product_list = bsObj.findAll('div',{'class':'product-block'})
			for product in product_list:
				product_name = product.find('div',{'class':'product-name'})
				product_link = 'https://www.konga.com'+product.a.attrs['href']
				images = product.img.attrs['src']
				request = requests.get(images, stream=True)
				if product.find('div',{'class':'special-price'}) != None:
					# If it does exist it find the price
					price = product.find('div',{'class':'special-price'})
				else:
					# If does not exist it finds the original price
					price = product.find('div',{'class':'original-price'})
				e_price = bytes(str(price.text),'UTF-8')
				e_price = e_price.decode('ascii','ignore')
				namelst = bytes(str(product_name.text), 'UTF-8')
				namelst = namelst.decode('ascii','ignore').replace('\n','')
				namelst = str(namelst)
				if Products.objects.filter(name=namelst,shop='konga').exists():
					
					produc = Products.objects.get(name=namelst,shop='konga')
					# Checks the price
					if produc.price != e_price:
						produc.old_price = produc.price
						produc.source_url = product_link
						produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
						# Updates the price
						produc.price = e_price
						# Saves the price
						
						produc.save()
				else:
					request = requests.get(images, stream=True)
					if request.status_code != requests.codes.ok:
						continue
					randd_ne = get_random_string(length=10)
					file_name = folder + images.split('/')[-1]
					point_finder = file_name.find('.')
					file_name = file_name[:point_finder] + randd_ne
					lf = tempfile.NamedTemporaryFile()
					for block in request.iter_content(1024*8):
						if not block:
							break
						lf.write(block)
					lf = ContentFile(httl)
					product = Products(name=namelst,price=e_price,source_url=product_link,genre='shirts',shop='konga')
					product.image.save(file_name[:20],files.File(lf))

	except Exception as e:
		print(e)
		# subject = 'Crawler Error'
		# from_email = settings.EMAIL_HOST_USER
		# message = 'The following exception occured %s' % e        
		# recipient_list = ['johnsonoye34@gmail.com']
		# html_message = '<p>Bros there\'s something went wrong : %s konga crawler %s </p>'%(e,'shirts')
		# sent_mail = send_mail(
		#                 subject, 
		#                 message, 
		#                 from_email, 
		#                 recipient_list,  
		#                 html_message=html_message)

def konga_televisions():
	try:
		for urls in range(1,10):
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			       'Accept-Encoding': 'none',
			       'Accept-Language': 'en-US,en;q=0.8',
			       'Connection': 'keep-alive'}
			html = Request('https://www.konga.com/televisions?page=%s'%urls,headers=hdr)
			htmll = urlopen(html).read()
			bsObj = BeautifulSoup(htmll,'html.parser')
			product_list = bsObj.findAll('div',{'class':'product-block'})
			for product in product_list:
				product_name = product.find('div',{'class':'product-name'})
				product_link = 'https://www.konga.com'+product.a.attrs['href']
				images = product.img.attrs['src']
				request = requests.get(images, stream=True)
				if product.find('div',{'class':'special-price'}) != None:
					# If it does exist it find the price
					price = product.find('div',{'class':'special-price'})
				else:
					# If does not exist it finds the original price
					price = product.find('div',{'class':'original-price'})
				e_price = bytes(str(price.text),'UTF-8')
				e_price = e_price.decode('ascii','ignore')
				namelst = bytes(str(product_name.text), 'UTF-8')
				namelst = namelst.decode('ascii','ignore').replace('\n','')
				namelst = str(namelst)
				if Products.objects.filter(name=namelst,shop='konga').exists():
					
					produc = Products.objects.get(name=namelst,shop='konga')
					# Checks the price
					if produc.price != e_price:
						produc.old_price = produc.price
						produc.source_url = product_link
						produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
						# Updates the price
						produc.price = e_price
						# Saves the price
						
						produc.save()
				else:
					request = requests.get(images, stream=True)
					if request.status_code != requests.codes.ok:
						continue
					randd_ne = get_random_string(length=10)
					file_name = folder + images.split('/')[-1]
					point_finder = file_name.find('.')
					file_name = file_name[:point_finder] + randd_ne
					lf = tempfile.NamedTemporaryFile()
					for block in request.iter_content(1024*8):
						if not block:
							break
						lf.write(block)
					lf = ContentFile(httl)
					print(namelst,e_price)
					product = Products(name=namelst,price=e_price,source_url=product_link,genre='televisions',shop='konga')
					product.image.save(file_name[:20],files.File(lf))

	except Exception as e:
		print(e)
		# subject = 'Crawler Error'
		# from_email = settings.EMAIL_HOST_USER
		# message = 'The following exception occured %s' % e        
		# recipient_list = ['johnsonoye34@gmail.com']
		# html_message = '<p>Bros there\'s something went wrong : %s konga crawler %s</p>'%(e, 'televisions')
		# sent_mail = send_mail(
		#                 subject, 
		#                 message, 
		#                 from_email, 
		#                 recipient_list,  
		#                 html_message=html_message)

		
			# https://www.konga.com/catalogsearch/result/?category_id=5294&aggregated_brand=Apple
				#print(namelst,e_price,product_link)https://www.konga.com/ict-brookersfor urls in range(1,417):
def konga_phones():
	try:
		for urls in range(1,2):
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
					'Accept-Encoding': 'none',
					'Accept-Language': 'en-US,en;q=0.8',
					'Connection': 'keep-alive'}
			html = Request('https://www.konga.com/mobile-phones?page=%s'%urls,headers=hdr)
			htmll = urlopen(html).read()
			print(type(htmll))
			bsObj = BeautifulSoup(htmll,'html.parser')
			product_list = bsObj.findAll('div',{'class':'product-block'})
			print(product_list)
			for product in product_list:
				product_name = product.find('div',{'class':'product-name'})
				product_link = 'https://www.konga.com'+product.a.attrs['href']
				images = product.img.attrs['src']
				htl = Request(images,headers=hdr)
				httl = urlopen(htl).read()
				if product.find('div',{'class':'special-price'}) != None:
					# If it does exist it find the price
					price = product.find('div',{'class':'special-price'})
				else:
					# If does not exist it finds the original price
					price = product.find('div',{'class':'original-price'})
				e_price = bytes(str(price.text),'UTF-8')
				e_price = e_price.decode('ascii','ignore')
				namelst = bytes(str(product_name.text), 'UTF-8')
				namelst = namelst.decode('ascii','ignore').replace('\n','')
				namelst = str(namelst)
				if Products.objects.filter(name=namelst,shop='konga').exists():
					
					produc = Products.objects.get(name=namelst,shop='konga')
					# Checks the price
					if produc.price != e_price:
						produc.old_price = produc.price
						produc.source_url = product_link
						produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
						# Updates the price
						produc.price = e_price
						# Saves the price
						
						produc.save()
				else:
					request = requests.get(images, stream=True)
					if request.status_code != requests.codes.ok:
						continue
					randd_ne = get_random_string(length=10)
					file_name = folder + images.split('/')[-1]
					point_finder = file_name.find('.')
					file_name = file_name[:point_finder] + randd_ne
					lf = tempfile.NamedTemporaryFile()
					for block in request.iter_content(1024*8):
						if not block:
							break
						lf.write(block)
					lf = ContentFile(httl)
					product = Products(name=namelst,price=e_price,source_url=product_link,shop='konga',genre='phone')
					product.image.save(file_name[:20],File(lf))
				# https://www.konga.com/catalogsearch/result/?category_id=5294&aggregated_brand=Apple
					#print(namelst,e_price,product_link)https://www.konga.com/ict-brookers
	except Exception as e:
		print(e)
def konga_laptops():
	try:
		for urls in range(1,10):
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			       'Accept-Encoding': 'none',
			       'Accept-Language': 'en-US,en;q=0.8',
			       'Connection': 'keep-alive'}
			html = Request('https://www.konga.com/laptops-5230?page=%s'%urls,headers=hdr)
			htmll = urlopen(html).read()
			bsObj = BeautifulSoup(htmll,'html.parser')
			product_list = bsObj.findAll('div',{'class':'product-block'})
			for product in product_list:
				product_name = product.find('div',{'class':'product-name'})
				product_link = f'https://www.konga.com{product.a.attrs["href"]}'
				images = product.img.attrs['src']
				htl = Request(images,headers=hdr)
				httl = urlopen(htl).read()
				if product.find('div',{'class':'special-price'}) != None:
					# If it does exist it find the price
					price = product.find('div',{'class':'special-price'})
				else:
					# If does not exist it finds the original price
					price = product.find('div',{'class':'original-price'})
				e_price = bytes(str(price.text),'UTF-8')
				e_price = e_price.decode('ascii','ignore')
				namelst = bytes(str(product_name.text), 'UTF-8')
				namelst = namelst.decode('ascii','ignore').replace('\n','')
				namelst = str(namelst)
				print(namelst)
				if Products.objects.filter(name=namelst,shop='konga').exists():
					
					produc = Products.objects.get(name=namelst,shop='konga')
					# Checks the price
					if produc.price != e_price:
						produc.old_price = produc.price
						produc.source_url = product_link
						produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
						# Updates the price
						produc.price = e_price
						# Saves the price
						
						produc.save()
				else:
					request = requests.get(images, stream=True)
					if request.status_code != requests.codes.ok:
						continue
					randd_ne = get_random_string(length=10)
					file_name = folder + images.split('/')[-1]
					point_finder = file_name.find('.')
					file_name = file_name[:point_finder] + randd_ne
					lf = tempfile.NamedTemporaryFile()
					for block in request.iter_content(1024*8):
						if not block:
							break
						lf.write(block)
					lf = ContentFile(httl)
					product = Products(name=namelst,price=e_price,source_url=product_link,shop='konga',genre='laptops')
					product.image.save(file_name[:20],File(lf))

	except Exception as e:
		print(e)
		# subject = 'Crawler Error'
		# from_email = settings.EMAIL_HOST_USER
		# message = 'The following exception occured %s' % e        
		# recipient_list = ['johnsonoye34@gmail.com']
		# html_message = '<p>Bros there\'s something went wrong : %s konga crawler %s</p>'%(e, 'laptops')
		# sent_mail = send_mail(
		#                 subject, 
		#                 message, 
		#                 from_email, 
		#                 recipient_list,  
		#                 html_message=html_message)

		# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		# 	       'Accept-Encoding': 'none',
		# 	       'Accept-Language': 'en-US,en;q=0.8',
		# 	       'Connection': 'keep-alive'}
		# html = Request('https://www.konga.com/catalogsearch/result/?category_id=5294&aggregated_brand=Apple',headers=hdr)
		# htmll = urlopen(html).read()
		# bsObj = BeautifulSoup(htmll,'html.parser')
		# product_list = bsObj.findAll('div',{'class':'product-block'})
		# for product in product_list:
		# 	product_name = product.find('div',{'class':'product-name'})
		# 	product_link = 'https://www.konga.com'+product.a.attrs['href']
		# 	images = product.img.attrs['src']
		# 	request = requests.get(images, stream=True)
		# 	if product.find('div',{'class':'special-price'}) != None:
		# 		# If it does exist it find the price
		# 		price = product.find('div',{'class':'special-price'})
		# 	else:
		# 		# If does not exist it finds the original price
		# 		price = product.find('div',{'class':'original-price'})
		# 	e_price = bytes(str(price.text),'UTF-8')
		# 	e_price = e_price.decode('ascii','ignore')
		# 	namelst = bytes(str(product_name.text), 'UTF-8')
		# 	namelst = namelst.decode('ascii','ignore')
		# 	if Products.objects.filter(name=namelst,shop='konga').exists():
				
		# 		produc = Products.objects.get(name=namelst,shop='konga')
		# 		# Checks the price
		# 		if produc.price != e_price:
		# 			produc.old_price = produc.price
		# 			produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
		# 			# Updates the price
		# 			produc.price = e_price
		# 			# Saves the price
					
		# 			produc.save()
		# 	else:
		# 		if request.status_code != requests.codes.ok:
		# 			continue
		# 		file_name = folder + images.split('/')[-1]
		# 		lf = tempfile.NamedTemporaryFile()
		# 		for block in request.iter_content(1024*8):
		# 			if not block:
		# 				break
		# 			lf.write(block)
		# 		print(namelst,e_price)
		# 		product = Products(name=namelst,price=e_price,source_url=product_link,shop='konga')
		# 		product.image.save(file_name[:20],files.File(lf))

def konga_men_watches():
	try:
		for urls in range(1,60):
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			       'Accept-Encoding': 'none',
			       'Accept-Language': 'en-US,en;q=0.8',
			       'Connection': 'keep-alive'}
			html = Request('https://www.konga.com/mens-watches?page=%s'%urls,headers=hdr)
			htmll = urlopen(html).read()
			bsObj = BeautifulSoup(htmll,'html.parser')
			product_list = bsObj.findAll('div',{'class':'product-block'})
			for product in product_list:
				product_name = product.find('div',{'class':'product-name'})
				product_link = 'https://www.konga.com'+product.a.attrs['href']
				images = product.img.attrs['src']
				request = requests.get(images, stream=True)
				if product.find('div',{'class':'special-price'}) != None:
					# If it does exist it find the price
					price = product.find('div',{'class':'special-price'})
				else:
					# If does not exist it finds the original price
					price = product.find('div',{'class':'original-price'})
				e_price = bytes(str(price.text),'UTF-8')
				e_price = e_price.decode('ascii','ignore')
				namelst = bytes(str(product_name.text), 'UTF-8')
				namelst = namelst.decode('ascii','ignore').replace('\n','')
				namelst = str(namelst)
				print(namelst,e_price)
				if Products.objects.filter(name=namelst,shop='konga',genre='men-watches').exists():
					
					produc = Products.objects.get(name=namelst,shop='konga',genre='men-watches')
					# Checks the price
					if produc.price != e_price:
						produc.old_price = produc.price
						produc.source_url = product_link
						produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
						# Updates the price
						produc.price = e_price
						# Saves the price
						
						produc.save()
				else:
					request = requests.get(images, stream=True)
					if request.status_code != requests.codes.ok:
						continue
					randd_ne = get_random_string(length=10)
					file_name = folder + images.split('/')[-1]
					point_finder = file_name.find('.')
					file_name = file_name[:point_finder] + randd_ne
					lf = tempfile.NamedTemporaryFile()
					for block in request.iter_content(1024*8):
						if not block:
							break
						lf.write(block)
					lf = ContentFile(httl)
					product = Products(name=namelst,price=e_price,source_url=product_link,shop='konga',genre='men-watches')
					product.image.save(file_name[:20],files.File(lf))
	
	except Exception as e:
		print(e)
		# subject = 'Crawler Error'
		# from_email = settings.EMAIL_HOST_USER
		# message = 'The following exception occured %s' % e        
		# recipient_list = ['johnsonoye34@gmail.com']
		# html_message = '<p>Bros there\'s something went wrong : %s konga crawler %s</p>'%(e,'men-watches')
		# sent_mail = send_mail(
		#                 subject, 
		#                 message, 
		#                 from_email, 
		#                 recipient_list,  
		#                 html_message=html_message)

def konga_womens_watches():
	try:
		for urls in range(1,60):
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			       'Accept-Encoding': 'none',
			       'Accept-Language': 'en-US,en;q=0.8',
			       'Connection': 'keep-alive'}
			html = Request('https://www.konga.com/womens-watches?page=%s'%urls,headers=hdr)
			htmll = urlopen(html).read()
			bsObj = BeautifulSoup(htmll,'html.parser')
			product_list = bsObj.findAll('div',{'class':'product-block'})
			for product in product_list:
				product_name = product.find('div',{'class':'product-name'})
				product_link = 'https://www.konga.com'+product.a.attrs['href']
				images = product.img.attrs['src']
				request = requests.get(images, stream=True)
				if product.find('div',{'class':'special-price'}) != None:
					# If it does exist it find the price
					price = product.find('div',{'class':'special-price'})
				else:
					# If does not exist it finds the original price
					price = product.find('div',{'class':'original-price'})
				e_price = bytes(str(price.text),'UTF-8')
				e_price = e_price.decode('ascii','ignore')
				namelst = bytes(str(product_name.text), 'UTF-8')
				namelst = namelst.decode('ascii','ignore').replace('\n','')
				namelst = str(namelst)
				print(namelst,e_price)
				if Products.objects.filter(name=namelst,shop='konga',genre='women-watches').exists():
					
					produc = Products.objects.get(name=namelst,shop='konga',genre='women-watches')
					# Checks the price
					if produc.price != e_price:
						produc.old_price = produc.price
						produc.source_url = product_link
						produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
						# Updates the price
						produc.price = e_price
						# Saves the price
						
						produc.save()
				else:
					request = requests.get(images, stream=True)
					if request.status_code != requests.codes.ok:
						continue
					randd_ne = get_random_string(length=10)
					file_name = folder + images.split('/')[-1]
					point_finder = file_name.find('.')
					file_name = file_name[:point_finder] + randd_ne
					lf = tempfile.NamedTemporaryFile()
					for block in request.iter_content(1024*8):
						if not block:
							break
						lf.write(block)
					lf = ContentFile(httl)
					product = Products(name=namelst,price=e_price,source_url=product_link,shop='konga',genre='women-watches')
					product.image.save(file_name[:20],files.File(lf))

	except Exception as e:
		print(e)
		# subject = 'Crawler Error'
		# from_email = settings.EMAIL_HOST_USER
		# message = 'The following exception occured %s' % e        
		# recipient_list = ['johnsonoye34@gmail.com']
		# html_message = '<p>Bros there\'s something went wrong : %s konga crawler %s</p>'%(e,'women-watches')
		# sent_mail = send_mail(
		#                 subject, 
		#                 message, 
		#                 from_email, 
		#                 recipient_list,  
		#                 html_message=html_message)
