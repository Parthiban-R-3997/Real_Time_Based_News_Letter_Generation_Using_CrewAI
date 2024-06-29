import os
import streamlit as st
from datetime import datetime, timedelta
from src.newsletter_gen.crew import NewsletterGenCrew

class NewsletterGenUI:

    def load_html_template(self):
        with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
            html_template = file.read()
        return html_template

    def generate_newsletter(self, topic, personal_message, days):
        start_datetime = datetime.now() - timedelta(days=days)
        end_datetime = datetime.now()
        
        inputs = {
            "topic": topic,
            "personal_message": personal_message,
            "html_template": self.load_html_template(),
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
        }
        return NewsletterGenCrew().crew().kickoff(inputs=inputs)

    def newsletter_generation(self):
        if st.session_state.generating:
            st.session_state.newsletter = self.generate_newsletter(
                st.session_state.topic,
                st.session_state.personal_message,
                st.session_state.days
            )

        if st.session_state.newsletter and st.session_state.newsletter != "":
            with st.container():
                st.write("Newsletter generated successfully!")
                current_date = datetime.now().strftime("%Y-%m-%d")
                file_name = f"{st.session_state.topic}_newsletter_{current_date}.html"
                st.download_button(
                    label="Download HTML file",
                    data=st.session_state.newsletter,
                    file_name=file_name,
                    mime="text/html",
                )
            st.session_state.generating = False

    def sidebar(self):
        with st.sidebar:
            st.title("Newsletter Generator")
            st.write(
                """
                To generate a newsletter, enter a topic, a personal message, and the number of days. \n
                Your team of AI agents will generate a newsletter for you!
                """
            )

            st.text_input("Topic", key="topic", placeholder="USA Stock Market")
            st.text_area(
                "Your personal message (to include at the top of the newsletter)",
                key="personal_message",
                placeholder="Dear readers, welcome to the newsletter!",
            )
            st.text_input(
                "Number of days to look back from today (e.g., 7 for one week)",
                key="days",
                placeholder="7",
                help="Enter the number of days to look back from today"
            )

            if st.button("Generate Newsletter"):
                st.session_state.generating = True

    def render(self):
        st.set_page_config(page_title="Newsletter Generation", page_icon="📧")

        if "topic" not in st.session_state:
            st.session_state.topic = ""

        if "personal_message" not in st.session_state:
            st.session_state.personal_message = ""

        if "days" not in st.session_state:
            st.session_state.days = 7  # Default to 7 days if not specified

        if "newsletter" not in st.session_state:
            st.session_state.newsletter = ""

        if "generating" not in st.session_state:
            st.session_state.generating = False

        self.sidebar()
        self.newsletter_generation()

if __name__ == "__main__":
    NewsletterGenUI().render()
