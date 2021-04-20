#Run a script to erase previous data
python3 delete_table.py


#Run script to get new data
cd newsscraper
scrapy crawl ndtv
scrapy crawl hindustan
scrapy crawl ie
scrapy crawl hindu
scrapy crawl toi