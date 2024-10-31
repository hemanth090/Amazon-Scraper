
# Amazon Scraper

![image](https://github.com/user-attachments/assets/3e63c960-76e4-4351-a58f-c59b5d695320)

An Amazon Scraper web application built with a frontend using Tailwind CSS and React, and a backend powered by Python. This tool allows users to scrape product details from Amazon, enabling data analysis or gathering insights.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- Scrapes Amazon product data
- Responsive frontend UI
- Real-time data fetching and display
- Easy-to-install and customizable

## Project Structure

### Frontend

- **package.json**: Lists the frontend dependencies.
- **tailwind.config.js** & **postcss.config.js**: Configuration files for styling with Tailwind CSS.
- **src/**: Contains the main React components and pages for the application.

### Backend

- **app.py**: Contains the main backend logic for scraping Amazon data.
- **requirements.txt**: Lists Python packages required for the backend.

## Setup

### Prerequisites

Ensure you have the following installed:
- [Node.js](https://nodejs.org/) and npm for the frontend
- [Python 3](https://www.python.org/) for the backend

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend server:
   ```bash
   npm start
   ```

### Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python app.py
   ```

## Usage

1. Open your web browser and navigate to the frontend URL (usually `http://localhost:3000`).
2. Enter the product URL or search term to scrape data.
3. View and analyze the scraped data directly from the web interface.

## Technologies Used

- **Frontend**: React, Tailwind CSS
- **Backend**: Python, Flask (or another backend framework depending on app.py implementation)
- **Other**: Node.js, npm, Virtual Environment (Python)

## License

This project is licensed under the MIT License.
