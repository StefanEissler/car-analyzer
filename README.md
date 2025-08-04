# Car Analyzer 🚗

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
<!--[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)-->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An open-source tool for automated car evaluation that scrapes vehicle listings from German automotive platforms and provides AI-powered analysis with pros/cons evaluation.

## 🎯 Features

- **Multi-platform scraping**: Support for mobile.de and kleinanzeigen.de
- **Intelligent data extraction**: Automatically extracts price, year, mileage, and vehicle details
- **AI-powered analysis**: Generate comprehensive vehicle evaluations
- **Price analysis**: Compare listing prices with estimated market values
- **Image analysis**: Assess vehicle condition from photos (planned)
- **Export capabilities**: Save results to CSV/JSON formats
- **CLI interface**: Easy-to-use command-line tools

## 🤝 Ethical Usage Guidelines

This project promotes responsible web scraping:

### ✅ Encouraged Use Cases
- Personal car purchase research
- Academic studies on automotive markets
- Small-scale price comparison for individual users
- Learning web scraping techniques

### ❌ Discouraged Use Cases
- Large-scale commercial data harvesting
- Creating competing automotive platforms
- Overloading target websites with excessive requests
- Ignoring website terms of service

### 🛡️ Built-in Protections
- Configurable request delays (default: 2-3 seconds)
- robots.txt checking (planned)
- Rate limiting features
- User-Agent identification as research tool

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/car-analyzer.git
cd car-analyzer
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package in development mode**
```bash
pip install -e .
```

### Basic Usage

#### Analyze a single vehicle listing

```bash
python scripts/test_scraper.py
# Enter a mobile.de or kleinanzeigen.de URL when prompted
```

#### Using the Python API

```python
from car_analyzer.scraper import SimpleScraper

# Initialize scraper
scraper = SimpleScraper()

# Scrape a vehicle listing
url = "https://mobile.de/anzeige/example"
car_data = scraper.scrape_url(url)

if car_data:
    print(f"Title: {car_data.title}")
    print(f"Price: €{car_data.price:,.0f}")
    print(f"Year: {car_data.year}")
    print(f"Mileage: {car_data.mileage:,} km")
```

## 📁 (Predefined) Project Structure

```
car-analyzer/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── requirements.txt          # Python dependencies
├── setup.py                  # Package configuration
├── pyproject.toml           # Modern Python packaging
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── src/
│   └── car_analyzer/        # Main package
│       ├── __init__.py      # Package initialization
│       ├── scraper.py       # Web scraping functionality
│       ├── models/          # Data models (planned)
│       ├── analyzers/       # AI analysis modules (planned)
│       └── utils/           # Utility functions (planned)
├── scripts/
│   ├── test_scraper.py      # Single URL testing script
│   └── collect_data.py      # Batch data collection (planned)
├── data/
│   ├── raw/                 # Raw scraped data
│   ├── processed/           # Cleaned and processed data
│   └── models/              # Trained models (planned)
├── tests/
│   └── test_scrapers.py     # Unit tests (planned)
├── notebooks/
│   └── exploration.ipynb    # Jupyter notebooks for analysis
└── docs/
    └── api.md               # API documentation (planned)
```

## 🛠️ Development

### Setting up Development Environment

1. **Clone and setup**
```bash
git clone https://github.com/yourusername/car-analyzer.git
cd car-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

2. **Install development dependencies**
```bash
pip install pytest black flake8 mypy
```

3. **Run tests**
```bash
pytest tests/
```

4. **Code formatting**
```bash
black src/
flake8 src/
```

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Available configuration options:
- `USER_AGENT`: Custom user agent for web scraping
- `REQUEST_DELAY`: Delay between requests (seconds)
- `MAX_RETRIES`: Maximum retry attempts for failed requests
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

## 📊 (Proposed) Data Models

### CarData

The core data structure for vehicle information:

```python
@dataclass
class CarData:
    title: str                    # Vehicle listing title
    price: Optional[float]        # Price in EUR
    year: Optional[int]          # Manufacturing year
    mileage: Optional[int]       # Mileage in kilometers
    url: str                     # Original listing URL
    make: Optional[str]          # Vehicle manufacturer
    model: Optional[str]         # Vehicle model
    fuel_type: Optional[str]     # Fuel type (gasoline, diesel, etc.)
