from flask import Flask, request, jsonify, send_file
from flask_cors import CORS  # Import CORS
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        return title.text.strip() if title else ""
    except AttributeError:
        return ""

def get_price(soup):
    try:
        # Attempt to find the main price
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'})
        if price:
            return price.string.strip()
        
        # If the main price is not found, attempt to find the deal price
        price = soup.find("span", attrs={'id': 'priceblock_dealprice'})
        if price:
            return price.string.strip()
        
        # If no price is found, return a default message
        return "Price not available"
    except Exception:
        return "Price not available"

def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            return ""
    return rating

def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        return ""
    return review_count

def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        return available.find("span").string.strip() if available else "Not Available"
    except AttributeError:
        return "Not Available"

@app.route('/scrape', methods=['GET'])
def scrape():
    search_query = request.args.get('query', '')
    HEADERS = {'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'}
    URL = f"https://www.amazon.com/s?k={search_query}"

    try:
        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")

        links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
        links_list = ["https://www.amazon.com" + link.get('href') for link in links]

        data = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}

        for link in links_list:
            new_webpage = requests.get(link, headers=HEADERS)
            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            data['title'].append(get_title(new_soup))
            data['price'].append(get_price(new_soup))
            data['rating'].append(get_rating(new_soup))
            data['reviews'].append(get_review_count(new_soup))
            data['availability'].append(get_availability(new_soup))

        amazon_df = pd.DataFrame.from_dict(data)
        amazon_df['title'].replace('', np.nan, inplace=True)
        amazon_df.dropna(subset=['title'], inplace=True)

        # Save the DataFrame to a CSV file
        csv_file = 'scraped_data.csv'
        amazon_df.to_csv(csv_file, index=False)

        # Return the DataFrame as JSON response and also allow downloading the CSV file
        return jsonify({
            'data': amazon_df.to_dict(orient='records'),
            'download_url': f'/download/{csv_file}'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return error message if something goes wrong

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
