from Dictionary_Generator_Output import backbone
import streamlit as st
from streamlit_carousel import carousel

# Convert the list of dictionaries to a language-keyed dictionary
backbone_dict = {entry['language']: entry for entry in backbone}

# 'RO' as the default language and initiating the st.session_state
if 'selected_language' not in st.session_state:
    st.session_state['selected_language'] = 'RO'

# Sidebar for language selection
with st.sidebar:
    for lang_code in backbone_dict.keys():
        if st.button(backbone_dict[lang_code]['language'], key=lang_code):
            st.session_state['selected_language'] = lang_code


# Access the selected entry directly
selected_entry = backbone_dict[st.session_state['selected_language']]

# Image Carousel

test_items = [
    dict( title= "" ,
          text = "",
          img="Isus_Pantokrator.png",
          link = ""

    ),
    dict( title= "",
          text = "",
        img="Manastirea_Sinaia.jpg",
          link = ""

    ),
    dict( title= "",
          text = "",
        img="Manastirea_Sinaia_1.jpg",
          link = ""
    ),
]

# Display the content
carousel(items=test_items, width=1.5)
st.title(selected_entry['title'])
st.write(selected_entry['intro'])
if selected_entry['audio'] != 'None':
    st.audio(selected_entry['audio'])





# # QR code 
# qr = qrcode.make('http://192.168.0.34:8501/')
# qr.save('/Users/tiberiuradan/Desktop/QR/Demo.png')
