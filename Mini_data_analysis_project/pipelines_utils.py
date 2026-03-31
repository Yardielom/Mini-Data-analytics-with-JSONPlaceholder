import pandas as pd
import requests
import matplotlib.pyplot as plt

class PipelinesUtils():
    def __init__(self):
        self.comments = None
        self.todos = None
        self.posts = None
        self.users = None

    def fetch_data(self):
        self.users = requests.get("https://jsonplaceholder.typicode.com/users").json()
        self.posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
        self.todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
        self.comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()

    def extract(self):
        # Converting the (JSON) lists into DataFrames
        self.users_df = pd.DataFrame(self.users)
        self.posts_df = pd.DataFrame(self.posts)
        self.todos_df = pd.DataFrame(self.todos)
        self.comments_df = pd.DataFrame(self.comments)
        # Some columns in the users df had nested dictionaries, by doing this they become separate columns
        self.users_df = pd.json_normalize(self.users)

    def merge_data(self):
        self.users_posts_merged = self.users_df.merge(self.posts_df, how='left', left_on='id', right_on='userId', suffixes=['_user', '_post'])
        self.posts_and_comments = self.posts_df.merge(self.comments_df, how='left', left_on='id', right_on='postId', suffixes=['_posts', "_comments"])
        self.users_todos_merged = self.users_df.merge(self.todos_df, how='left', left_on='id', right_on='userId', suffixes=['_user', "_todo"])

    def posts_per_user(self):
        # Group by name and count the id_post
        self.posts_per_user = self.users_posts_merged.groupby('name')['id_post'].count()
        print(self.posts_per_user)

    def avg_comment_per_post(self):
        # Group all comments by the post they belong and then .count() counts all the comments per post
        self.comments_per_posts = self.posts_and_comments.groupby('postId').size()
        self.avg_comments = self.comments_per_posts.mean()
        print(self.avg_comments)
    def percent_todos_completed(self):
        # Filter only completed TODOs
        # Then group by user name and count how many tasks each user has completed
        self.completed_todos = self.users_todos_merged[self.users_todos_merged['completed'] == True] \
            .groupby('name')['completed'].count()
        # Count the total TODOs per user
        self.total_todos_per_user = self.users_todos_merged.groupby('name')['id_todo'].count()
        # Then get the percentage of the completed TODOs
        self.percentage_todos_completed = (self.completed_todos / self.total_todos_per_user) * 100
        print(self.percentage_todos_completed)
    def top_5_commented_posts(self):
        # Sort posts by number of comments and then printing the top 5 using .head(5)
        self.top_5 = self.comments_per_posts.sort_values(ascending=False).head(5)
        print(self.top_5)
    def user_activity(self):
        # Create a bar chart showing the number of posts per user
        self.posts_per_user.plot(kind='bar', color='skyblue')
        plt.title('User activity')
        plt.ylabel('Number of posts per user')
        plt.xlabel('User name')
        # Rotates the names for readability
        plt.xticks(rotation=45)
        # Add horizontal grid lines for easier visualization
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    def percent_completed_todos_chart(self):
        # Creates a pie chart showing the percentage of completed TODOs per user, autopct is used to show the porcentages on the slices, and startangle is used for a better layout
        self.percentage_todos_completed.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
        plt.title('Percentage of tasks completed')
        plt.ylabel('')
        plt.show()
    def top_5_commented_posts_chart(self):
        # Create a bar chart showing the top 5 posts with the most comments
        self.top_5.plot(kind='bar', color='green')
        plt.title('Top 5 most commented posts')
        plt.ylabel('Number comments')
        plt.xlabel('Post ID')
        # Keep x-axis labels horizontal for readability
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()