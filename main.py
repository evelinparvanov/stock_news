import requests
import smtplib
import random


my_email = "your_email"
password = "your_password"

COMPANY_NAME = "Select company name"
ALPHAVANTAGE_END_POINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API = "Your API KEY"
STOCK = "Select stock symbol"
NEWS_API = "Your API KEY"
NEWS_END_POINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API,
}

news_parameters = {
    "apiKey": NEWS_API,
    "q": COMPANY_NAME,
    "language": "en",
    "pageSize": 3
}

try:
    stock_request = requests.get(ALPHAVANTAGE_END_POINT, params=stock_parameters)
    stock_request.raise_for_status()
    stock_data = stock_request.json()["Time Series (Daily)"]
    stock_data_list = [value for (key, value) in stock_data.items()]
    stock_info_yesterday = float(stock_data_list[0]["4. close"])
    stock_info_day_before_yesterday = float(stock_data_list[1]["4. close"])

    percentage_change = ((stock_info_yesterday - stock_info_day_before_yesterday) / stock_info_day_before_yesterday) * 100

    if abs(percentage_change) >= 5:

        news_request = requests.get(NEWS_END_POINT, params=news_parameters)
        news_request.raise_for_status()
        articles = news_request.json()["articles"]
        news_for_stock = []

        for article in articles:
            news_for_stock.append({article["title"]: article["description"]})

        # Extract titles and descriptions from the list of dictionaries
        titles_descriptions = [(article["title"], article["description"]) for article in articles]

        # Select a random article
        selected_article = random.choice(titles_descriptions)
        percentage_change_str = str(percentage_change)
        sign = '\U0001F53A' if percentage_change > 0 else '\U0001F53B'
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject: {COMPANY_NAME} {sign} {percentage_change:.2f}% \n\n"
                                    f"Title: {selected_article[0]}\n"
                                    f"Description: {selected_article[1]}")
    else:
        print("Percentage change is less than 5%. No email sent.")
    print("Stock Information for Yesterday:", stock_info_yesterday)
    print("Stock Information for the Day Before Yesterday:", stock_info_day_before_yesterday)

except Exception as e:
    print(f"An error occurred: {str(e)}")
