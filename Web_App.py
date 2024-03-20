from Dictionary_Generator_Output import backbone
import streamlit as st

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

# Display the content
st.image('Isus_Pantokrator.png', use_column_width=True)
st.title(selected_entry['title'])
st.write(selected_entry['intro'])
if selected_entry['audio'] != 'None':
    st.audio(selected_entry['audio'])





# # QR code generation (you might want to move this to a more appropriate place in your code)
# qr = qrcode.make('http://192.168.0.34:8501/')
# qr.save('/Users/tiberiuradan/Desktop/QR/Demo.png')
