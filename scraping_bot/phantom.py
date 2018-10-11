from selenium import webdriver
from django.conf import settings
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
# driver.get('http://stackoverflow.com/')
#
# cookies = driver.get_cookies()
#
# driver.delete_all_cookies()
#
# for cookie in cookies :
#     driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry')})


# # You can save the current cookies as a python object using pickle. For example:
#
# import pickle
# import selenium.webdriver
#
# driver = selenium.webdriver.Firefox()
# driver.get("http://www.google.com")
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
#
# # and later to add them back:
#
# import pickle
# import selenium.webdriver
#
# driver = selenium.webdriver.Firefox()
# driver.get("http://www.google.com")
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)


def get_driver():
    ROOT_DIR = '/Users/snowsaturday/PycharmProjects/StudioDoctor_project/'
    PHANTOM_PATH = '{}/scraping_bot/phantomjs-2.1.1-macosx/bin/phantomjs'.format(ROOT_DIR)
    #CERTIFICATE = None
    SERVICE_ARGS = [
        # '--proxy=IP:PORT',
        # '--proxy-auth=LOGIN:PASSWORD',
        # '--proxy-type=HTTP',
        # '--load-images=False'
        '--webdriver-logfile=scraper.log',
        '--webdriver-loglevel=DEBUG',
        # '--ssl-client-certificate-file={}'.format(CERTIFICATE),
        # '--ignore-ssl-errors=True',
        # '--ssl-protocol=any'
        # '--web-security=False',
    ]
    DCAP = dict(DesiredCapabilities.PHANTOMJS)
    DCAP['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
    )

    driver = webdriver.PhantomJS(executable_path=PHANTOM_PATH,
                                 service_args=SERVICE_ARGS,
                                 desired_capabilities=DCAP
                                 )
    driver.set_window_size(1366, 768)
    return driver
