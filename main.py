#python web scraping - this code can extract Python related jobs from 'TimesJobs' site every 10mins , can add skills filter


import requests
from bs4 import BeautifulSoup
import time
# with open('home.html', 'r') as html_file:
#     content = html_file.read()
   
#     soup = BeautifulSoup()
# URL ='https://www.flipkart.com//'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# #print(soup.prettify())
# html_tags= soup.find_all('span', class_ = 'VU-ZEz')
# print(html_tags)

#bring jobs related to python recent  
print('Put skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        pub_date = job.find('span', class_ ='sim-posted').text.replace(' ', '')
        if 'few' in pub_date:
            comp_name= job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company name : {comp_name.strip()} \n")
                    f.write(f"required skills : {skills.strip()} \n")
                    f.write(f'more infor: {more_info} \n')
                    f.write('')
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes')
        time.sleep(time_wait*60)
                