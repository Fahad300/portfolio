import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title("Lorem Ipsum")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquam fermentum sapien et vestibulum. Mauris 
    fermentum ut neque auctor hendrerit. Vestibulum placerat, justo sed suscipit ultrices, elit justo efficitur justo, 
    non convallis lorem diam ac orci. Aliquam at venenatis purus. Nullam ultrices est vel aliquam rutrum. Sed a magna 
    at velit dictum molestie sagittis in ligula. Ut ac erat in nulla laoreet sagittis. Sed eu turpis nisl. Aliquam erat 
    volutpat. Maecenas eget accumsan leo. Morbi porta, odio in dignissim iaculis, risus eros dignissim elit, sit amet 
    porttitor mauris justo id tellus.
    
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquam fermentum sapien et vestibulum. Mauris 
    fermentum ut neque auctor hendrerit.
    """
    st.info(content)