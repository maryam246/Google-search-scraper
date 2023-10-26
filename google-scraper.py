import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


# Function to sanitize a string for use as a filename
def sanitize_filename(filename):
    # Remove invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading and trailing whitespaces
    sanitized = sanitized.strip()
    return sanitized


# Function to scroll down the page using Selenium
def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust the sleep duration as needed


# Function to click "More results" to load additional search results
def click_more_results(driver):
    try:
        more_results_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Show more results')
        more_results_button.click()
        time.sleep(2)  # Wait for the page to load
    except NoSuchElementException:
        pass


# Function to perform Google search and retrieve search results
def google_search(query, num_results=50):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    search_results = []  # Initialize search_results

    try:
        driver.get("https://www.google.com")

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )

        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        query_sanitized = sanitize_filename(query)  # Sanitize the query for use in the filename

        while len(search_results) < num_results:
            scroll_down(driver)
            search_results += driver.find_elements(By.CSS_SELECTOR, 'h3')

            if len(search_results) >= num_results:
                break

            click_more_results(driver)


        if search_results:
            with open(f"{query_sanitized}_result.txt", "w", encoding="utf-8") as file:
                for result in search_results[:num_results]:
                    title = result.text
                    url = result.find_element(By.XPATH, '..').get_attribute("href")
                    file.write(f"Title: {title}\n")
                    file.write(f"URL: {url}\n")

        print("Result saved successfully.")

    except TimeoutException:
        print("Timeout: The search input field could not be found within the timeout.")
    finally:
        driver.quit()


if __name__ == "__main__":
    query = input("Enter your search query:")  # User input for the search query
    google_search(query)
