import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://slack.com/apps/'
CATEGORY_URL = BASE_URL + 'category/'


def get_application(slug):
    soup = get_soup(BASE_URL + slug)
    application = parse_application(soup)
    application['slack_id'] = slug.split('-')[0]
    application['slug'] = slug
    application['url'] = BASE_URL + slug
    return application


def get_applications(slug, page):
    soup = get_soup(CATEGORY_URL + slug + '?page=' + str(page))
    list_items = soup.find_all('li', class_='app_row interactive')
    return list(map(parse_application_list_item, list_items))


def get_categories():
    soup = get_soup(BASE_URL)
    links = soup.find_all('a', class_='sidebar_menu_list_item')
    return list(map(parse_category_link, links))


def get_category(slug):
    soup = get_soup(CATEGORY_URL + slug)
    category = parse_category(soup)
    category['slack_id'] = slug.split('-')[0]
    category['slug'] = slug
    category['url'] = CATEGORY_URL + slug
    return category


def get_soup(url):
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')


def parse_application_list_item(soup):
    slug = soup.a.get('href').split('/')[2]
    return {
        'avatar': soup.a.img.get('src'),
        'is_slack_owned': soup.get('data-app-is-slack-owned') == 'True',
        'name': soup.find('span', class_='media_list_title').get_text(),
        'position': int(soup.get('data-position')),
        'short_description': soup.find('span', class_='media_list_subtitle').get_text(),
        'slack_id': soup.get('data-app-id'),
        'slug': slug,
        'url': BASE_URL + slug,
    }


def parse_application(soup):
    def get_categories(soup):
        container = soup.find('div', class_='top_margin hide_on_mobile')
        links = container.find_all('a', class_='tag')
        return list(map(parse_category_link, links))

    def get_screenshots(soup):
        containers = soup.find_all('div', class_='p-screenshots')
        return list(map(lambda e: e.img.get('src'), containers))

    return {
        'avatar': soup.find('img', class_='large_app_icon').get('src'),
        'categories': get_categories(soup),
        'description': soup.find('div', class_='p-app_description').div.div.get_text(),
        'help_url': soup.find(id='action_app_support').get('href'),
        'name': soup.find('h2', class_='large app_name').get_text(),
        'privacy_policy_url': soup.find(id='action_app_privacy').get('href'),
        'screenshots': get_screenshots(soup),
        'short_description': soup.find('meta', attrs={'name': 'description'}).get('content'),
    }


def parse_category_link(soup):
    slug = soup.get('href').split('/')[3]
    return {
        'name': soup.get_text().strip(),
        'slack_id': slug.split('-')[0],
        'slug': slug,
        'url': CATEGORY_URL + slug,
    }


def parse_category(soup):
    def get_description(soup):
        container = soup.find('div', class_='description_container')
        return container.p.text if container else None

    return {
        'description': get_description(soup),
        'name': soup.find('h1', class_='page_title_text').get_text(),
    }
