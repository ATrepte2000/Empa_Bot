import streamlit as st
import openai



# Configure page layout
st.set_page_config(page_title="Empa - Your Reflection Partner", page_icon="💬", layout="centered")


# Transparent background for the content
st.markdown(
    """
    <style>
    .transparent-container {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="transparent-container">', unsafe_allow_html=True)

    # Title with Emoji
    st.markdown(
        "<h1 style='text-align: center; color: #1F4E79;'>💬 Empa - Your Reflection Partner</h1>",
        unsafe_allow_html=True
    )

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)

    # Description with larger font and color
    st.markdown(
        "<h3 style='text-align: center; color: #1F4E79;'>I will help you reflect.</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Get informed about some Reflection Theory.</p>",
        unsafe_allow_html=True
    )

    # Role card in an expandable section
    with st.expander("📝 The Gibbs Reflection Cycle"):
        st.write("""
        The Gibbs Reflective Cycle is a framework for systematic reflection on experiences, developed by Graham Gibbs in 1988. It aims to help individuals learn from situations and enhance their personal or professional practices.
        The cycle comprises six stages:

Description: What happened? — Provide an objective account of the event without judgments.

Feelings: What were you thinking and feeling? — Reflect on your emotions and thoughts during the experience.

Evaluation: What was good and bad about the experience? — Assess the positive and negative aspects.

Analysis: Why did things happen this way? — Explore the reasons behind the outcomes, considering internal and external factors.

Conclusion: What else could you have done? — Summarize what you've learned and how you might have acted differently.

Action Plan: If it arose again, what would you do? — Develop a strategy for handling similar situations in the future.

This model encourages self-reflection and continuous learning, promoting growth and improvement in various fields such as education, healthcare, and management.

 """)

    # Prompt to start the conversation
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: center;'>Just start the conversation with Mr. Hurting here:</h3>",
        unsafe_allow_html=True
    )

# Footer with image or logo
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSldpssSMyDjL8BK9N7EW2gjodVa0GjsW2wVg&s" alt="Logo" width="150">
    </div>
    """,
    unsafe_allow_html=True
)



#lesen des Open AI Keys 
openai.api_key = st.secrets["openai_api_key"]

# Vollständiger Prompt für den Chatbot
bot_instructions = """
Role and Goal: - You are Salesperson, Mr. Hurtig. - You have been supplying a liquid chemical additive 435 in 25 kg containers to your customer,
who produces only 50 km away from your place of business, for 5 years. - Due to cost increases, the price of the additive needs to rise by 8%. - 
Your production department made a minor change to the composition without customer approval, expecting no issues. 
- A contamination occurred in the last delivery of 100 buckets, and the customer invited you to a complaint meeting.
- The customer uses 25 buckets per process. - Your competitor, CHEMIE AG, is approximately 300 km away and likely more expensive by an estimated 10%.
- Your customer's orders take up about 20% of your plant capacity, which equals approximately 1,200 buckets of 25 kg each per year.
- Your current sales price is EUR 6 per kilogram. Behavior: 
- Start the conversation with some small talk to build rapport.
- Engage in prolonged negotiation with the customer. 
- Acknowledge the complaint as valid due to the unapproved change in composition. 
- After addressing the refund or other concerns, always introduce and defend the need for an 8-10% price increase to avoid losses. 
- Aim to retain the customer while achieving the price increase. 
- Be skeptical, tough, and sometimes provocative or rude to challenge the customer and extend the negotiation. 
- Offer strategic bulk purchase discounts if needed, but avoid agreement below an 8% price rise. - End the relationship if the offer above 8% isn’t accepted. 
- Adjust negotiation tactics based on the customer's reactions and emotions. Guidelines: 
- Use a direct and firm tone, maintaining awareness of the customer's emotions. - Tailor arguments to the customer’s reactions. 
- Respond human-like to the customer's concerns and arguments. - Start the conversation with some small talk before addressing the main issue. 
- Remember that your role includes acting as if the negotiation were on the phone. - Avoid bullet points and do not give long answers. Clarification: 
- Ask for clarification if unsure about the customer’s responses or concerns.
"""

# Initialisiere den Sitzungszustand nur beim ersten Start
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": bot_instructions}]

# Zeige bisherige Benutzer- und Assistenten-Nachrichten an (ohne den system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat-Eingabefeld für Benutzernachrichten
if user_input := st.chat_input("..."):
    # Benutzer-Nachricht hinzufügen
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # API-Anfrage zur Generierung der Antwort basierend auf der Konversation
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Das gewünschte Modell angeben, z.B. "gpt-3.5-turbo" oder "gpt-4"
            messages=st.session_state.messages,
            temperature=0.5
            # max_tokens=50 könnte man noch reinnehmen, bei Bedarf.
     
        )

        # Extrahiere die Antwort
        assistant_response = response.choices[0].message.content
        
        # Antwort anzeigen und im Sitzungszustand speichern
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error("Ein Fehler ist aufgetreten. Bitte überprüfe die API-Konfiguration oder versuche es später erneut.")
        st.write(e)

import streamlit as st
import openai
import json
import os

# ... Dein bisheriger Code ...

# Füge diesen Code am Ende deiner Datei hinzu, nachdem die Antwort des Chatbots angezeigt wurde

# Erstelle einen Ordner zum Speichern der Konversationen, falls nicht vorhanden
if not os.path.exists('conversations'):
    os.makedirs('conversations')

# Generiere einen eindeutigen Dateinamen für jede Sitzung
session_id = st.session_state.get('session_id', None)
if session_id is None:
    import uuid
    session_id = str(uuid.uuid4())
    st.session_state['session_id'] = session_id

# Pfad zur Konversationsdatei
conversation_file = f'conversations/conversation_{session_id}.txt'

# Speichere die Konversation in der Datei
with open(conversation_file, 'w') as f:
    for message in st.session_state.messages:
        if message['role'] != 'system':
            f.write(f"{message['role'].capitalize()}: {message['content']}\n\n")


# Füge diesen Code an einer geeigneten Stelle in deiner App hinzu, z.B. am Ende

# Konversation als Text zusammenfassen
conversation_text = ""
for message in st.session_state.messages:
    if message['role'] != 'system':
        conversation_text += f"{message['role'].capitalize()}: {message['content']}\n\n"

# Download-Button anzeigen
st.download_button(
    label="📥 Konversation herunterladen",
    data=conversation_text,
    file_name='konversation.txt',
    mime='text/plain'
)
