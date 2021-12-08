import smtplib
import os
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'



def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    s = Service('D:\python\chromedriver.exe')
    driver = webdriver.Chrome(service=s,options=chrome_options)
    return driver

d = get_driver()

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos

def parse_video(video):
    title_tag = video.find_element(By.ID,'video-title')
    title_text = video.find_element(By.ID, 'video-title').text
    url = title_tag.get_attribute('href')
    thumbnail_tag = video.find_element(By.TAG_NAME,'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')
    channel_text = video.find_element(By.CLASS_NAME,'ytd-channel-name').text
    return {
        'Title': title_text,
        'Url': thumbnail_url,
        'Channel Name': channel_text
        }


if __name__ == '__main__':
    print('Creating videos')
    driver = get_driver()

    print('Fetching videos')
    videos = get_videos(driver)
    print(f'found {len(videos)} videos')
    print('parsing top 10 video')
    videos_data = [parse_video(video) for video in videos[:10]]
    print(videos_data)

    
    
    