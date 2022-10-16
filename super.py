import streamlit as st
import os
from time import sleep
import requests
from zipfile import ZipFile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options



bar = st.progress(0)

# 1. API
a = "7a3f2bf87c744232930c121780d68cdb"

# 2. Retrieving audio file from YouTube video
def get_tok(inputURL):
    dirx = os.getcwd()

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)

    st.info(dirx+'/chromedriver')
    #visit tiktok to mp3 converter website
    driver.get("https://ssstik.io/download-tiktok-mp3")

    #Enter url in the textbox and click submit button
    k=driver.find_element(By.XPATH,'//*[@id="main_page_text"]')
    time.sleep(2)
    k.send_keys(inputURL)
    driver.find_element(By.XPATH,'//*[@id="submit"]').click()

    #Await the download page to load
    time.sleep(4)
    #scroll down
    driver.execute_script("window.scrollTo(0, 200)") 


    #Trying to extract the link of "Download MP3 Button"
    element = driver.find_element(By.XPATH,'//*[@id="mainpicture"]/div/div/a[4]')
    k=element.get_attribute("href")
    st.info('2. Audio file has been retrieved from YouTube video')
    bar.progress(10)
    return k

# 3. Upload YouTube audio file to AssemblyAI
def transcribe_tok(durl):
    current_dir = os.getcwd()


    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": durl,
            "iab_categories": True,
                "sentiment_analysis": True,
                        "entity_detection": True,
                            "auto_chapters": True,
                                "content_safety": True





    }
    headers = {
        "authorization": a,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    print(response.json())

    bar.progress(25)


    st.info('4. Transcribing uploaded file')
    bar.progress(40)

    # 5. Extract transcript ID
    transcription_id = response.json()['id']
    st.info('5. Extract transcript ID')
    bar.progress(50)

    # 6. Retrieve transcription results
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcription_id}"
    headers = {
        "authorization": a,
    }
    transcript_output_response = requests.get(
        endpoint,
        headers=headers,
    )

    print(response.json())

    st.info('6. Retrieve transcription results')
    bar.progress(60)

    # Check if transcription is complete

    st.warning('Transcription is processing ...')
    while transcript_output_response.json()['status'] != 'completed':
        sleep(1)
        transcript_output_response = requests.get(endpoint, headers=headers)
    
    bar.progress(100)

    # 7. Print transcribed text
    st.header('Output')
    
    with st.expander('Show Text'):
        st.success(transcript_output_response.json()["text"])

    # 8. Save transcribed text to file

    # Save as TXT file
    yt_txt = open('yt.txt', 'w')
    yt_txt.write(transcript_output_response.json()["text"])
    yt_txt.close()

    # 9. Write JSON to app
    with st.expander('Show Full Results'):
        st.write(transcript_output_response.json())

    # 10. Write content_safety_labels
    with st.expander('Show summary'):
        st.write(transcript_output_response.json()["chapters"])

    # 10. Write content_safety_labels
    with st.expander('Show entities'):
        st.write(transcript_output_response.json()["entities"])

    # 10. Write content_safety_labels
    with st.expander('Show content_safety_labels'):
        st.write(transcript_output_response.json()["iab_categories_result"]['summary'])
        
    
    with st.expander('Summary of content_safety_labels'):
        st.write(transcript_output_response.json()["content_safety_labels"]["summary"])
        
    # Save as SRT file
    srt_endpoint = endpoint + "/srt"
    srt_response = requests.get(srt_endpoint, headers=headers)
    with open("yt.srt", "w") as _file:
        _file.write(srt_response.text)
    
    zip_file = ZipFile('transcription.zip', 'w')
    zip_file.write('yt.txt')
    zip_file.write('yt.srt')
    zip_file.close()
    
    # Delete processed files
    for file in os.listdir(current_dir):

        if file.endswith(".txt"):
            os.remove(file)
        if file.endswith(".srt"):
            os.remove(file)
