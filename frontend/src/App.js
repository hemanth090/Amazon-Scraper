import React, { useState } from 'react';
import axios from 'axios';
import { TailSpin } from 'react-loader-spinner';
import './App.css'; // Import your CSS file

function App() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSearch = async () => {
        setError('');
        setLoading(true);
        try {
            const response = await axios.get(`http://localhost:5000/scrape?query=${encodeURIComponent(query)}`);
            console.log("Response Data:", response.data);
            setResults(response.data.data); // Update results
        } catch (error) {
            console.error("Error fetching data", error);
            setError('Failed to fetch data. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="background">
            <h1 className="text-4xl font-bold mb-6 text-blue-600 text-center">Amazon Scraper</h1>
            <div className="flex mb-6">
                <input
                    type="text"
                    placeholder="Search for products"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    className="border border-gray-300 rounded-l-lg p-2"
                />
                <button
                    onClick={handleSearch}
                    className="bg-blue-500 text-white rounded-r-lg p-2 hover:bg-blue-600"
                >
                    Search
                </button>
            </div>
            {loading ? (
                <TailSpin
                    height="80"
                    width="80"
                    color="#4fa94d"
                    ariaLabel="tail-spin-loading"
                    radius="1"
                    visible={true}
                />
            ) : error ? (
                <p className="text-red-500">{error}</p>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {results.length === 0 ? (
                        <p className="text-center text-gray-600">No products found.</p>
                    ) : (
                        results.map((item, index) => (
                            <div key={index} className="bg-white shadow-md rounded-lg p-4">
                                <h2 className="text-lg font-semibold">{item.title}</h2>
                                <p className="text-gray-600">Price: {item.price || "Price not available"}</p>
                                <p className="text-gray-600">Rating: {item.rating}</p>
                                <p className="text-gray-600">Reviews: {item.reviews}</p>
                                <p className="text-gray-600">Availability: {item.availability}</p>
                            </div>
                        ))
                    )}
                </div>
            )}
        </div>
    );
}

export default App;
