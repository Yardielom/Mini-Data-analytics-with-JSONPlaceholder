from pipelines_utils import PipelinesUtils

print("\n" + "=" * 60)
print("MINI DATA ANALYTICS WITH JSONPLACEHOLDER".center(60))
print("=" * 60 + "\n")

# 1. Creates the pipeline object
pipeline = PipelinesUtils()
# 2. Fetch data from the API
pipeline.fetch_data()
# 3. Create the DataFrames from JSON
pipeline.extract()
# 4. Merge the datasets for better analysis
pipeline.merge_data()

# 5. Calculate and print metrics
print("\n======== Posts per user =========")
pipeline.posts_per_user()

print("\n======== Average comments per post ========")
pipeline.avg_comment_per_post()

print("\n======== Percentage of completed TODOs ========")
pipeline.percent_todos_completed()

print("\n======== Top 5 most commented posts =========")
pipeline.top_5_commented_posts()

# 6. Visualizations
pipeline.user_activity() # Bar chart for posts per user

pipeline.percent_completed_todos_chart() # Pie chart for completed TODOs

pipeline.top_5_commented_posts_chart() # Bar chart for top 5 posts