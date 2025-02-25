#Web Scraping and Data Analysis of E-commerce Products
Overview
This project focuses on web scraping product data from an e-commerce website, storing it in a structured format, and performing analysis to extract insights. The goal is to scrape product names, prices, and links, save them in a CSV file, and visualize the price distribution.

Features
Web Scraping: Extracts product details including name, price, and link.
Data Storage: Saves scraped data in a CSV file for further processing.
Data Cleaning: Filters out invalid price entries and ensures data integrity.
Statistical Analysis: Identifies the most and least expensive products, along with price distribution statistics.
Visualization: Generates histograms to display the price distribution of products.

Technologies Used
Python – For scripting and data processing
BeautifulSoup – For web scraping
Requests – To fetch webpage content
Pandas – For data manipulation
Matplotlib & Seaborn – For data visualization

Installation and Usage
Prerequisites
Ensure you have Python installed along with the required dependencies. You can install them using:
pip install requests beautifulsoup4 pandas matplotlib seaborn
Running the Script
Update the URL variable in the script with the target e-commerce website.
Run the script: 
python scraper.py
The output CSV file (product_prices.csv) will be generated.
Analysis results, including insights on most and least expensive products, will be displayed.
A histogram showing the price distribution will be plotted.

Output
CSV File: A structured dataset containing scraped product details.
Statistical Summary: Key insights on pricing trends.
Graphical Representation: A histogram visualizing price distribution.
Future Improvements
Expand scraping functionality to multiple pages.
Implement real-time price monitoring.
Store data in a database for better management.
License
This project is open-source and free to use under the MIT License.


