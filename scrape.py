from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
driver = webdriver.Chrome()
driver.set_window_size(800, 600)

# /////////////////<=== Variable Defination ===>///////////////////////

img_srcs_list = []
card_title_list = []
price_list = []
location_list = []
date_list = []
duration_list = []
inner_content_list = []
content_url_list = []
content_list = []
img_srcs_list_res = []
card_title_list_res = []
price_list_res = []
location_list_res = []
date_list_res = []
duration_list_res = []
content_url_list_res = []
inner_imgurls_list = []
urls_list = []
inner_img_urls = []
all_data = []
res1 = []
res2 = []
res3 = []
res4 = []
content_data_res = []
content_data_res1 = []
content_data_res2 = []
content_data_res3 = []
img_urls = []
inner_content_res1 = []
inner_content_res2 = []
inner_content_res3 = []
data = {	
            'img_src' : "",
            'card_title' : "",
            'per_person_from_price' : "",
            'location' : "",
            'date' : "",
            'duration' : "",
            'content_data1': "",
            'content_data2': "",
            'content_data3': "",
            'img_urls':"",
		}

# //////////////// <==== Function Define ====> ////////////////////

def openPage(url):
	driver.get(url)

def exitDrive():
	driver.quit()

def print_csv(out_data):
    card_info = pd.DataFrame(out_data,columns=['img_src','card_title','per_person_from_price','location','date','duration','content_data1','content_data2','content_data3','img_urls'])
    card_info.to_csv('result.csv')

def getImageSrcFromElementByClass(domclass):
    img_srcs = driver.find_elements_by_class_name(domclass)
    for i in range(len(img_srcs)):
        img_srcs_list.append(img_srcs[i].get_attribute('src'))
    return img_srcs_list

def getCardTitleFromElementByClass(domclass):
    card_title = driver.find_elements_by_class_name(domclass)
    for i in range(len(card_title)):
        card_title_list.append(card_title[i].text)
    return card_title_list

def getPriceFromElementByClass(domclass):
    price = driver.find_elements_by_class_name(domclass)
    for i in range(len(price)):
        price_list.append(price[i].text)
    return price_list

def getLocationFromElementByClass(domclass):
    location = driver.find_elements_by_class_name(domclass)
    for i in range(len(location)):
        location_list.append(location[i].text)
    return location_list

def getDateFromElementByClass(domclass):
    date = driver.find_elements_by_class_name(domclass)
    for i in range(len(date)):
        date_list.append(date[i].text)
    return date_list

def getDurationFromElementByClass(domclass):
    duration = driver.find_elements_by_class_name(domclass)
    for i in range(len(duration)):
        duration_list.append(duration[i].text)
    return duration_list

def getInnerContentUrlFromElementByClass(domclass):
    content = driver.find_elements_by_class_name(domclass)
    for i in range(len(content)):
        content_url_list.append(content[i].get_attribute('href'))
    return content_url_list

def getInnerContent1FromElementByClass(domclass):
    inner_content1 = driver.find_elements_by_class_name(domclass)
    inner_content_res1 = inner_content1[0].text
    return inner_content_res1

def getInnerContent2FromElementByID(domclass):
    inner_content2 = driver.find_elements_by_id(domclass)
    inner_content_res2 = inner_content2[0].text
    return inner_content_res2

def getInnerContent3FromElementByID(domclass):
    inner_content3 = driver.find_elements_by_id(domclass)
    inner_content_res3 = inner_content3[0].text
    return inner_content_res3

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1

def getInnerImagUrlsFromElementByClass(domclass):
    inner_content = driver.find_elements_by_class_name(domclass)
    for i in range(len(inner_content)):
        inner_img_urls.append(inner_content[i].get_attribute('src'))
    return listToString(inner_img_urls)

def getContentDataFromElementByContentUrls(content_url_list_res):
    for i in range(len(content_url_list_res)):
        openPage(content_url_list_res[i])
        res1 = getInnerContent1FromElementByClass('m-offer-description__text')
        res2 = getInnerContent2FromElementByID('sect1')
        res3 = getInnerContent3FromElementByID('sect2')
        res4 = getInnerImagUrlsFromElementByClass('m-impressions__image')
        all_data.append(res1)
        all_data.append(res2)
        all_data.append(res3)
        all_data.append(res4)
    return all_data

def scrap_events():
    
    img_srcs_list_res = getImageSrcFromElementByClass("js-offer-card-image")
    card_title_list_res = getCardTitleFromElementByClass("js-offer-card-title")
    price_list_res = getPriceFromElementByClass("js-offer-price")
    location_list_res = getLocationFromElementByClass("js-offer-location")
    date_list_res = getDateFromElementByClass("js-offer-date")
    duration_list_res = getDurationFromElementByClass("js-offer-duration")
    content_url_list_res = getInnerContentUrlFromElementByClass("js-offer-button")
    content_data_res = getContentDataFromElementByContentUrls(content_url_list_res)

    
    content_data_res1 = content_data_res[0]
    content_data_res2 = content_data_res[1]
    content_data_res3 = content_data_res[2]
    img_urls = content_data_res[3]

    data = { 	
                'img_src' : img_srcs_list_res,
                'card_title' : card_title_list_res,
				'per_person_from_price' : price_list_res,
				'location' : location_list_res,
				'date' : date_list_res,
				'duration' : duration_list_res,
                'content_data1': content_data_res1,
                'content_data2': content_data_res2,
                'content_data3': content_data_res3,
                'img_urls': img_urls,
			}
    return data

# ////////////////<===Run Scrapping===>//////////////////////

openPage('https://www.bikecamp365.com/offers')
print_csv(scrap_events())
exitDrive()
