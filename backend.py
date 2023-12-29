from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import webbrowser
import threading

app = Flask(__name__)

HTML_TEMPLATE = """ <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modern Movie Search</title>
  <style>
    :root {
      --primary-color: #0f9;
      --text-color: #e0e0e0;
      --bg-color: black; 
      --container-bg-color: rgba(0, 0, 0, 0.85);
      --box-shadow-color: rgba(15, 255, 150, 0.2); 
      --border-color: #0f9; 
      --hover-effect: brightness(1.2);
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      background-image: url('/static/background.jpg');
      background-size: cover; 
      background-position: center; 
      background-repeat: no-repeat; 
    }

    .container {
      width: 90%;
      max-width: 800px;
      background-color: var(--container-bg-color);
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 4px 8px var(--box-shadow-color);
      text-align: center;
      border: 1px solid var(--border-color);
    }

    h2 {
      color: var(--primary-color);
      text-shadow: 0 0 5px var(--primary-color);
    }

    .search-bar {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 2rem;
    }

    input[type="text"] {
      flex: 1;
      padding: 0.5rem;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      outline: none;
      background: #0a101e;
      color: var(--text-color);
    }

    .search-button {
      background-color: var(--primary-color);
      color: var(--container-bg-color);
      border: none;
      border-radius: 8px;
      padding: 0.5rem 1rem;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    .search-button:hover {
      filter: var(--hover-effect);
    }

    .movie-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 1rem;
    }

    .movie-box {
      background-color: var(--container-bg-color);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1rem;
      box-shadow: 0 4px 8px var(--box-shadow-color);
      transition: transform 0.3s;
    }

    .movie-box:hover {
      transform: scale(1.05);
      box-shadow: 0 0 10px var(--primary-color);
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Find Your Favorite Movie</h2>
    <div class="search-bar">
      <input type="text" placeholder="Enter a movie" id="movie-input">
      <button class="search-button" onclick="searchMovies()">Search</button>
    </div>
    <div class="movie-container" id="movie-list">
      
    </div>
  </div>

  <script>
    function searchMovies() {
      const movieInput = document.getElementById("movie-input").value;
  
      fetch('/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ movie: movieInput }),
      })
      .then(response => response.json())
      .then(data => {
        const movieList = document.getElementById("movie-list");
        movieList.innerHTML = "";  // Clear existing movies
  
        data.forEach(movie => {
          const movieBox = document.createElement("div");
          movieBox.classList.add("movie-box");
          movieBox.textContent = movie;
          movieList.appendChild(movieBox);
        });
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  </script>
  

</body>
</html>
 """


# Load movie data
m_data = pd.read_csv('movies.csv')
r_f = ['genres', 'keywords', 'tagline', 'original_title', 'director', 'cast']

for feature in r_f:
    m_data[feature] = m_data[feature].fillna('')

# Prepare the content for vectorization
content = m_data['genres'] + ' ' + m_data['keywords'] + ' ' + m_data['tagline'] + ' ' + m_data['original_title'] + ' ' + m_data['director'] + ' ' + m_data['cast']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(content)
sim_score = cosine_similarity(X)

def recommendMovies(user_input):
    movie_name_list = m_data['title'].tolist()
    match = difflib.get_close_matches(user_input, movie_name_list, n=1)
    
    if not match:
        return ["No match found. Try another movie name."]
    
    match = match[0]  # Get the closest match
    index = m_data[m_data.title == match]['index'].values[0]

    sim_movies = list(enumerate(sim_score[index]))
    sorted_sim_movies = sorted(sim_movies, key=lambda x: x[1], reverse=True)

    recommend_title_list = []
    recommend_homepage_list = []
    for i in sorted_sim_movies[1:21]:  # Skip the first (self) and take the next 20
        index = i[0]
        title = m_data.at[index, 'title']
        homepage = m_data.at[index, 'homepage']
        recommend_title_list.append(title)
        recommend_homepage_list.append(homepage)
        
    return recommend_title_list, recommend_homepage_list

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_input = data['movie']
    recommendations = recommendMovies(user_input)[0]
    homepage = recommendMovies(user_input)[1]
    return jsonify(recommendations)

@app.route('/')
def home():
    return HTML_TEMPLATE

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)