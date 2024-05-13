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

# Specify username and password fields when running the program
# username = "User_Name@email.com"
# password = "password123!"

# Download the compatible ChromeDriver version
chromedriver_path = ChromeDriverManager().install()  # Download and get path

# Create a service object from the path
service = webdriver.ChromeService(executable_path=chromedriver_path)

# Instantiate Chrome driver with the service object
driver = webdriver.Chrome(service=service)

# Maximize the browser window to full screen
driver.maximize_window()

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
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='run_all_cells']"))
    )
driver.execute_script("arguments[0].click();", element)

time.sleep(5)

# Scroll to the bottom of the notebook
notebook_container = driver.find_element(By.XPATH, "//*[@id='site']")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", notebook_container)

# Specify time needed to review notebook run results. Stop program earlier if needed
time.sleep(1000)

# Close the WebDriver session
driver.quit()
