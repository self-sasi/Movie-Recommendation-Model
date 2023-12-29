# Movie Recommendation Model Readme

## Basic Functionality

The Movie Recommendation Model is designed to provide movie recommendations based on user input and the similarity scores with other entries in the dataset. Here's an overview of how the model works:

1. Data Loading: The model first analyzes and reads movie data from a CSV file (`movies.csv`).
2. Feature Selection: Feature selection is performed to choose the most relevant features for building feature vectors.
3. Feature Vectorization: The selected features are used to create feature vectors for each movie.
4. Cosine Similarity: Cosine similarity is calculated between these feature vectors to measure their similarity.
5. Recommendation Model: Using the processed information, a recommendation model is built. It takes user input and recommends movies based on their similarity scores with other entries in the dataset.

## About Files

- `reccomend.ipynb`: This notebook contains the skeleton code that demonstrates the logic and steps behind the recommendation model.
- `backend.py`: The `backend.py` file contains all the backend code and the model, with Flask implemented to create a frontend for the recommendation system.
- `index.html`: This HTML file is for testing purposes and determines how the `HTML_TEMPLATE` string variable in `backend.py` looks. It serves no functional purpose.
- `movies.csv`: This CSV file contains the dataset used to design the recommendation model.
- `static` folder: This folder contains the background image. It is placed in a static folder because Flask expects static assets like images to be stored in a designated folder.
- `LICENSE` : The project is licensed under the MIT License. This license permits reuse, distribution, modification, private use, and licensing, provided that the original authorship is credited and the license notice and warranty disclaimer are preserved with the distribution.

## How to Run the Model on Your Local Computer

### Ⅰ) Cloning the Repository:

To get started, clone the repository into a local directory on your machine using the following command in your command prompt or Git Bash:

```bash
git clone https://github.com/self-sasi/Movie-Recommendation-Model.git
```

### Ⅱ) Installing Necessary Tools:

Make sure you have Python installed on your system. Then, install the required libraries by running the following commands:

```python
pip install Flask numpy pandas scikit-learn
```

### Ⅲ) Ensuring File Organization:

Ensure that all the files are saved in the same directory to avoid file-not-found errors.

### Ⅳ) Running the Application:

Execute the `backend.py` file by running the following command in your terminal:

```bash
python backend.py
```

This should open a web page in your preferred browser. Once loaded, you can use the tool for movie recommendations.

## Screenshots and Model Insights

This section provides a visual representation of how the model works. The user is required to enter the name of a movie they want related recommendations for. 

![image](https://github.com/self-sasi/Movie-Recommendation-Model/assets/140454190/bbf4b736-508b-4f5b-b022-03b4577e487c)

After clicking the search button, the model displays 20 movie recommendations based on similarity scores.

![image](https://github.com/self-sasi/Movie-Recommendation-Model/assets/140454190/b0ada1c1-a539-4f26-8528-06ab962a8214)

Please note that clicking on the recommended movie names will not redirect the user to a different site, as this functionality was out of the target scope and not included in the project to focus on showcasing machine learning-related skills.

## Note

Please note that the functionality of the model is limited, as it was created for the purpose of showcasing machine learning skills and is not intended for commercial use. Movie recommendations are based on the dataset being used, which implies that the information may not be up-to-date.

---

## Contributions

Feel free to fork the project, submit issues and pull requests to enhance the functionalities or fix problems.
