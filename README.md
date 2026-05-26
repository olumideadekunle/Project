

#  Theatre Events Data Pipeline — Shakespeare’s Globe Scraper

A lightweight data pipeline that extracts structured theatre event information from the Shakespeare’s Globe website and transforms it into a clean, analysis ready dataset.

This project demonstrates practical skills in **web scraping, data cleaning, and dataset engineering**, with a focus on building reproducible and structured data outputs from unstructured web sources.

---

##  What This Project Does

The scraper collects live event listings and converts them into a structured dataset containing:

* Event metadata (title, category, type, status)
* Venue details (name, location, capacity)
* Event schedule and dates
* Pricing information (cleaned and normalized)
* Event imagery (where available)
* Descriptions and contextual metadata

The output is exported as a CSV file ready for analysis, dashboards, or downstream ML/analytics pipelines.

---

##  Pipeline Overview

The workflow follows a simple but production-style structure:

### 1. Data Ingestion

* Sends HTTP requests to the Shakespeare’s Globe “What’s On” page
* Retrieves raw HTML content for processing

### 2. Parsing Layer

* Uses BeautifulSoup to extract relevant event nodes
* Traverses anchor tags containing event-related information

### 3. Data Cleaning & Filtering

* Removes navigation noise and irrelevant links
* Filters short or malformed text entries
* Deduplicates event records
* Standardises extracted text fields

### 4. Feature Engineering

Each event is enriched with additional structured attributes such as:

* Venue capacity mapping
* Price range normalization
* Timestamped scraping metadata
* Event image extraction (when available)

### 5. Export Layer

* Writes cleaned records into a structured CSV dataset

---

##  Output Schema

Each record in the dataset includes:

* `event_title`
* `event_category`
* `event_type`
* `event_status`
* `venue_name`
* `venue_city`
* `venue_country`
* `venue_capacity`
* `event_start_date`
* `event_end_date`
* `price_range`
* `seat_price_range`
* `event_image`
* `event_description`
* `scraped_at`

---

##  Tech Stack

* Python 3
* Requests (HTTP ingestion)
* BeautifulSoup4 (HTML parsing)
* Regex (data extraction & cleaning)
* CSV module (data export)

---

##  Design Decisions

* **Rule-based filtering** was used instead of ML classification to keep the pipeline lightweight and deterministic.
* **Capacity mapping** is hardcoded to simulate enrichment from external reference datasets.
* **Price extraction** uses regex heuristics to handle inconsistent formatting across the page.
* **Deduplication** is handled using an in-memory set to ensure unique event records.

---

##  Future Improvements

This pipeline can be extended into a more production-grade system by adding:

* Dynamic multi-page crawling
* Real-time booking URL resolution per event
* Persistent storage (PostgreSQL / MongoDB)
* Scheduled scraping with cron or GitHub Actions
* Streamlit dashboard for event analytics
* API layer using FastAPI

---

##  Author

**Olumide**
Data Engineer | AI Builder | Web Scraping & Automation Enthusiast

---

##  Note

This project is part of a growing portfolio focused on building real-world data pipelines from unstructured web sources and transforming them into structured, analysis-ready datasets.

---

If you want next upgrade, I can help you turn this into a:

*  “Senior Data Engineer style README (Netflix-level documentation)”
*  Streamlit dashboard version
*  Fully production pipeline (API + database + scheduler)

Just say 👍
