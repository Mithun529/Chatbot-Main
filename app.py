import os
import streamlit as st

from groq import Groq

#create a Groq object
key=st.secrets["api_key"]
client = Groq(api_key= key)
st.title('Groq Streamlit Example')
st.write('Please ask anything to me')

def main():
    message=st.text_input('Write the Questions here')
    if st.button('submit'):
        st.write('You asked: ', message)

        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                        {
                        "role": "user",
                        "content": message,
                        }
                    ],
                        
        )
        if chat_completion:
            st.write('Bot'+ chat_completion.choices[0].message.content)
        else:
            st.write('No Message Found')

if __name__ == '__main__':
    main()
