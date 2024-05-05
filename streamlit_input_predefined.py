import streamlit as st
from blogpost import blogposts


st.set_page_config(page_icon="B", layout="wide")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

p=0
if p<1:
    icon("Blog Post Writer")

    st.subheader("Let AI agents write catchy blogs for you!",
                 divider="rainbow", anchor=False)

t = 0
p=p+1
while (t<1):
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            trip_crew = blogposts()
            result = trip_crew.newblogpost()
        status.update(label="✅ Blog posts are ready!",
                      state="complete", expanded=True)

    st.subheader("Here is the blog on AI advancements", anchor=False, divider="rainbow")
    st.markdown(result)
    t=t+1

