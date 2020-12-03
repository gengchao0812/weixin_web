import pytest
from selenium import webdriver
import random

class BasePage():
    
    driver=webdriver.Chrome()
    
    def get_data_value(self):
        data_value=['2001','2002','2003','2004','2005','2006']
        n=random.randint(0,5)
        return data_value[n]


