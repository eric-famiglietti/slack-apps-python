# slack-apps-python

Python module for scraping the Slack App Directory.

## Requirements

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](http://docs.python-requests.org/en/master/)

## Usage

```
# Get all categories
categories = get_categories()

# Get a single categories
category = get_category('At0EFWTR6D-featured')

# Get a page of applications
applications = get_applications('At0EFWTR6D-featured', 1)

# Get a single application
application = get_application('A15KDN02Y-must-read')
```
