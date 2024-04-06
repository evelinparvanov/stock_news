# Stock News Alert

This Python script fetches stock data using the Alpha Vantage API and news related to a specific company using the News API. If the percentage change in the stock price between yesterday and the day before yesterday is greater than or equal to 5%, it selects a random news article about the company and sends an email with the article's title and description.

## Setup

1. **Requirements**: Make sure you have Python installed on your system along with the `requests` library. You can install it using pip:

    ```bash
    pip install requests
    ```

2. **Alpha Vantage API Key**: Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key). Replace `Your API KEY` in the script with your actual API key.

3. **News API Key**: Obtain an API key from [News API](https://newsapi.org/docs/get-started). Replace `Your API KEY` in the script with your actual API key.

4. **Email Configuration**: Replace `your_email` and `your_password` in the script with your actual email credentials.

5. **Company Name and Stock Symbol**: Replace `Select company name` and `Select stock symbol` in the script with your actual company name and stock symbol.

## Usage

Run the script using Python:

```bash
python main.py
