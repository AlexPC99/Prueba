import time
import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from fpdf import FPDF

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/mch/Documents/GitHub/Prueba/chromedriver')
driver.get("https://www.pressreader.com/mexico/el-universal/20211103/page/1/textview")
