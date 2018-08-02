import time
import datetime
import pyodbc
import urllib
from selenium import webdriver
import json
import requests
import PIL.ImageGrab


channel_id = "enter channel id"
key = "enter key"
number_of_popular_videos = "50"

search_channel = "https://www.googleapis.com/youtube/v3/channels?id=UC_x5XG1OV2P6uZZ5FSM9Ttw&part=snippet%2CcontentDetails%2Cstatistics&key=" + key


print (search_channel)




