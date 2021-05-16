from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

x = input('Введите название вакансии: ')

page = 0
domain = 'https://hh.ru'
params = {'clusters':'true',
          'area':'1',
          'enable_snippets': 'true',
          'st': 'searchVacancy',
          'text' : x,
          'page': page}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

response = requests.get(domain+'/search/vacancy',params=params, headers=headers)
dom = bs(response.text,'html.parser')
vacancies_list = dom.find_all('div', {'class' : 'vacancy-serp-item'})

find_pages = dom.find_all('a', {'data-qa' : 'pager-page'})
last_span = find_pages[-1].find('span').text
last_page = int(last_span)


all_vacancies = []
for i in range(last_page):
    for vac in vacancies_list:
        vac_title = vac.find('a', {'data-qa' : 'vacancy-serp__vacancy-title'}).text
        vac_link = vac.find('a', {'data-qa' : 'vacancy-serp__vacancy-title'})['href']
        salary = vac.find('span', {'data-qa':'vacancy-serp__vacancy-compensation'})
        if not salary:
            salary_min=None
            salary_max=None
        else:
            salary = salary.getText().replace('\u202f', '').split()
            if salary[0] == 'от':
                salary_min = int(salary[1])
                salary_max = None
            elif salary[0] == 'до':
                salary_min = None
                salary_max = int(salary[1])
            else:
                salary_min = int(salary[0])
                salary_max = int(salary[2])
        job_offer = [vac_title, vac_link, salary_min, salary_max]
        all_vacancies.append(job_offer)

    page += 1
    response = requests.get(domain + '/search/vacancy', params=params, headers=headers)
    dom = bs(response.text, 'html.parser')
    vacancies_list = dom.find_all('div', {'class': 'vacancy-serp-item'})

pprint(all_vacancies)
print(len(all_vacancies))
