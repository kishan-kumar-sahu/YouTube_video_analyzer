from youtube_analyzer import  build_analyzer_agent

import streamlit as st



st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"
)

st.title(" 🎥 AI YouTube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_analyzer_agent()

agent = get_agent()


#  inout box 

video_url=st.text_input(
    "Enter Youtube URL",
     placeholder="https://www.youtube.com/watch?v=..."
    )



# --------------------------
# Analyze button
# --------------------------

button = st.button(
    "🔍 Analyze Video"
)


if video_url and button:
    with st.spinner("Analyzing video...."):
        response=agent.run(
            f"Analyze this video:{video_url}"  
                    )
         
     



    # print(response.content)
    st.markdown("Analysis  Report of video : ")
    st.markdown(response.content)
