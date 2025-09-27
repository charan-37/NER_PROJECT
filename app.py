# Import libraries
import spacy
import streamlit as st
import pandas as pd

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Streamlit app title
st.title("Named Entity Recognition (NER) Mini Project")
st.write("This app extracts named entities from your text.")

# Text input
user_input = st.text_area("Enter your text here:")

# Button to trigger NER
if st.button("Extract Entities"):
    if user_input:
        doc = nlp(user_input)

        # Extract entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        if entities:
            # Display entities as a table
            df = pd.DataFrame(entities, columns=["Entity", "Label"])
            st.table(df)
            
            # Optional: Highlight entities in text
            highlighted_text = user_input
            for ent_text, ent_label in entities:
                highlighted_text = highlighted_text.replace(ent_text, f"{ent_text} ({ent_label})")
            st.markdown("### Text with Entities Highlighted")
            st.markdown(highlighted_text)
        else:
            st.write("No entities found in the text.")
    else:
        st.write("Please enter some text to analyze.")