from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import random 

def scrape(type_question):
    sourceUrl = 'https://www.codechef.com/problems/'+type_question
    try:
        browser = webdriver.PhantomJS(executable_path = '../phantomjs/bin/phantomjs')
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
    print(total)
    print(index)
    j=0
    for row in rows:
        if(j==index):
            print("MATCH ",j)
            tds=row.find_all('td')
            problem=[]
            problem.append(type_question)
            i=0
            for td in tds:
                if(i==0):
                    name = td.find('div',class_='problemname')
                    a = name.find('a')
                    url = a.get('href')
                    url = 'https://www.codechef.com'+url
                    name = a.text
                    print(name)
                    print(url)
                    problem.append(name)
                    problem.append(url)
                if(i==1):
                    code = td.find('a')
                    url = code.get('href')
                    code = code.text
                    url = 'https://www.codechef.com'+url
                    print(url)
                    print(code)
                    problem.append(code)
                    problem.append(url)
                if(i==2):
                    submissions = td.find('div')
                    submissions = submissions.text
                    print(submissions)
                    problem.append(submissions)
                if(i==3):
                    accuracy = td.find('a')
                    url = accuracy.get('href')
                    url = 'https://www.codechef.com'+url
                    accuracy = accuracy.text
                    print(url)
                    print(accuracy)
                    problem.append(url)
                    problem.append(accuracy)
                i+=1
        j+=1 
            # problem.append()

if __name__ == "__main__":
    type_no=random.choice([1, 2, 3, 4])
    type_question = 'school'
    if(type_no==2):
        type_question = 'easy'
    if(type_no==3):
        type_question = 'medium'
    if(type_no==4):
        type_question = 'hard'
    scrape(type_question)
