# Automated Google News Scraper 📈

This Python script automatically fetches news articles from the last 10 days across five predefined categories (Technology, Entertainment, Sports, Science, and Health). It uses the `pygooglenews` library to search for topics, cleans the data using `pandas`, and saves the structured results into both a `.csv` and `.xlsx` file for easy analysis.

## 🚀 Features

* **Time-Filtered:** Fetches articles published within the "last 10 days" (`10d`).
* **Categorized:** Gathers news for 5 specific topics.
* **Structured Output:** Saves data to `pandas` DataFrame.
* **Multi-Export:** Exports the final, clean data to both `CSV` and `Excel` formats.
* **Data Cleaning:**
    * Removes duplicate articles (based on headline and URL).
    * Cleans HTML tags from news summaries.
    * Sorts articles by published date (newest first).
    * Fixes datetime timezone issues for Excel compatibility.

## 💻 Technology Stack

* **Python** 3.10+
* **`pygooglenews`**: For fetching Google News data.
* **`pandas`**: For data manipulation, cleaning, and structuring.
* **`openpyxl`**: Required by `pandas` to write `.xlsx` files.
* **`beautifulsoup4`**: For cleaning HTML tags from summaries.

## 🔧 Installation & Setup

This project has a **critical dependency conflict** that requires a specific, two-step installation. The `pygooglenews` library (v0.1.2) requires an old, broken version of `feedparser`.

To fix this, we will manually install the *correct* dependencies first, then install `pygooglenews` without its own dependencies.

**1. Clone the repository:**
git clone https://[your-github-repo-url].git
cd [your-project-directory]

**2. Create a virtual environment (Recommended):**

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

**3. Run the Two-Step Installation:**
Step 1: Install all dependencies except pygooglenews. This includes the modern, working version of feedparser.Bashpip install "dateparser<0.8.0,>=0.7.6" feedparser pandas openpyxl beautifulsoup4
Step 2: Force-install pygooglenews without its broken dependencies (which we've already handled).Bashpip install --no-deps pygooglenews
You are now ready to run the script.

**▶️ How to Run**
Once all dependencies are installed, simply run the Python script from your terminal:
python news_scraper.py

The script will print its progress to the console:Initializing Google News client...
Fetching news for category: 🖥️ Technology (Search: 'Technology')...
Fetching news for category: 🎬 Entertainment (Search: 'Entertainment')...
Fetching news for category: 🏅 Sports (Search: 'Sports')...
Fetching news for category: 🔬 Science (Search: 'Science')...
Fetching news for category: 💊 Health (Search: 'Health')...
Total articles fetched: 500
Creating DataFrame...
Converting dates...
Removing timezone info for Excel compatibility...
Saving to google_news_last_10_days.csv...
Saving to google_news_last_10_days.xlsx...

✅ Successfully fetched and saved news articles.

**📊 Example Output**
After the script finishes, you will find two new files in your project directory:
google_news_last_10_days.csv - A CSV file for use in data analysis.
google_news_last_10_days.xlsx - A well-formatted Excel file for easy viewing.
