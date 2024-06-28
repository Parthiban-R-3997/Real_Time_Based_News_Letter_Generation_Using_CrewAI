import os
import sys
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import streamlit as st
from datetime import datetime, timedelta
from src.newsletter_gen.crew import NewsletterGenCrew



class NewsletterGenUI:

    def load_html_template(self):
        with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
            html_template = file.read()
        return html_template

    def generate_newsletter(self, topic, personal_message, start_datetime, end_datetime):
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
            start_datetime, end_datetime = self.calculate_start_end_datetime()
            st.session_state.newsletter = self.generate_newsletter(
                st.session_state.topic,
                st.session_state.personal_message,
                start_datetime,
                end_datetime
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
                To generate a newsletter, enter a topic, a personal message, and select the time duration. \n
                Your team of AI agents will generate a newsletter for you!
                """
            )
            
            anthropic_api_key = st.text_input("Enter your Anthropic API Key", type="password", help="Get your API key from [Anthropic Website](https://console.anthropic.com/settings/keys)")
            os.environ["ANTHROPIC_API_KEY"] = str(anthropic_api_key)
            st.text_input("Topic", key="topic", placeholder="USA Stock Market")
            st.text_area(
                "Your personal message (to include at the top of the newsletter)",
                key="personal_message",
                placeholder="Dear readers, welcome to the newsletter!",
            )

            col1, col2, col3 = st.columns(3)
            with col1:
                st.session_state.days = st.number_input("Days", min_value=0, max_value=30, value=0, step=1)
            with col2:
                st.session_state.hours = st.number_input("Hours", min_value=0, max_value=23, value=0, step=1)
            with col3:
                st.session_state.minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0, step=1)

            if st.button("Generate Newsletter"):
                st.session_state.generating = True

    def calculate_start_end_datetime(self):
        total_minutes = (st.session_state.days * 24 * 60) + (st.session_state.hours * 60) + st.session_state.minutes
        if total_minutes == 0:
            # Default to 1 day if no time is specified
            start_datetime = datetime.now() - timedelta(days=1)
        else:
            start_datetime = datetime.now() - timedelta(minutes=total_minutes)
        end_datetime = datetime.now()
        return start_datetime, end_datetime

    def render(self):
        st.set_page_config(page_title="Newsletter Generation", page_icon="📧")

        if "topic" not in st.session_state:
            st.session_state.topic = ""
        if "personal_message" not in st.session_state:
            st.session_state.personal_message = ""
        if "newsletter" not in st.session_state:
            st.session_state.newsletter = ""
        if "generating" not in st.session_state:
            st.session_state.generating = False
        if "days" not in st.session_state:
            st.session_state.days = 0
        if "hours" not in st.session_state:
            st.session_state.hours = 0
        if "minutes" not in st.session_state:
            st.session_state.minutes = 0

        self.sidebar()
        self.newsletter_generation()

if __name__ == "__main__":
    NewsletterGenUI().render()
