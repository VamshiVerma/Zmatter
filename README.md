
# [ZMATTER](http://Zmatter.tech)

# Inspiration
The pandemic altered Genz's approach to schooling. Top creators on social media platforms aren't there because of their educational background or certifications. Their expertise and capacity to convincingly demonstrate what they are teaching are what give them authority and influence. It’s like a "pink elephant in the room." Nobody discusses it. Students also get major learning from social platforms. But, what about the time to watch all those videos on social platforms, THO? Seems like a lot of content. Time matters for a continuous learner. Also, we save a lot of videos to watch later, but do we really watch all those videos? Also, in low internet connectivity areas, one could not watch many videos to grasp the content in them. What about teachers who want to provide new content to students, social platforms have a lot of it. "WHAT IF WE HAVE A SOLUTION THAT REDUCES THE “TIME & INTERNET USAGE” TO GRASP FROM ALL VIDEOS OF EDUCATIONAL CONTENT?"

# What it does
It'll extract the insights from the TikTok video. Once we input the video URL, it would serve as input to the Assembly AI where we extracted the Transcription, Summary, Entity Detection, Sentiment Analysis, NSFW, and explicit content detection. The results are then displayed through the Streamlight Application.

# Features
Input: Accepts both shortened TikTok URLs and web URLs
Assembly AI: Uses Assembly AI for transcription, summary, entity detection, sentiment analysis, NSFW, and explicit content detection
Output: Displays results through a Streamlit UI
# How we built it
We've leveraged the AssemblyAI to transcribe the audio to text. We've used the python libraries to work on the data ETL methods. Our way of process is to fetch the desired Tiktok video we want to extract the insights. Then the video URL webpage is scraped and the downloadable mp4 link hosted at TiktokCDN is extracted. This video URL would serve as input to the Assembly AI where we extracted the Transcription, Summary, Entity Detection, Sentiment Analysis, NSFW, and explicit content detection. The results are then displayed through the Streamlight Application. We've deployed the application on the Streamlit application and it's a mobile-friendly application we've hosted it on Zmatter.tech

# Challenges we ran into
# Challenge 1: 
 The first major challenge we faced is there is no public TikTok API available. The API provided by Tiktok is selective and restricted it takes a couple of days to review and provide the API Keys. The challenge is to find the downloadable mp4 or mp3 direct URLs to serve as input to assembly. Tiktok make sure it doesn't facilitate that details when we tried to capture the API calls that are making communication at the tiktok.com through chrome network console but the TikTok had the internal mechanism to restrict the calls made through the.
# Challenge 2: 
Now, we tried to scrape the data from the external Tiktok to the MP3-converting websites through web scraping but they had the blockers set for the automatic bots. We are on the brink of losing hope but we didn't give up after 27hrs of issues we figured out to fix the issue.
# Challenge 3: 
The Biggest Issue of all is sharing videos on TikTok that are shortened as URLs but our mechanism is based on web URLs, the task is to translate to the full web URL to facilitate the work. So, we retrieved the GET request that converts a short URL to an actual URL after hours of intensive research.

# Accomplishments that we're proud of
We are proud of addressing a major problem for students who are curious to gain knowledge from various videos available online. Also, in countries where there is less internet connectivity, this app could help many curious people to learn from any given TikTok video without watching.

* Addresses a major problem for students and learners to gain knowledge from online videos
* Successful deployment of an end-to-end product development
* Input capability for both shortened TikTok URLs and web URLs

# Future plans
* Expansion to other media platforms like YouTube and Instagram
* Providing insights for a user's entire profile with headline and gist
* Turning into a small-scale startup to help students with education and more.
* The application is deployed and hosted on [ZMATTER](http://Zmatter.tech) and is mobile-friendly.

