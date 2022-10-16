import streamlit as st
import os
from time import sleep
import requests
from zipfile import ZipFile
import re
bar = st.progress(0)

# 1. API
a = "7a3f2bf87c744232930c121780d68cdb"

# 2. Retrieving audio file from YouTube video
def get_tok(inputURL):
    
    import requests
    if(len(inputURL)<=45):
        import requests
        import re

        payload = ""
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Cookie': '_abck=9B99715C1B982D72E24C5375E353DEFE~-1~YAAQxSkauDpCx5yDAQAAJWe73wj3XP0JuNIOfyedwd0MRaOeb9uAyBY0dmpuhbjl3G7qZ4bKUa0zi01xNoIUdlSNrFr5fJNr+hAjZA/nUWIYAhKPunR+t6n+VHU6TuRntjOxfVo/DOrYHiCCGSqURIeUll/lA/ku/eNPhlE1mTf/qrLSI5pjYLQIbhhoMARcSUfnIASli+mXpk8akyPE6v0RuFjSMP8HMXXhUkckCfh3YKXKm8Ois8u2NTfl46sLVed+PYoaKm0dcn1wva+dbXytdKRE4A0D8SYxhJALTAD4DKj83mlbNfr+WVQvETQ0FglyZbl7nRip0wsie8yr4qGVq0FVz/SzaMnpMlxKCYm2tzvdp4Isj5U=~-1~-1~-1; bm_sz=75A44BEE8A99C8259742183CCC9E8CE3~YAAQxSkauDtCx5yDAQAAJWe73xHBRxHRFqCz8MAtGBQnQXyHDoli7Ks/9ZDDyA5fcg20/wTeGpIcIyuNFifmH+VC1iioIyH0K90LF3pvGuLbuFNuXdjFRBRtOywM3LDkZhTj+RT4V9zav8M+KxHhqPkQXRIcc3jglsWpDMAJUaRboELomK8IGAgch6GkTiBC+B/O6RdvIwgZ96AqpWN53orpnNSNMF7Z9TxIfyJB8ChM9gDK3ibsJku8uFLO6awz2yhp5GrDhpuwSljEVVtawfIemSRZIA1yxDLNOEFRQxP1gUY=~4274225~3228473; msToken=r_BTLq4ZsN1dVedr5I1q4jUwDe74VaiXI6o7zSs1Z-teClFElWHSr1JPp6PjecQXsivc9R-WdjE7cU-65SU72gwekE8TALFtyfRlogDu0o8xetC-0mXzrtzuB1i3eYZZ; tt_csrf_token=1XQH07PK-32oWdQUnGRt7nL6BUt7E2q6ULos; ttwid=1%7CVp-VSJcengmXqnGssfT66Z8P-BKJaKT3XHKqqiG86to%7C1665906577%7C1ac7874882082b52713b4ea2b36e8ed2cf1d4699b7cd3bf642a108d97785ea29'
        }
        response = requests.request("GET", inputURL, headers=headers, data=payload)
        marker1 = 'canonical" href="'
        marker2 = '"/><'
        rx = marker1 + '(.+?)' + marker2
        inputURL = re.search(rx, response.text).group(1)
        print((inputURL))
        


    url = "https://tiktok-video-downloader.p.rapidapi.com/api/downloader"
    print(str(inputURL))
    querystring = {"url":inputURL}

    headers = {
        "X-RapidAPI-Key": "vk4hE6Nr9JmshjuBCJe3s6zaxkpnp1vZQnrjsnVyo82LaCvAw2",
        "X-RapidAPI-Host": "tiktok-video-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
    st.info('1. Audio file has been retrieved from Tiktok video')
    bar.progress(10)
    k= response.json()['data']['musicUrl']
    return k

# 3. Upload YouTube audio file to AssemblyAI
def transcribe_tok(durl):
    current_dir = os.getcwd()


    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": durl,
            "iab_categories": True,
                    "content_safety": True,
                        "entity_detection": True,
                            "auto_chapters": True,
    }
    headers = {
        "authorization": a,
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    print(response.json())

    bar.progress(25)


    st.info('2. Transcribing the Audio')
    bar.progress(40)

    # 5. Extract transcript ID
    transcription_id = response.json()['id']
    st.info('3. Calling AssemblyAI for transcript ID')
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

    st.info('4. Retrieving transcription results')
    bar.progress(60)

    # Check if transcription is complete

    st.warning('Transcription is processing ...')
    while transcript_output_response.json()['status'] != 'completed':
        sleep(2)
        bar.progress(80)
        transcript_output_response = requests.get(endpoint, headers=headers)
    
    bar.progress(100)

    # 7. Print transcribed text
    st.header('Output')
    
    with st.expander('Show Text'):
        st.success(transcript_output_response.json()["text"])

    # 8. Save transcribed text to file

    # Save as TXT file
    tok_txt = open('tok.txt', 'w')
    tok_txt.write("Tiktok to text:\n")

    tok_txt.write(transcript_output_response.json()["text"])
    tok_txt.write("\n")

    #tok_txt.success(transcript_output_response.json()["text"])


   # 9. Write JSON to app
  #  with st.expander('Show Full Results'):
   #     st.write(transcript_output_response.json())
    #tok_txt.write("----------------------------------------------------------------\n")
    #tok_txt.write("----------------------------------------------------------------\n")
    #tok_txt.write("Full Results:\n")  


    # 10. Write content_safety_labels
    with st.expander('Show summary'):
        o=(transcript_output_response.json()['chapters'])
        su= "Summary: {}".format(o[0]['summary'])
        he= "Headline: {}".format(o[0]['headline'])
        gi= "Gist: {}".format(o[0]['gist'])
        st.write(su)
        st.write(he)
        st.write(gi)
        tok_txt.write(su)
        tok_txt.write("\n")
        tok_txt.write(he)
        tok_txt.write("\n")
        tok_txt.write(gi)
        tok_txt.write("\n")

    tok_txt.write("----------------------------------------------------------------\n")
    tok_txt.write("----------------------------------------------------------------\n")
    tok_txt.write("Entities:\n")
    # 10. Write content_safety_labels
    with st.expander('Show entities'):
        for r in (transcript_output_response.json()['entities']):
            en=("{} : {}".format(r['entity_type'].capitalize(),r['text'].capitalize()))
            st.write(en)
            tok_txt.write(en)
            tok_txt.write("\n")



    tok_txt.write("----------------------------------------------------------------\n")
    tok_txt.write("----------------------------------------------------------------\n")
    tok_txt.write("Categorization:\n")

    # 10. Write content_safety_labels
    with st.expander('Show Categorization with subcategory'):
        f=(transcript_output_response.json()['iab_categories_result']['summary'])
        count=0
        for k, v in f.items():
            cat=("{} with {} matching".format(k,"%.0f%%" % (100 * v)))
            st.write(cat)
            tok_txt.write(cat)
            if(count==2):
                break
            count=count+1


    tok_txt.write("----------------------------------------------------------------\n")
    tok_txt.write("----------------------------------------------------------------\n")
    tok_txt.write("Summary of safety:\n")


    with st.expander('Summary of Safety'):

        x=(transcript_output_response.json()['content_safety_labels']['summary'])
        for k, v in x.items():
            saf=("This Tiktok has {} of {}".format(k,"%.0f%%" % (100 * v)))
            st.write(saf)
            tok_txt.write(saf)
            tok_txt.write("\n")



    tok_txt.close()

    zip_file = ZipFile('transcription.zip', 'w')
    zip_file.write('tok.txt')
    zip_file.close()
    
    # Delete processed files
    for file in os.listdir(current_dir):

        if file.endswith(".txt"):
            os.remove(file)