```

### CarAnalysis (Planned)

AI analysis results structure:

```python
@dataclass
class CarAnalysis:
    car_data: CarData
    overall_score: float         # Overall rating 1-10
    price_score: float          # Price-performance rating 1-10
    condition_score: float      # Vehicle condition rating 1-10
    pros: List[str]             # Positive aspects
    cons: List[str]             # Negative aspects
    estimated_market_value: Optional[float]
    price_difference: Optional[float]
```

## 🔧 API Reference

### SimpleScraper Class

The main scraping class for extracting vehicle data.

#### Methods

**`__init__()`**
Initialize the scraper with default settings.

**`scrape_url(url: str) -> Optional[CarData]`**
Scrape a single vehicle listing URL.

- **Parameters:**
  - `url (str)`: The vehicle listing URL
- **Returns:**
  - `CarData`: Extracted vehicle data or None if failed
- **Raises:**
  - `requests.RequestException`: Network-related errors

#### Example Usage

```python
from car_analyzer.scraper import SimpleScraper

scraper = SimpleScraper()

# Scrape single URL
result = scraper.scrape_url("https://mobile.de/anzeige/example")

if result:
    print(f"Found: {result.title}")
    print(f"Price: €{result.price}")
else:
    print("Scraping failed")
```

## 🎯 Roadmap

### Phase 1: Basic Scraping ✅
- [x] Basic project structure
- [x] Simple web scraper for kleinanzeigen.de
- [x] Data extraction (price, year, mileage)
- [x] CLI interface

### Phase 2: Enhanced Scraping (In Progress)
- [ ] Support for mobile.de
- [ ] Image URL extraction
- [ ] Enhanced data validation
- [ ] Batch processing capabilities
- [ ] Data export to CSV/JSON

### Phase 3: AI Analysis (Planned)
- [ ] Machine learning price prediction
- [ ] Computer vision for image analysis
- [ ] LLM integration for pros/cons generation
- [ ] Market value estimation
- [ ] Condition assessment from photos

### Phase 4: Web Application (Planned)
- [ ] Web-based user interface
- [ ] Browser extension for one-click analysis
- [ ] Historical data tracking
- [ ] User accounts and saved searches
- [ ] API for third-party integrations

### Phase 5: Advanced Features (Future)
- [ ] Real-time monitoring of new listings
- [ ] Price trend analysis
- [ ] Automated alerts for good deals
- [ ] Integration with financing calculators
- [ ] Mobile app development

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Bug Reports**: Found a bug? [Open an issue](https://github.com/yourusername/car-analyzer/issues)
2. **Feature Requests**: Have an idea? [Start a discussion](https://github.com/yourusername/car-analyzer/discussions)
3. **Code Contributions**: Submit pull requests with improvements
4. **Documentation**: Help improve our docs
5. **Testing**: Test the tool and report issues

### Development Workflow

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Make your changes**
```bash
# Make changes
git add .
git commit -m "Add: your feature description"
```

4. **Run tests and formatting**
```bash
pytest tests/
black src/
flake8 src/
```

5. **Push and create pull request**
```bash
git push origin feature/your-feature-name
```

### Code Style Guidelines

- Use [Black](https://black.readthedocs.io/) for code formatting
- Follow [PEP 8](https://pep8.org/) style guidelines
- Add type hints where possible
- Write docstrings for all public functions

<!-- ## 📄 License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
-->
## ⚖️ Legal Notice

This tool is designed for personal use and research purposes. Users are responsible for:

- Complying with website terms of service
- Respecting robots.txt files
- Following applicable laws and regulations
- Using reasonable request rates to avoid overloading servers

The developers are not responsible for misuse of this tool or any legal consequences.


## 🔗 Links

- **Documentation**: [Link to docs](https://yourusername.github.io/car-analyzer)
- **PyPI Package**: [Link when published](https://pypi.org/project/car-analyzer)
- **Docker Hub**: [Link when available](https://hub.docker.com/r/yourusername/car-analyzer)

---

**Made with ❤️ for the automotive community**