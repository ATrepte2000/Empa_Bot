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
        "<h3 style='text-align: center;'>Start your Refelction Journey here:</h3>",
        unsafe_allow_html=True
    )

# Footer with image or logo
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <img src="data:image/jpeg;base64,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s" alt="Logo" width="150">
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
