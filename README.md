# Java Islands Kelurahan From Wikipedia

This repository contains a web scraper script that can be used to extract the names of all sub-districts (kelurahan) in the Java islands from Wikipedia. The script utilizes Python and the BeautifulSoup library to scrape the data from the Wikipedia pages. The get_kelurahan_data(url, city_name) function is the core of the web scraper. It fetches the HTML content from a specified Wikipedia URL, searches for the table containing sub-district names, and identifies the column with the sub-district names using header text variations like 'Daftar Desa', 'Daftar Desa/Kelurahan', or 'Daftar Kelurahan'. The function then extracts the sub-district names, performs data cleaning, and organizes the data into a Pandas DataFrame.

## Prerequisites

Before running the web scraper, make sure you have the following installed:

- Python 3.x
- BeautifulSoup library

You can install the required packages using the following command:
pip install beautifulsoup4

## How to Use
1. Clone this repository to your local machine:
git clone https://github.com/your-username/java-islands-subdistricts-scraper.git
cd java-islands-subdistricts-scraper

or use GitHub Desktop

2. Run the web scraper script:
python scraper.py

The script will start scraping the Wikipedia pages for all sub-districts in the Java islands and save the data into a CSV file.

## Output
The web scraper will generate a CSV file named java_islands_subdistricts.csv that contains the names of all sub-districts in the Java islands.

## Explanation of the Code in main.py
The code snippet provided in main.py demonstrates how the get_kelurahan_data function identifies the column index containing the sub-district names in the HTML table. It iterates through the header columns using the enumerate function, and for each header column, it checks if any of the variations 'Daftar Desa', 'Daftar Desa/Kelurahan', or 'Daftar Kelurahan' are present in the header text using the in operator. If a match is found, the kelurahan_column_index is assigned the current index, and the loop breaks, indicating the location of the desired column with the sub-district names. This process allows the function to accurately locate the necessary data in the Wikipedia table and extract the sub-district names for further processing.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to use and modify the code according to your needs. If you have any questions or suggestions, please feel free to open an issue or submit a pull request.

Happy web scraping! 🚀