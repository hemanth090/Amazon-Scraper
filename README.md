# Amazon Product Scraper

This application allows users to search for Amazon products based on a query and displays key product information including title, price, rating, review count, and availability. It consists of a frontend built in React and a backend using Flask for data scraping from Amazon.

## Features

- **Product Search:** Search Amazon for products by keyword.
- **Data Scraping:** Extracts product details from Amazon such as title, price, rating, review count, and availability.
- **Downloadable Data:** Exports scraped data as a CSV file.

## Project Structure

- `frontend/`: Contains the React frontend code.
- `backend/`: Contains the Flask API for web scraping.

## Prerequisites

- **Frontend**: Node.js and npm installed
- **Backend**: Python 3.x, Flask, and required dependencies installed

## Setup and Installation

### Backend

1. **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd backend
    ```

2. **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask server**:
    ```bash
    python app.py
    ```
   The backend will run at `http://localhost:5000`.

### Frontend

1. **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

3. **Start the React app**:
    ```bash
    npm start
    ```
   The frontend will run at `http://localhost:3000`.

## Usage

1. Enter a product keyword in the search bar and click "Search."
2. View product details including title, price, rating, review count, and availability.
3. Download the data as a CSV file by clicking the download link.

## Technologies Used

- **Frontend**: React, Tailwind CSS
- **Backend**: Flask, BeautifulSoup, Pandas
- **Data Scraping**: Requests, BeautifulSoup

## License

This project is licensed under the MIT License.

