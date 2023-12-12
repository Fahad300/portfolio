import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title("")
    content = """
    👋 Hello there! I'm a passionate UI/UX Developer on a journey to seamlessly blend design aesthetics with the power of code. Currently, I'm diving into the fascinating world of Python to enhance my skill set and broaden my capabilities.

🎨 As a UI/UX Developer, I specialize in creating intuitive and visually appealing user interfaces that prioritize the end user's experience. I believe in the power of design thinking and am dedicated to crafting solutions that not only look good but also function seamlessly.

🚀 Python has recently become a focal point in my learning journey. I'm excited about the prospect of leveraging Python to enhance my workflow, whether it's for prototyping, automating repetitive tasks, or diving into the realms of data visualization.

🔧 When I'm not immersed in the world of pixels and code, you might find me exploring the latest design trends, experimenting with new interaction patterns, or collaborating with cross-functional teams to bring ideas to life.


    """
    st.info(content)

content1 = """
    🌟 Let's connect and explore the endless possibilities at the intersection of design and technology!
    """
st.success(content1)

df = pandas.read_csv('data.csv', sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:int(len(df)/2)].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}", width=200)
        st.write(f"[Preview App]({row['url']})")

with col4:
    for index, row in df[int(len(df)/2):len(df)].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}", width=200)
        st.write(f"[Preview App]({row['url']})")