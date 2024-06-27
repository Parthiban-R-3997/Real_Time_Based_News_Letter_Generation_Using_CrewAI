import streamlit as st
from datetime import datetime, timedelta
from newsletter_gen.crew import NewsletterGenCrew

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
                To generate a newsletter, enter a topic, a personal message, and select a relative time duration. \n
                Your team of AI agents will generate a newsletter for you!
                """
            )

            st.text_input("Topic", key="topic", placeholder="USA Stock Market")
            st.text_area(
                "Your personal message (to include at the top of the newsletter)",
                key="personal_message",
                placeholder="Dear readers, welcome to the newsletter!",
            )

            relative_time = st.text_input("Relative time duration (e.g., '1 day', '5 hours', '30 minutes')", key="relative_time")
            st.write(f"You entered: {relative_time}")

            if st.button("Generate Newsletter"):
                st.session_state.generating = True

    def calculate_start_end_datetime(self):
        relative_time_input = st.session_state.relative_time.strip().lower()
        if 'day' in relative_time_input:
            days = int(relative_time_input.split()[0])
            start_datetime = datetime.now() - timedelta(days=days)
            end_datetime = datetime.now()
        elif 'hour' in relative_time_input:
            hours = int(relative_time_input.split()[0])
            start_datetime = datetime.now() - timedelta(hours=hours)
            end_datetime = datetime.now()
        elif 'minute' in relative_time_input:
            minutes = int(relative_time_input.split()[0])
            start_datetime = datetime.now() - timedelta(minutes=minutes)
            end_datetime = datetime.now()
        else:
            # Default to 1 day if no valid input is provided
            start_datetime = datetime.now() - timedelta(days=1)
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

        if "relative_time" not in st.session_state:
            st.session_state.relative_time = ""

        self.sidebar()

        self.newsletter_generation()


if __name__ == "__main__":
    NewsletterGenUI().render()
