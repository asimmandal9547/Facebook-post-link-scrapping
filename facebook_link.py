from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

# Notification block or bypass......................
driver = webdriver.Edge(executable_path = 'C:\\msedgedriver.exe')


# login to facebook....................
def facebook_login():
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    Email_box=driver.find_element(By.NAME,"email").send_keys('your_email_or_phone_number')
    Pass_box=driver.find_element(By.NAME,'pass').send_keys('your_facebook_password')

    login_btn=driver.find_element(By.NAME,'login').click()
    time.sleep(2)

facebook_login()


# whopostedwhat page....................
driver.get('https://whopostedwhat.com/')


def get_Id(link):
    paste_link= driver.find_element(By.ID, "username-input").send_keys(link)
    driver.find_element(By.ID,"btn-get-user").click()
    
def search_by_specific_day(keyword, day, year):
    search_input = driver.find_element(By.ID, "input-exact-day-keyword").send_keys(keyword)
    date_input = driver.find_element(By.ID, "hey").send_keys(day)
    driver.find_element(By.ID, "btn-search-exact-day").click()
    time.sleep(5)

def search_by_specific_month(keyword, month):
    search_input = driver.find_element(By.ID, "input-exact-month-keyword").send_keys(keyword)
    month_input = driver.find_element(By.ID, "hey2").send_keys(month)
    driver.find_element(By.ID, "btn-search-exact-month").click()
    time.sleep(5)

def search_by_specific_year(keyword, year):
    search_input = driver.find_element(By.ID, "input-exact-year-keyword").send_keys(keyword)
    year_input = driver.find_element(By.ID, "hey3").send_keys(year)
    driver.find_element(By.ID, "btn-search-exact-year").click()
    time.sleep(5) 

def search_by_timerange(keyword, month1, month2):
    search_input = driver.find_element(By.ID, "input-timerange-keyword").send_keys(keyword)
    month_input1 = driver.find_element(By. ID, "from-input").send_keys(month1)
    month_input2 = driver.find_element(By. ID, "until-input").send_keys(month2)
    driver.find_element(By.ID,"btn-search-timerange").click()

def search_by_Location(keyword,UID):
    search_input = driver.find_element(By.ID, "input-location-keyword").send_keys(keyword)
    UID_input = driver.find_element(By.ID, "input-location-id").send_keys(UID)
    driver.find_element(By.ID, "btn-search-location").click()

def search_by_Instagram(link,day):
    search_input = driver.find_element(By.ID, "input-ig-date-location").send_keys(keyword)
    day_month_year_input = driver.find_element(By.ID, "input-ig-date-date").send_keys(day)
    driver.find_element(By.ID, "btn-search-ig-date").click()

def post_from(keyword,UID):
    search_input = driver.find_element(By.ID, "input-user-keyword").send_keys(keyword)
    UID_input = driver.find_element(By.ID, "input-user-id").send_keys(UID)
    driver.find_element(By.ID, "btn-search-user").click()
    
def perform_search():
    search_type = input("Enter search type (day/month/year/timerange/Id/Location/Instagram): ")

    if search_type == "day":
        keyword = input("Enter keyword (e.g, Sachin): ")
        day = input("Enter day (e.g., 9 Jan 2020): ")
        year = input("Enter year (e.g, 2020): ")
        search_by_specific_day(keyword, day, year)
    elif search_type == "month":
        keyword = input("Enter keyword (e.g, Sachin): ")
        month = input("Enter month (e.g., Jan 2020): ")
        search_by_specific_month(keyword, month)
    elif search_type == "year":
        keyword = input("Enter keyword (e.g, Sachin): ")
        year = input("Enter year (e.g, 2020): ")
        search_by_specific_year(keyword, year)
    elif search_type=="Id":
        link= input("Paste your link (e.g.,https://www.facebook.com/zuck): ")
        get_Id(link)
    elif search_type == "timerange":
        keyword = input("Enter keyword (e.g, Sachin): ")
        month1 = input("Enter month (e.g.,from Jan 2020): ")
        month2 = input("Enter month (e.g.,until Jan 2020): ")
    elif search_type == "Location":
        keyword = input("Enter keyword (e.g, Sachin): ")
        UID = input("Enter UID (e.g.,106423786059675): ")
    elif search_type == "Instagram":
        link = input("Enter Url (e.g, https://www.instagram.com/explore/locations/95099702/mgm-grand-las-vegas/): ")
        day = input("Enter day (e.g., 9 Jan 2020): ")
    elif search_type == "post_from":
        keyword = input("Enter keyword (e.g, Mumbai): ")
        UID = input("Enter UID (e.g.,106423786059675): ")
    else:
        print("Invalid search type. Please try again.")

perform_search()
    

def jump_to_current_window():
    p=driver.current_window_handle
    parent=driver.window_handles[0]
    child=driver.window_handles[1]
    driver.switch_to.window(child)

jump_to_current_window()

# for find the  web-elements from new tab..........
find_links = driver.find_elements(By.XPATH,"//div[@class='x9f619 x193iq5w x1miatn0 xqmdsaz x1gan7if x1xfsgkm']")

def extract_results(find_links):
    result_list = []
    for find_link in find_links:
        find_tags = find_link.find_elements(By.TAG_NAME, "a")

        for tag in find_tags:
            result = tag.get_attribute('href')
            if result:
                result_list.append(result)
        print('Results from Facebook: ',result_list)
    return result_list

result_list = extract_results(find_links)

def write_results_to_file(result_list, output_file_path):
    with open(output_file_path, "w") as f:
        f.write("<html><head><title>Search Results</title></head><body>")
        for link in result_list:
            f.write('<a href="' + str(link) + '">' + str(link) + '</a><br>')
        f.write("</body></html>")

output_file_path = "results_from_facebook.html" # your output file path
write_results_to_file(result_list, output_file_path)

driver.quit()
