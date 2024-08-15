## Web Scraping Bot

### Description
This repository contains a Python web scraping bot designed to extract data from a list of URLs provided. The bot utilizes Scrapy for scraping and optionally integrates Selenium for certain tasks. The main goal is to gather specific information from each URL, listed in the targeted URL section.

### Problem Statement:
I have been tasked with scraping data from United States government websites using the Python Scrapy Framework. My goal is to extract specific information from these websites for further analysis or processing.

### Objective
The objective of this task is to develop a scraping bot that can efficiently retrieve relevant data from various US government websites. This data could be related to government programs, policies, statistics, publications, or any other pertinent information.

### Targeted Url: 
https://rewardsforjustice.net/index/?jsf=jet-engine:rewards-grid&tax=crime-category:1070%2C1071%2C1073%2C1072%2C1074

### Requirements
Python
Scrapy
Data to Scrape
  1) Page URL
  2) Category
  3) Title
  4) Reward amount
  4) Associated Organization(s)
  5) Associated Location(s)
  6) About
  7) Image URL(s)
  8) Date Of Birth (Stored in ISO date format)

### Output
The output file formats should be in "xlsx" and "JSON". The file name should follow this format:

Output file name:

SName_Ctime.xlsx (Example: RWJST_20220629_235959.xlsx)
SName_Ctime.json (Example: RWJST_20220629_235959.json)
Where:
SName: Your Spider Name
Ctime: Current date and time. Date time format should be "YYYYMMDD_hhmmss"

### How to Use
Clone this repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the scraping bot by executing the main script.
Retrieve the scraped data in both xlsx and JSON formats.

### Support
For any inquiries or issues, feel free to open an issue on this repository.

### Contribution
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.

### License
This project is licensed under the MIT License.

### Contact
Email: ywaquar@gmail.com
Mobile: +91-8269058687


##### Begin the scrappy project with the below command
`scrapy startproject project_name`

##### Navigate to the spiders folder using the following command
`cd project_name`
`cd project_name/spiders`

##### create the folder with foldername as spider_name.py using the below command
`scrapy genspider spider_name url`

##### check ipython is installed or not
`ipython --version`
`pip install ipython`

##### Add the following in the scrapy.cfg below the dafault
`shell = ipython`

#### Input Task

[Scraping Test (1).pdf](https://github.com/user-attachments/files/16621102/Scraping.Test.1.pdf)

#### OutPut CSV
[terrordata.csv](https://github.com/user-attachments/files/16621110/terrordata.csv)
