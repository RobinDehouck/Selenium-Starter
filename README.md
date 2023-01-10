# Selenium Web Scraper

This is a simple Python script that uses Selenium to scrape a website.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This script requires the following Python packages to be installed:
- selenium
- undetected_chromedriver (v2)

You can install these packages using pip:
pip install selenium undetected_chromedriver


### Usage

To use the script, simply enter the URL of the website you want to scrape in the `url` variable and the xpath of the elements you want to retrieve in the `list_of_elements` variable.

url = 'ENTER URL'
list_of_elements = driver.find_elements_by_xpath("ELEMENTS")


You can run the script by executing:
python selenium_scraper.py

### Additional Information

This script uses Chrome in headless mode. Additional options have been added to avoid some known issue with Chrome headless.

### Note
The `undetected_chromedriver` package you are using is a web-driver to avoid browser fingerprinting, so it may be problematic while scraping high-security websites, if you are facing any issues you may want to consider other options.

Note that the script is just a sample and it is up to you to adapt it to your needs and to respect legal terms and regulation on web scraping, Respect the terms of use of the websites you scraping.
