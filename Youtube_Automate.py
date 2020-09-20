# install chocolatey
# install selenium
# install chromedriver


from selenium import webdriver

#Open Chrome Browser and youtube
driver = webdriver.Chrome()
driver.get('https://youtube.com')


#Find the search bar and type in Hello World
searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
driver.implicitly_wait(2)
searchbox.send_keys('Hello World')


#Find the search button and click it
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
