from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
load_dotenv()

from selenium.webdriver.chrome.options import Options


def NextButton():
    button = driver.find_element_by_id("NextButton")
    button.click()


#####
#CONFIG  DATA
#Some dummy data for not - TODO read these from a config file
receipt_date = os.environ.get("receipt_date")
print('Loaded receipt_date: ', receipt_date)
receipt_time = os.environ.get("receipt_time")
print('Loaded receipt_time: ', receipt_time)
receipt_id   = os.environ.get("receipt_id")
print('Loaded receipt_id: ', receipt_id)
rewards_phone_number = os.environ.get('phone_number')
print('Loaded phone_number: ', rewards_phone_number)


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--headless")

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

#Arrived at the first page (Overall satisfaction)
element = driver.find_element_by_xpath('//*[@id="FNSR331002"]/td[1]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Describe why highly satisfied, just click next
#Click the Next Button
button = driver.find_element_by_id("NextButton")
button.click()

#Choose highly satisfied on a bunch of things - can I get them all as a group
opts = driver.find_elements_by_class_name("Opt5")
print("Got this many: ", len(opts))
for x in opts:
    time.sleep(1)
    x.send_keys(Keys.SPACE)

button = driver.find_element_by_id("NextButton")
button.click()
#Skip optional multiselect question
button = driver.find_element_by_id("NextButton")
button.click()

#Did you require assistance from an employee (choose) I did not require assistance
element = driver.find_element_by_xpath('//*[@id="FNSR120001"]/td[3]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Did you have a problem, choose no
element = driver.find_element_by_xpath('//*[@id="FNSR113000"]/td[2]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Recognize an employee, choose no
element = driver.find_element_by_xpath('//*[@id="FNSR050001"]/td[2]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Will you return?
element = driver.find_element_by_xpath('//*[@id="FNSR115001"]/td[1]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Scale of 1-10
element = driver.find_element_by_xpath('//*[@id="FNSR115004"]/td[1]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Skip optional question

button = driver.find_element_by_id("NextButton")
button.click()

#Recommendto a friend
element = driver.find_element_by_xpath('//*[@id="FNSR128008"]/td[1]/span')
element.click()

button = driver.find_element_by_id("NextButton")
button.click()

#Select age from dropdown
element = driver.find_element_by_name('R002004') # xpath //*[@id="R002004"]
element.send_keys('30')

button = driver.find_element_by_id("NextButton")
button.click()

#Choose gender
element = driver.find_element_by_name('R002003') #xpath //*[@id="R002003"]
element.send_keys("Prefer not to answer")

button = driver.find_element_by_id("NextButton")
button.click()
print('88%')
#Including self how many adults at home how many children
element = driver.find_element_by_name('R002017')
element.send_keys("Prefer not to answer")

element = driver.find_element_by_name('R002018')
element.send_keys("Prefer not to answer")

NextButton()

# Income and Education
element = driver.find_element_by_name('R002005')
element.send_keys("Prefer not to answer")

element = driver.find_element_by_name('R002006')
element.send_keys("Prefer not to answer")

NextButton()

NextButton()

#Do you know a smiths employee
element = driver.find_element_by_xpath('//*[@id="FNSR003002"]/td[2]/span')
element.click()

NextButton()


#Enter Sweepstakes?
element = driver.find_element_by_xpath('//*[@id="FNSR003003"]/td[2]/span')
element.click()

NextButton()

#Select alternate ID for rewards points
element = driver.find_element_by_xpath('//*[@id="FNSR003005"]/div/div/div[2]/span/span')
element.click()

NextButton()

#Enter phone number
element = driver.find_element_by_name('S003009')
element.send_keys(rewards_phone_number)
element = driver.find_element_by_name('R003010')
element.send_keys(rewards_phone_number)

NextButton()

#Done
print("Finished")
driver.close()
