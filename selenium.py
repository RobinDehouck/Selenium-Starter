from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# STARTING CODE FOR SELENIUM WEB SCRAPPING

if __name__ == "__main__":

	url = 'ENTER URL'
	options = uc.ChromeOptions()
	options.add_argument("--no-sandbox --no-first-run --no-service-autorun --password-store=basic")
	options.headless = True

	driver = uc.Chrome(options=options, version_main=96)
	driver.get(url)

	list_of_elements = driver.find_elements_by_xpath("ELEMENTS") 
	# Use find_element_by_xpath for one particular element
	
	for ad in list_of_elements:
		print(ad.text,'\n\n')
