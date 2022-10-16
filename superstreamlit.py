import streamlit as st
from super import get_tok, transcribe_tok
import re
import requests
st.markdown('# 📝 **Tiktok Insights**')

st.warning('Awaiting URL input in the sidebar.')


# Sidebar
st.sidebar.header('Input parameter')

with st.sidebar.form(key='my_form'):
        URL = st.text_input('Enter URL of Tiktok video:')
        if(len(URL)<=45):
            payload = ""
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Cookie': '_abck=9B99715C1B982D72E24C5375E353DEFE~-1~YAAQxSkauDpCx5yDAQAAJWe73wj3XP0JuNIOfyedwd0MRaOeb9uAyBY0dmpuhbjl3G7qZ4bKUa0zi01xNoIUdlSNrFr5fJNr+hAjZA/nUWIYAhKPunR+t6n+VHU6TuRntjOxfVo/DOrYHiCCGSqURIeUll/lA/ku/eNPhlE1mTf/qrLSI5pjYLQIbhhoMARcSUfnIASli+mXpk8akyPE6v0RuFjSMP8HMXXhUkckCfh3YKXKm8Ois8u2NTfl46sLVed+PYoaKm0dcn1wva+dbXytdKRE4A0D8SYxhJALTAD4DKj83mlbNfr+WVQvETQ0FglyZbl7nRip0wsie8yr4qGVq0FVz/SzaMnpMlxKCYm2tzvdp4Isj5U=~-1~-1~-1; bm_sz=75A44BEE8A99C8259742183CCC9E8CE3~YAAQxSkauDtCx5yDAQAAJWe73xHBRxHRFqCz8MAtGBQnQXyHDoli7Ks/9ZDDyA5fcg20/wTeGpIcIyuNFifmH+VC1iioIyH0K90LF3pvGuLbuFNuXdjFRBRtOywM3LDkZhTj+RT4V9zav8M+KxHhqPkQXRIcc3jglsWpDMAJUaRboELomK8IGAgch6GkTiBC+B/O6RdvIwgZ96AqpWN53orpnNSNMF7Z9TxIfyJB8ChM9gDK3ibsJku8uFLO6awz2yhp5GrDhpuwSljEVVtawfIemSRZIA1yxDLNOEFRQxP1gUY=~4274225~3228473; msToken=r_BTLq4ZsN1dVedr5I1q4jUwDe74VaiXI6o7zSs1Z-teClFElWHSr1JPp6PjecQXsivc9R-WdjE7cU-65SU72gwekE8TALFtyfRlogDu0o8xetC-0mXzrtzuB1i3eYZZ; tt_csrf_token=1XQH07PK-32oWdQUnGRt7nL6BUt7E2q6ULos; ttwid=1%7CVp-VSJcengmXqnGssfT66Z8P-BKJaKT3XHKqqiG86to%7C1665906577%7C1ac7874882082b52713b4ea2b36e8ed2cf1d4699b7cd3bf642a108d97785ea29'
            }

            response = requests.request("GET", URL, headers=headers, data=payload)

            marker1 = 'canonical" href="'
            marker2 = '"/><'
            regexPattern = marker1 + '(.+?)' + marker2
            URL = re.search(regexPattern, response.text).group(1)
        

        submit_button = st.form_submit_button(label='Go')

# Run custom functions if URL is entered 
if submit_button:
    durl=get_tok(URL)
    transcribe_tok(durl)

    with open("transcription.zip", "rb") as zip_download:
        btn = st.download_button(
            label="Download ZIP",
            data=zip_download,
            file_name="transcription.zip",
            mime="application/zip"
        )

with st.sidebar.expander('Example URL'):
	st.code('https://www.tiktok.com/@neildegrassetyson/video/7138886180099198251')

with st.sidebar.expander('Example URL'):
	st.code('https://www.tiktok.com/@therock/video/7151364108066000174')
