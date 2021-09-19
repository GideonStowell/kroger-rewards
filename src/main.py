from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

from selenium.webdriver.chrome.options import Options

#####
#CONFIG  DATA
#Some dummy data for not - TODO read these from a config file
receipt_date = "09/18/2021"
receipt_time = "17:52"
receipt_id = "706-244-171-276-511-682"
rewards_phone_number = os.environ.get('phone_number')


options = Options()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome('./chromedriver', options=options)

driver.get("http://krogerfeedback.com")
print(driver.title)


#Index_VisitDateDatePicker
date = driver.find_element_by_name("Index_VisitDateDatePicker")
driver.execute_script("arguments[0].removeAttribute('readonly','readonly')",date)
date.send_keys("09/17/2021")

#Convert military time to meridian
hours    = receipt_time[:2]
minutes  = receipt_time[3:]
meridian = "AM" if int(hours) < 12 else "PM"

#InputHour
input_hour = driver.find_element_by_name("InputHour")
input_hour.send_keys(hours)

#InputMinute
input_minutes = driver.find_element_by_name("InputMinute")
input_minutes.send_keys(minutes)

#InputMeridian
input_meridian = driver.find_element_by_name("InputMeridian")
input_meridian.send_keys(meridian)
#
# Split the ID number into a list
receipt_numbers = receipt_id.split("-")
input_names = ["CN1", "CN2", "CN3", "CN4", "CN5", "CN6"]
print(receipt_numbers)
zip_object = zip(input_names, receipt_numbers)
for name, value in zip_object:
    inp = driver.find_element_by_name(name)
    inp.send_keys(value)

#Click the Next Button
button = driver.find_element_by_name("NextButton")
button.click()

time.sleep(10)

driver.close()
