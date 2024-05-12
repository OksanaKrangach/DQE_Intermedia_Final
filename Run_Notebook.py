from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Save pages URL into variables
login_page_url = 'https://login.dlabanalytics.com/auth/realms/dlab/protocol/openid-connect/auth?client_id=iskldl04-ui&redirect_uri=https://ssn.trainings.dlabanalytics.com/&response_type=code'
dlab_url = "https://ssn.trainings.dlabanalytics.com/#/instances"
notebook_url = "https://dqelearn.trainings.dlabanalytics.com/okrangach/notebooks/DQ_Checks_okrangach.ipynb"

# Specify username and password fields
# username = input("Enter your username (email): ")
# password = input("Enter your password: ")

# Download the compatible ChromeDriver version
chromedriver_path = ChromeDriverManager().install()  # Download and get path

# Create a service object from the path
service = webdriver.ChromeService(executable_path=chromedriver_path)

# Instantiate Chrome driver with the service object
driver = webdriver.Chrome(service=service)

# Open the SSO login page
driver.get(login_page_url)

time.sleep(2)  # Adjust this time delay as needed

# Submit the login form
driver.find_element(By.ID, 'social-epam-idp').click()

# Open the URL of the Jupyter Notebook

WebDriverWait(driver, 300).until(
    EC.url_to_be(dlab_url)
)

driver.get(notebook_url)

WebDriverWait(driver, 300).until(
    EC.url_to_be(notebook_url)
)

time.sleep(5)

# Execute all cells in the notebook
runAllDiv=driver.find_element(By.XPATH, "//div[text()='Run All Cells']")
driver.execute_script("arguments[0].click();", runAllDiv)

time.sleep(5)

# Scroll to the bottom of the notebook
content=driver.find_element(By.XPATH, "//div[@class='jp-WindowedPanel-outer']")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", content)

time.sleep(3000)

# Close the WebDriver session
driver.quit()
