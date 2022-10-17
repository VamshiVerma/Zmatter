import streamlit as st
from super import get_tok, transcribe_tok

st.header('👩‍🎓 **ZMatter: Fetch Tiktok Insights**💡')
sam=st.empty()

sir = st.empty()

sir.markdown('**Usage Example**')

sam.success('⬆️ Awaiting URL input in the sidebar.')
war = st.empty()


war.image("https://i.postimg.cc/PJ108MpR/hack.gif")

# Sidebar
st.sidebar.header('Input parameter')

with st.sidebar.form(key='my_form'):
	URL = st.text_input('Enter URL of Tiktok video:')
	submit_button = st.form_submit_button(label='Go')

# Run custom functions if URL is entered 
if submit_button:
    war.empty()
    sam.empty()
    sir.empty()
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
