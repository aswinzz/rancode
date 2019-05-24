from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import random 

def scrape(type_question):
    sourceUrl = 'https://www.codechef.com/problems/'+type_question
    try:
        browser = webdriver.PhantomJS(executable_path = 'scraper/phantomjs/bin/phantomjs')
    except:
        browser = webdriver.PhantomJS(executable_path = './phantomjs/bin/phantomjs')
    browser.get(sourceUrl)
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    main_div = soup.find('table',class_='dataTable')
    body = soup.find('tbody')
    rows = body.find_all('tr',class_='problemrow')
    total=len(rows)
    index=random.randint(0,total)
    problems=[]
    for row in rows:
        tds=row.find_all('td')
        i=0
        data={}
        data['type']=type_question
        if(type_question=="school"):
            data['type']="beginner"
        for td in tds:
            if(i==0):
                name = td.find('div',class_='problemname')
                a = name.find('a')
                url = a.get('href')
                url = 'https://www.codechef.com'+url
                name = a.text
                name=name.strip('\n')
                data['name']=name
                data['url']=url
            if(i==1):
                code = td.find('a')
                url = code.get('href')
                code = code.text
                url = 'https://www.codechef.com'+url
                data['code']=code
                data['submit_url']=url
            if(i==2):
                submissions = td.find('div')
                submissions = submissions.text
                data['submissions']=submissions
            if(i==3):
                accuracy = td.find('a')
                url = accuracy.get('href')
                url = 'https://www.codechef.com'+url
                accuracy = accuracy.text
                data['accuracy']=accuracy
                data['status']=url
                problems.append(data)
            i+=1
    return problems 

if __name__ == "__main__":
    type_no=random.choice([1, 2, 3, 4])
    type_question = 'school'
    if(type_no==2):
        type_question = 'easy'
    if(type_no==3):
        type_question = 'medium'
    if(type_no==4):
        type_question = 'hard'
    problems=scrape(type_question)
