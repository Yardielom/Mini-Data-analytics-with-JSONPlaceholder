# Mini-Data-analytics-with-JSONPlaceholder
## Description
This project fetches data from the public API [JSONPlaceholder](https://jsonplaceholder.typicode.com) and performs simple data analysis. It calculates metrics on user posts, comments, and TODO tasks, and visualizes results using Python and Matplotlib.  
The project is implemented using **Object-Oriented Programming (OOP)**, with a pipeline class that handles data fetching, transformation, merging, analysis, and visualization.

## Features
- Fetches data from multiple endpoints: `users`, `posts`, `comments`, `todos`
- Transforms JSON data into pandas DataFrames
- Merges datasets for relational analysis
- Calculates metrics:
  - Number of posts per user
  - Average comments per post
  - Percentage of completed TODOs per user
  - Top 5 most commented posts
- Generates visualizations:
  - Bar chart: user activity (posts per user)
  - Pie chart: percentage of completed TODOs
  - Bar chart: top 5 most commented posts

## Installation
1. Clone the repository:
   - Run in the terminal:
        - git clone https://github.com/Yardielom/Mini-Data-analytics-with-JSONPlaceholder.git
2. Install dependencies:
   - Run in the terminal:
      -  pip install -r requirements.txt
## Usage
  - Run in the terminal:
      python main.py
    
   Metrics will be printed in the console and charts displayed using Matplotlib, you will first see only one of the charts, but you just have to press on the "X" on the pop up window that will appear and the next chart will show.
## AI Usage
ChatGPT was used to:
- Debug issues and fix errors in the code
- Improve code readability and maintainability
- Help write documentation and explain the project structure
## Jupyter Notebook Version
Before creating the final OOP based version in PyCharm, I developed this project in a Jupyter Notebook. 
The notebook contains the step by step workflow, data exploration, metric calculations, and visualizations.
It shows how my project went from the notebook to the final structured implementation.
You can open and run it in Jupyter Lab/Notebook to see how the project evolved.
