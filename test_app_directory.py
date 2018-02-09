from bs4 import BeautifulSoup
import requests
import responses
import unittest

import app_directory


class GetCategoriesTest(unittest.TestCase):

    @responses.activate
    def test_it_returns_a_list_of_categories(self):
        with open('index.html', 'r') as f:
            body = f.read()
        responses.add(responses.GET, app_directory.BASE_URL, body=body)

        categories = app_directory.get_categories()

        self.assertEqual(len(categories), 25)
        self.assertEqual(categories[0]['name'], 'Featured')
        self.assertEqual(categories[0]['slack_id'], 'At0EFWTR6D')
        self.assertEqual(categories[0]['slug'], 'At0EFWTR6D-featured')
        self.assertEqual(categories[0]['url'], 'https://slack.com/apps/category/At0EFWTR6D-featured')


class GetCategoryTest(unittest.TestCase):

    @responses.activate
    def test_it_returns_a_category(self):
        url = app_directory.CATEGORY_URL + 'At0EFWTR6D-featured'
        with open('At0EFWTR6D-featured.html', 'r') as f:
            body = f.read()
        responses.add(responses.GET, url, body=body)

        category = app_directory.get_category('At0EFWTR6D-featured')

        self.assertEqual(category['description'], None)
        self.assertEqual(category['name'], 'Featured')
        self.assertEqual(category['slack_id'], 'At0EFWTR6D')
        self.assertEqual(category['slug'], 'At0EFWTR6D-featured')
        self.assertEqual(category['url'], 'https://slack.com/apps/category/At0EFWTR6D-featured')


class GetApplicationsTest(unittest.TestCase):

    @responses.activate
    def test_it_returns_a_list_of_applications(self):
        url = app_directory.CATEGORY_URL + 'At0EFWTR6D-featured'
        with open('At0EFWTR6D-featured.html', 'r') as f:
            body = f.read()
        responses.add(responses.GET, url, body=body)

        applications = app_directory.get_applications('At0EFWTR6D-featured', 1)

        self.assertEqual(len(applications), 12)
        self.assertEqual(applications[0]['avatar'], 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2016-05-03/39674680625_65ad135f72eff91b6ddf_96.jpg')
        self.assertFalse(applications[0]['is_slack_owned'])
        self.assertEqual(applications[0]['name'], '@must-read')
        self.assertEqual(applications[0]['position'], 1)
        self.assertEqual(applications[0]['short_description'], 'Controllable must-read lists for your team in Slack ð\x9f\x93\x95ð\x9f\x93\x97ð\x9f\x93\x98')
        self.assertEqual(applications[0]['slack_id'], 'A15KDN02Y')
        self.assertEqual(applications[0]['slug'], 'A15KDN02Y-must-read')
        self.assertEqual(applications[0]['url'], 'https://slack.com/apps/A15KDN02Y-must-read')


class GetApplicationTest(unittest.TestCase):

    @responses.activate
    def test_it_returns_an_application(self):
        url = app_directory.BASE_URL + 'A15KDN02Y-must-read'
        with open('A15KDN02Y-must-read.html', 'r') as f:
            body = f.read()
        responses.add(responses.GET, url, body=body)

        application = app_directory.get_application('A15KDN02Y-must-read')

        self.assertEqual(application['avatar'], 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2016-05-03/39674680625_65ad135f72eff91b6ddf_512.jpg')
        self.assertEqual(len(application['categories']), 4)
        self.assertTrue(len(application['description']) > 0)
        self.assertEqual(application['help_url'], 'https://finalem.com/must-read/help?utm_source=slack.com&utm_medium=special&utm_campaign=apps')
        self.assertEqual(application['name'], '@must-read')
        self.assertEqual(application['privacy_policy_url'], 'https://finalem.com/must-read/privacy-policy?utm_source=slack.com&utm_medium=special&utm_campaign=apps')
        self.assertEqual(len(application['screenshots']), 6)
        self.assertEqual(application['short_description'], 'Controllable must-read lists for your team in Slack ð\x9f\x93\x95ð\x9f\x93\x97ð\x9f\x93\x98')
        self.assertEqual(application['slug'], 'A15KDN02Y-must-read')
        self.assertEqual(application['url'], 'https://slack.com/apps/A15KDN02Y-must-read')


class GetSoupTest(unittest.TestCase):

    @responses.activate
    def test_it_returns_an_instance_of_beautiful_soup(self):
        with open('index.html', 'r') as f:
            body = f.read()
        responses.add(responses.GET, app_directory.BASE_URL, body=body)

        soup = app_directory.get_soup(app_directory.BASE_URL)

        self.assertIsInstance(soup, BeautifulSoup)

    @responses.activate
    def test_it_raises_an_exception_when_response_is_not_ok(self):
        responses.add(responses.GET, app_directory.BASE_URL, status=404)

        with self.assertRaises(requests.exceptions.HTTPError):
            app_directory.get_soup(app_directory.BASE_URL)


if __name__ == '__main__':
    unittest.main()
