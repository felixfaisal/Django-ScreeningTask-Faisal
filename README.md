# Django Screening Task 1 
## The Web Application performs the functions as required by the problem statement 

To install this on your computer follow these steps:
1. Clone this repository and open it in your terminal 
2. Type  `pip3 install -r requirements.txt` 
3. In FOSSEE/settings.py change the database settings according to your mysql local server
4. Type 'python3 manage.py runserver' to start the web application

The application splits only one video at a time, and every time you upload a new video all previously obtained results are destroyed<br>

localhost:8000 - Upload Video and Subtitle<br>
localhost:8000/list - List the chunks obtained after splitting the video according to subtitles<br>
localhost:8000/api/videos - Contains the JSON values of uploaded videos and subtitles<br>
localhost:8000/api/chunk - Contains the JSON values of all the chunks obtained<br> 
