import time
import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from fpdf import FPDF

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.pressreader.com/mexico/el-universal/20211103/page/1/textview")
