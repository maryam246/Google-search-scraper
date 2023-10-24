# Google Search Results Scraper
The google-scraper.py script allows you to perform Google searches, retrieve search results, and save the first 50 results to a text file. Below, we'll walk through the script and understand its functionality.

## _Overview_
This Python script uses the Selenium library to automate web interactions and perform Google searches. It's a command-line tool that prompts the user for a search query, scrapes search results, and saves them to a text file.

## Key Functions
Let's dive into the key functions and how they work:

### sanitize_filename(filename):

This function is used to sanitize a string for use as a filename. It removes any characters that are invalid in filenames, such as <>:"/\|?*, and strips leading and trailing whitespaces. This ensures that the search query can be used as a valid filename.

### scroll_down(driver):

The scroll_down function uses Selenium to scroll down the web page to load additional search results. It simulates pressing the "Page Down" key and includes a sleep duration to allow time for content to load.

### click_more_results(driver):

This function clicks the "Show more results" button to load additional search results. It uses the Selenium WebDriver to locate and click the button. If no more results are available, it handles the NoSuchElementException gracefully.

### google_search(query, num_results=50):

 The main function for performing Google searches and retrieving results. It uses the following steps:

- It initializes the Chrome WebDriver using the specified chrome_driver_path.
- It opens the Google homepage and locates the search input field.
- The script then iteratively scrapes search results:
1. It scrolls down the page to load more results.
2. It collects search results, storing them in the search_results list.
3. If the desired number of results (default: 50) is reached, the loop terminates.
4. If not, it clicks the "Show more results" button and repeats the process.
- Once the results are collected, it saves the first 50 results to a text file using the sanitized search query as the filename.
## Usage Follow these steps to use the script:

1. Ensure you have Python installed and the required packages (Selenium) set up.

2. Download the appropriate Chrome WebDriver that matches your Chrome browser version and set its path in the code.

3. Run the script in the terminal or command prompt.

4. Enter your search query when prompted.

5. The script will start the Google search, scrape results, and save 1st 50 search result in the file.

