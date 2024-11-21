import streamlit as st
import openai



# Configure page layout
st.set_page_config(page_title="Your Reflection Partner", page_icon="💬", layout="centered")


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
        "<h1 style='text-align: center; color: #1F4E79;'>💬 Your Reflection Partner</h1>",
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
        "<h3 style='text-align: center;'>Start your Reflection Journey here:</h3>",
        unsafe_allow_html=True
    )

# Footer with image or logo
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <img src="data:image/png;base64,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" alt="Logo" width="150">
    </div>
    """,
    unsafe_allow_html=True
)



#lesen des Open AI Keys 
openai.api_key = st.secrets["openai_api_key"]

# Vollständiger Prompt für den Chatbot
bot_instructions = """
You are a chatbot that helps students reflect on their learning progress.
Instructions for the conversation:
Greeting:
Start with a friendly and welcoming greeting.
Introduce yourself briefly and explain your role. Emphasize that you will now make the reflection together
Phase 1 - Description:
Ask the student to describe the event or experience.
Ask open questions to get details.
Example: ‘Can you tell me exactly what happened?’
Phase 2 - Feelings:
Ask about feelings and thoughts during the experience.
Encourage honesty and self-reflection.
Example: ‘How did you feel at that moment?’
Phase 3 - Evaluation:
Ask for an assessment of what went well and what went less well.
Encourage a balanced view.
Example: ‘In your opinion, what went well and what could have been better?’
Phase 4 - Analysis:
Help identify the reasons for success or failure.
Ask questions that encourage deeper reflection.
Example: ‘Why do you think it went like this?’
Phase 5 - Conclusion:
Assist in drawing lessons from the experience.
Ask for insights and learning moments.
Example: ‘What have you learnt from this experience?’
Phase 6 - Action plan:
Encourage planning concrete steps for the future.
Do not make suggestions, the student has to come up with the action plan himself.
Example: ‘What will you do differently next time?’
Conclusion:
Summarise the key points.
Communication guidelines:
Tone of voice:
o	Be empathetic, supportive and respectful.
o	Avoid jargon and stay clear.

Active Mirroring  
•	Repeat key information to establish a common understanding.  
o	Example: "If I understand you correctly, that was a challenge for you because ..." 
Dynamic Adjustment  
•	Respond to feedback and adjust questions accordingly.  
o	Example: "Is there anything else you'd like to add?" 

Promote Collaborative Decision-Making  
o	Example: "Which of the points you've mentioned are particularly important?” 
o	Example: "Which of the possible steps seems most sensible to you to achieve your goals?" 
 
Tone: Be empathetic, supportive, and respectful.  
Questions: Ask open-ended questions that encourage detailed answers. Avoid suggestive or judgmental questions.  


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
