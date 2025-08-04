import os
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

load_dotenv()

@dataclass
class CarData:
    title: str
    price: float
    year: str
    mileage: str
    fuel_type: str
    transmission: str
    power: str
    car_type: str
    doors: str
    color: str
    condition: str
    features: List[str]
    url: str

class SimpleScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": os.getenv('USER_AGENT', 'Mozilla/5.0')
        })

    def scrape_url(self, url: str) -> CarData:
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            # --- Required: title ---
            title_tag = soup.find("h1", id="viewad-title")
            if not title_tag:
                raise ValueError("Missing title on the page.")
            title = title_tag.text.strip()

            # --- Required: price ---
            price_meta = soup.find("meta", itemprop="price")
            if not price_meta:
                raise ValueError("Missing price on the page.")
            price = float(price_meta["content"])

            # Optional values with fallback to "None"
            mileage = self._get_text_by_label(soup, "Kilometerstand")
            year = self._extract_year(soup, "Erstzulassung")
            fuel_type = self._get_text_by_label(soup, "Kraftstoffart")
            transmission = self._get_text_by_label(soup, "Getriebe")
            power = self._get_text_by_label(soup, "Leistung")
            car_type = self._get_text_by_label(soup, "Fahrzeugtyp")
            doors = self._get_text_by_label(soup, "Anzahl Türen")
            color = self._get_text_by_label(soup, "Außenfarbe")
            condition = self._get_text_by_label(soup, "Fahrzeugzustand")

            # Features list
            features = [tag.text.strip() for tag in soup.select(".checktaglist .checktag")]
            if not features:
                features = ["None"]
                
            return CarData(
                title=title,
                price=price,
                year=year,
                mileage=mileage,
                fuel_type=fuel_type,
                transmission=transmission,
                power=power,
                car_type=car_type,
                doors=doors,
                color=color,
                condition=condition,
                features=features,
                url=url
            )

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            raise

    def _get_text_by_label(self, soup: BeautifulSoup, label: str) -> str:
        li = soup.find("li", string=lambda t: t and label in t)
        if li:
            span = li.find_next("span")
            if span:
                return span.text.strip()
        return "None"

    def _extract_year(self, soup: BeautifulSoup, label: str) -> str:
        text = self._get_text_by_label(soup, label)
        if text != "None":
            parts = text.split()
            for part in parts:
                if part.isdigit() and len(part) == 4:
                    return part
        return "None"
