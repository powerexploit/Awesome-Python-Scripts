import praw
import pandas as pd
import datetime as dt


print("----------Set your preferences---------") 
client_id = input("Enter your client ID of Reddit app: ")
client_secret = input("Enter your client secret of Reddit app: ")
user_agent = input("Enter your user agent: ")
subreddits = input("Enter comma seperated list of subreddits you want to scrape (Jokes, soccer, news...): ").split(',')
limit = int(input("Enter how many post you want from each subreddit: "))
type_of_post = input("Enter the catergory of post you want to scrape (new,rising, hot, top, or controversial): ")

reddit = praw.Reddit(client_id=client_id, 
                    client_secret=client_secret,
                    user_agent=user_agent)  # Reddit instance


print('Now sit back and wait for process to complete...')
data = []
for sub in subreddits:
    print(f"Currently Scrapping {sub}")
    if type_of_post == 'hot':
        posts = reddit.subreddit(sub).hot(limit=limit)
    elif type_of_post == 'new':
        posts = reddit.subreddit(sub).new(limit=limit)
    elif type_of_post == 'rising':
        posts = reddit.subreddit(sub).rising(limit=limit)
    elif type_of_post == 'top':
        posts = reddit.subreddit(sub).top(limit=limit)
    elif type_of_post == 'controversial':
        posts = reddit.subreddit(sub).controversial(limit=limit)
    else:
        print("Wrong Type of post selected!")
        break
    for post in posts:
        data.append([post.id, post.author, post.title, post.score, post.subreddit, post.url, post.num_comments, post.upvote_ratio, post.selftext, post.created])


dataframe = pd.DataFrame(data, columns=['ID', 'Author', 'Title', 'Score', 'Subreddit_Name', 'Url', 'Number_of_Comments', 'Upvote_Ratio', 'Post_Body', 'Date'])
dataframe['Date'] = dataframe.Date.apply(lambda x: dt.datetime.fromtimestamp(x))
dataframe.to_csv('result.csv') 
print("Scrapping Done! Check the result.csv")