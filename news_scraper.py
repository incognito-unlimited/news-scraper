import pandas as pd
from pygooglenews import GoogleNews
from bs4 import BeautifulSoup

def clean_html(raw_html):
    """
    Removes HTML tags from a string.
    """
    if not raw_html:
        return ""
    try:
        # Use BeautifulSoup to parse and get text
        soup = BeautifulSoup(raw_html, 'html.parser')
        return soup.get_text()
    except Exception as e:
        print(f"Error cleaning HTML: {e}")
        return raw_html # Return original if cleaning fails

def fetch_google_news(categories, time_period='10d'):
    """
    Fetches news articles for given categories using the search function.
    """
    print("Initializing Google News client...")
    # Initialize GoogleNews client
    # You can change 'IN' to your preferred country code (e.g., 'US', 'GB')
    gn = GoogleNews(lang='en', country='IN') 
    
    all_articles = []

    for user_category, search_term in categories.items():
        print(f"Fetching news for category: {user_category} (Search: '{search_term}')...")
        try:
            # We use gn.search() which supports the 'when' parameter
            search_results = gn.search(query=search_term, when=time_period)

            if not search_results['entries']:
                print(f"No articles found for {user_category}.")
                continue

            # Process each article
            for entry in search_results['entries']:
                article = {
                    'News Headline': entry.title,
                    'News Content / Summary': clean_html(entry.summary),
                    'News Website Link (URL)': entry.link,
                    'Published Date': entry.published,
                    'Category': user_category 
                }
                all_articles.append(article)
        
        except Exception as e:
            print(f"Error fetching news for {user_category}: {e}")

    print(f"Total articles fetched: {len(all_articles)}")
    return all_articles

# --- Main execution ---
if __name__ == "__main__":
    
    # 1. DEFINE CATEGORIES
    categories_to_fetch = {
        '🖥️ Technology': 'Technology',
        '🎬 Entertainment': 'Entertainment',
        '🏅 Sports': 'Sports',
        '🔬 Science': 'Science',
        '💊 Health': 'Health'
    }

    # 2. FETCH NEWS
    articles_list = fetch_google_news(categories_to_fetch, time_period='10d')

    if articles_list:
        # 3. CREATE DATAFRAME
        print("Creating DataFrame...")
        df = pd.DataFrame(articles_list)

        # 4. CLEAN DATA
        print("Converting dates...")
        
        # Convert to timezone-aware datetime
        df['Published Date'] = pd.to_datetime(df['Published Date'], utc=True, errors='coerce')
        df = df.dropna(subset=['Published Date'])

        # Sort by date, newest first
        df = df.sort_values(by='Published Date', ascending=False)
        
        # Drop duplicates, keeping the first occurrence
        df = df.drop_duplicates(subset=['News Headline', 'News Website Link (URL)'], keep='first')

        # --- FIX FOR EXCEL ---
        print("Removing timezone info for Excel compatibility...")
        # We make the datetimes "naive" (remove timezone) so Excel can read them
        df['Published Date'] = df['Published Date'].dt.tz_localize(None)
        # --- END OF FIX ---
        
        # Re-order columns to match the request
        df = df[[
            'Category',
            'Published Date',
            'News Headline', 
            'News Content / Summary', 
            'News Website Link (URL)'
        ]]

        # 5. EXPORT TO FILES
        csv_filename = 'google_news_last_10_days.csv'
        excel_filename = 'google_news_last_10_days.xlsx'

        # Export to CSV (using utf-8-sig for better Excel compatibility)
        print(f"Saving to {csv_filename}...")
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

        # Export to Excel (This will now work)
        print(f"Saving to {excel_filename}...")
        df.to_excel(excel_filename, index=False, engine='openpyxl') # <-- TYPO FIXED

        print("\n✅ Successfully fetched and saved news articles.")
        print(f"DataFrame shape: {df.shape}")
        print("\n--- DataFrame Head ---")
        print(df.head())
    
    else:
        print("No articles were fetched. Exiting.")