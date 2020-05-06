from splinter import Browser

def before_all(context):
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.browser = Browser('chrome', options=chrome_options)

def after_all(context):
    context.browser.quit()
    context.browser = None