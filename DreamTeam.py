from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyodbc
#import behave Given, when , then 
driver = webdriver.Chrome()

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://illindtkbstm01.corp.amdocs.com/allocation")
time.sleep(10)
print("here")
#driver.find_element(By.XPATH,'//*[@title="Search"]')
#driver.implicitly_wait(30)
#driver.find_element(By.XPATH,'//input[@type='email']')
#driver.find_element(By.XPATH,"//input[@type='email']").send_keys("shwetran@amdocs.com")
#driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)
#driver.find_element(By.XPATH,'//div[contains(text(),"Org4's")]').click()

driver.find_element(By.XPATH, '//div[contains(text(),"Org4\'s")]').click()   
               
driver.find_element(By.XPATH,'//*[@id="mainContainer"]/app-activity-bar-container/app-activity-bar/div[2]/div[1]/div/app-multi-select/div/div[2]/div/input').send_keys("Business Technology Group")

driver.find_element(By.XPATH,"//div[@class='item ng-star-inserted']//input[@type='checkbox']").click()

driver.find_element(By.XPATH,'//div[contains(text(),"Org4\'s")]').click()

server = 'ILRNADTDBST01'
database = 'DreamTeam'
username = 'dtstuser'
password = 'dt@1$Tuser'

# Establish connection
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor()

# Example query
query = " Select top 1 EmpID from [dbo].[NonHistoricalEmpEngageWithAdditionalAttributes] where ORGID4 = 4444000009  and isActive=1 and EmpID not in (Select iEmpId from dbo.EmpAllocations union Select iEmpId from dbo.EmpSpecialAllocations union Select iEmpID from EmpLoans)"

# Execute the query
cursor.execute(query)
data = cursor.fetchone()

# Check if data is not None
if data is not None:
    # Convert data to string (assuming it's a single value)
    data_str = str(*data)
#Print(*data_str)

# Fetch the results
#for row in cursor:
  #  print(*row)
#employee_id = row['EmpID']
time.sleep(10)
driver.find_element(By.XPATH,'//*[@title="Search Employee List"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@placeholder="Enter employee ID list..."]').send_keys(data_str)
driver.find_element(By.XPATH,'//*[@tooltip="Apply"]').click()
time.sleep(10)
#driver.implicitly_wait(10)
source_element = driver.find_element(By.XPATH,"(//div[@class='activityDetails'])[1]")
target_element = driver.find_element(By.XPATH,"//div[@class='grid']//span[1]//span[1]")
ActionChains(driver).drag_and_drop(source_element,target_element).perform()

cursor.close()
connection.close()

workpackage = driver.find_element(By.XPATH,"(//div[@class='allocationDetails'])[1]")
value=workpackage.value_of_css_property
print(value)

input()

