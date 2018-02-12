# slack-apps-python

[![Build Status](https://travis-ci.org/eric-famiglietti/slack-apps-python.svg?branch=master)](https://travis-ci.org/eric-famiglietti/slack-apps-python)

Python module for scraping the Slack App Directory.

## Requirements

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](http://docs.python-requests.org/en/master/)

## Usage

### Summary

- `get_categories()`
- `get_category(slug)`
- `get_applications(slug, page)`
- `get_application(slug)`

### Methods

#### `get_categories()`

Returns a list of dictionaries representing the categories in the Slack App Directory.

```py
>>> categories = get_categories()
>>> print(categories)
[
    {
        'name': 'Featured',
        'slack_id': 'At0EFWTR6D',
        'slug': 'At0EFWTR6D-featured',
        'url': 'https://slack.com/apps/category/At0EFWTR6D-featured'
    },
    ...
]
```

#### `get_category(slug)`

Returns a dictionary containing information for a single category. The category may have additional data such as a description.

```py
>>> category = get_category('At0MQP5BEF-bots')
>>> print(category)
{
    'description': 'Bots are like having a virtual team member — they can help you manage tasks, run your team standup, poll the office, and more!',
    'name': 'Bots',
    'slack_id': 'At0MQP5BEF',
    'slug': 'At0MQP5BEF-bots',
    'url': 'https://slack.com/apps/category/At0MQP5BEF-bots'
}
```

#### `get_applications(slug, page)`

Returns a list of dictionaries representing a single page of applications in a category.

```py
>>> applications = get_applications('At0EFWTR6D-featured', 1)
>>> print(applications)
[
    {
        'avatar': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2016-05-03/39674680625_65ad135f72eff91b6ddf_96.jpg',
        'is_slack_owned': False,
        'name': '@must-read',
        'position': 1,
        'short_description': 'Controllable must-read lists for your team in Slack 📕📗📘',
        'slack_id': 'A15KDN02Y',
        'slug': 'A15KDN02Y-must-read',
        'url': 'https://slack.com/apps/A15KDN02Y-must-read'
    },
    ...
]
```

#### `get_application(slug)`

Returns a dictionary containing information for a single application.

```py
>>> application = get_application('A15KDN02Y-must-read')
>>> print(application)
{
    'avatar': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2016-05-03/39674680625_65ad135f72eff91b6ddf_512.jpg',
    'categories': [
        {
            'name': 'Featured',
            'slack_id': 'At0EFWTR6D',
            'slug': 'At0EFWTR6D-featured',
            'url': 'https://slack.com/apps/category/At0EFWTR6D-featured'
        },
        ...
    ],
    'description': '@must-read transforms any important message into micro-task...',
    'help_url': 'https://finalem.com/must-read/help',
    'name': '@must-read',
    'privacy_policy_url': 'https://finalem.com/must-read/privacy-policy',
    'screenshots': [
        'https://s3-us-west-2.amazonaws.com/slack-files2/images/2017-07-20/216663485463_0196a3e4ff408839be40_1600.png',
        ...
    ],
    'short_description': 'Controllable must-read lists for your team in Slack 📕📗📘',
    'slug': 'A15KDN02Y-must-read',
    'url': 'https://slack.com/apps/A15KDN02Y-must-read'
}
```

## Testing

You can run the included unit tests using `python -m unittest`.
