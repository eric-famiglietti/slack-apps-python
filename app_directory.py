import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://slack.com/apps/'
CATEGORY_URL = BASE_URL + 'category/'

def parse_category_link(soup):
    slug = soup.get('href').split('/')[3]
    return {
        'name': soup.get_text().strip(),
        'slack_id': slug.split('-')[0],
        'slug': slug,
        'url': CATEGORY_URL + slug,
    }

def get_categories():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('a', class_='sidebar_menu_list_item')
    return list(map(parse_category_link, elements))

def get_category(slug):
    url = CATEGORY_URL + slug
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    def parse_description(soup):
        element = soup.find('div', class_='description_container')
        if element:
            return element.p.text
        return None
    return {
        'description': parse_description(soup),
        'name': soup.find('h1', class_='page_title_text').get_text(),
        'slack_id': slug.split('-')[0],
        'slug': slug,
        'url': url,
    }

def get_applications(slug, page):
    url = CATEGORY_URL + slug + '?page=' + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    applications = []
    elements = soup.find_all('li', class_='app_row interactive')
    for element in elements:
        applications.append({
            'avatar': element.a.img.get('src'),
            'is_slack_owned': element.get('data-app-is-slack-owned'),
            'name': element.find('span', class_='media_list_title').get_text(),
            'position': element.get('data-position'),
            'short_description': element.find('span', class_='media_list_subtitle').get_text(),
            'slack_id': element.get('data-app-id'),
            'slug': element.a.get('href').split('/')[2],
            'url': BASE_URL + element.a.get('href').split('/')[2],
        })
    return applications

def get_application(slug):
    url = BASE_URL + slug
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    def parse_categories(soup):
        elements = soup.find_all('a', class_='tag')
        return list(map(parse_category_link, elements))
    def parse_screenshots(soup):
        screenshots = []
        elements = soup.find_all('div', class_='p-screenshots')
        for element in elements:
            screenshots.append(element.img.get('src'))
        return screenshots
    return {
        'avatar': soup.find('img', class_='large_app_icon').get('src'),
        'categories': parse_categories(soup),
        'description': soup.find('div', class_='p-app_description').div.div.get_text(),
        'help_url': soup.find(id='action_app_support').get('href'),
        'name': soup.find('h2', class_='large app_name').get_text(),
        'privacy_policy_url': soup.find(id='action_app_privacy').get('href'),
        'screenshots': parse_screenshots(soup),
        'short_description': soup.find('meta', attrs={'name': 'description'}).get('content'),
        'slug': slug,
        'url': url,
    }
