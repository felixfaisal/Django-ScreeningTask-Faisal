# Django Screening Task 1 
## The Web Application performs the functions as required by the problem statement 

To install this on your computer follow these steps:
1. Clone this repository and open it in your terminal 
2. Type  `pip3 install -r requirements.txt` and `pip3 install djangorestframework` 
3. In FOSSEE/settings.py change the database settings according to your mysql local server
4. Type `python3 manage.py runserver` to start the web application

The application splits only one video at a time, and every time you upload a new video all previously obtained results are destroyed<br>

# Routes
`localhost:8000` - Upload Video and Subtitle<br>
`localhost:8000/list` - List the chunks obtained after splitting the video according to subtitles<br>
`localhost:8000/api/videos` - Contains the JSON values of uploaded videos and subtitles<br>
`localhost:8000/api/chunk`- Contains the JSON values of all the chunks obtained<br> 

# Structure of my application - Files other than default django files
 `\Vsplit\`<br>
  `\spliiter.py\` - Contains functions for performing video editing which are created by me<br>
  `\forms.py\` - To create ModelForms <br>
  `\serializers.py\` - JSon serializer for API view <br><br>
  
  
# How I went about solving the project <br>
# Phase 1
* The core part of the application was to split the videos into chunks according to subtitles, and also concatenating them with the ability to change their audio
* I created python programs to accomplish the following using opencv and gstreamer but I couldn't do anything 
* After searching for various open source libraries, I stumbled upon MoviePy, It was an easy to use library for video editing
* I created a python program using MoviePy that would do the core tasks of my web application and it did 

# Phase 2
* I had to integrate this logic into a django web application, I knew basics of django but i had to watch youtube videos to get going
* After various hours of watching videos, I started developing the application at full speed with all the views and templates
* Before I write a function, I usually write it in my book and see if it's feasible 
* MoviePy could not split the video into chunks due to a pipeline error, So I started surfing for a look around to this problem 
* The problem was with the MoviePy version so I reverted it to 1.0.0 from 1.0.1 
* The video was getting split and stored in the file system and database but I could not access them 

# Phase 3
* Once the video was split, I had to display them in html which was easy to do but then i had to given an upload button to each audiofile and the  new uploaded audio file would be replacing it. 
* So I created a button for each audio file having the same name but it's value equal to the chunk of that video 
* So in the post i would retrieve the object based on the button value 
* I learnt the Django Rest framework and created two API views

# Phase 4
* I have everything working, I need to test out the upload audio function. The audio is getting uploaded fine but it is not replacing the previous audio in the video clip
* After hours of trying out various solutions, I finally got another function that would do the same for me and it worked like a charm 
* Earlier I couldn't access the files in my django filesystem so I learnt about how media_root,media_url must be configured
* I lost a lot of commits because I tried to push a video file beyond 100mb 

# Phase 5
* Started pushing code to the Repository and did a lot of minor debugging 
* Created the video of working and documentation 
* I did all of the above in a span of three days 

