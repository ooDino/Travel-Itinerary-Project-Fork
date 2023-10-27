from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_functionality():
    chrome_options = Options()
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(
            "http://127.0.0.1:8000/search_results/?term=restaurant&location=San%20Francisco"
        )  # initial pre-search page not set up, but we can test this out with an initial search

        # searching for 'restaurant' in 'New York'.
        search_term_input = driver.find_element(By.NAME, "term")
        search_term_input.clear()
        search_term_input.send_keys("restaurant")
        location_input = driver.find_element(By.NAME, "location")
        location_input.clear()
        location_input.send_keys("New York")
        location_input.send_keys(Keys.RETURN)  # press Enter

        wait = WebDriverWait(driver, 10)

        # making sure stuff is actually returned for New York... weird if it wasn't but still
        ul = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
        list_items = ul.find_elements(By.TAG_NAME, "li")
        assert len(list_items) > 0, "No results found for 'restaurant' in 'New York'."

        # searching for a non-existent term in a non-existent location.
        search_term_input = driver.find_element(By.NAME, "term")
        search_term_input.clear()
        search_term_input.send_keys("somethingthatdoesntexist")
        location_input = driver.find_element(By.NAME, "location")
        location_input.clear()
        location_input.send_keys("bleh")
        location_input.send_keys(Keys.RETURN)  # press Enter

        # Check if results are shown in <ul>.
        try:
            ul = wait.until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
            list_items = ul.find_elements(By.TAG_NAME, "li")
            assert len(list_items) > 0, "No results found."
        # check if the right error message is shown if it didn't find anything
        except:
            error_msg = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//*[contains(text(), 'Sorry, there was an error processing your request.')]",
                    )
                )
            )
            assert error_msg is not None, "Error message not displayed."

    finally:
        driver.quit()


if __name__ == "__main__":
    test_search_functionality()
