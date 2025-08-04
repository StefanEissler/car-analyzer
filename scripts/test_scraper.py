import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from car_analyzer.scraper import SimpleScraper

def main():
    test_url = input("Gib eine Kleinanzeigen URL ein: ")
    
    scraper = SimpleScraper()
    result = scraper.scrape_url(test_url)
    
    if result:
        print(f"Titel: {result.title}")
        print(f"URL: {result.url}")
    else:
        print("Scraping fehlgeschlagen")

if __name__ == "__main__":
    main()