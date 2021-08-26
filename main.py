from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.gov.uk/book-theory-test')

start_reg_button = driver.find_element_by_xpath('/html/body/div[4]/main/div/div[2]/div/div/section[1]/p/a')
webdriver.ActionChains(driver).move_to_element(start_reg_button).click().perform()

# New page

day_input = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div/fieldset/div[1]/div[1]/div/input')
month_input = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div/fieldset/div[1]/div[2]/div/input')
year_input = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div/fieldset/div[1]/div[3]/div/input')

start_date = datetime.date(2021, 11, 4)  # this is for later
end_date = start_date + datetime.timedelta(days=20)

day_input.send_keys(f'{start_date.day}')
month_input.send_keys(f'{start_date.month}')
year_input.send_keys(f'{start_date.year}')

continue_button1 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/button')
webdriver.ActionChains(driver).move_to_element(continue_button1).click().perform()

# new page

radio_button1 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div/fieldset/div/div[2]/input')
webdriver.ActionChains(driver).move_to_element(radio_button1).click().perform()

continue2 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/button')
webdriver.ActionChains(driver).move_to_element(continue2).click().perform()

# new page

fname_input = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div[1]/input')
sname_input = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div[2]/input')
long_number = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div[3]/input')
day_dob = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/fieldset/div/div[2]/div[1]/div/input')
month_dob = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/fieldset/div/div[2]/div[2]/div/input')
year_dob = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/fieldset/div/div[2]/div[3]/div/input')
continue3 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/button')

fname_input.send_keys('Alex Stefanov')
sname_input.send_keys('Nakov')
long_number.send_keys('NAKOV004293AS9EE')
day_dob.send_keys('29')
month_dob.send_keys('04')
year_dob.send_keys('2003')
webdriver.ActionChains(driver).move_to_element(continue3).click().perform()

# new page

email_input1 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/fieldset/div[1]/input')
email_input2 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/fieldset/div[2]/input')
email_input1.send_keys('alex.nakov3@gmail.com')
email_input2.send_keys('alex.nakov3@gmail.com')
continue4 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/button')
webdriver.ActionChains(driver).move_to_element(continue4).click().perform()

# new page

radio_button2 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/div/form/div/fieldset/div[2]/div[1]/input')
continue5 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/div/form/button')
webdriver.ActionChains(driver).move_to_element(radio_button2).click().perform()
webdriver.ActionChains(driver).move_to_element(continue5).click().perform()

# new page

radio_button3 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/div/form/fieldset/div/div/div/div[1]/input')
continue6 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/div/form/button')
webdriver.ActionChains(driver).move_to_element(radio_button3).click().perform()
webdriver.ActionChains(driver).move_to_element(continue6).click().perform()

# new page

postcode_input = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/div/form/fieldset/div/input')
continue7 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/div/form/button')
postcode_input.send_keys('IG8 7NR')
webdriver.ActionChains(driver).move_to_element(continue7).click().perform()

# new page

test_centres_url = driver.current_url
new_url = test_centres_url + '?numberOfResults=50&distanceUom=miles'
driver.get(new_url)

# new page

test_centres_select_button_list = []
for i in range(1, 51):
    test_centres_select_button_list.append(driver.find_element_by_xpath('/html/body/div[1]/main/div[4]/div[1]/div[2]/'
                                                                        'div/div/form/fieldset/'
                                                                        f'div[{i}]/div[3]/div/button'))

for test_center_select_button in test_centres_select_button_list:
    webdriver.ActionChains(driver).move_to_element(test_center_select_button).click().perform()
    continue8 = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/button')
    webdriver.ActionChains(driver).move_to_element(continue8).click().perform()
    button1 = driver.find_element_by_class_name('govuk-button govuk-button--secondary')
    print(button1)
