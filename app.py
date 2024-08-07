import streamlit as st
from datetime import datetime, timedelta
from src.newsletter_gen.crew import NewsletterGenCrew
from crewai.crews.crew_output import CrewOutput

class NewsletterGenUI:

    def load_html_template(self):
        with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
            html_template = file.read()
        return html_template

    def generate_newsletter(self, topic, personal_message, start_date):
        end_date = datetime.now()

        st.write(f"Generating newsletter starting from {start_date}.")
        st.write(f"End date: {end_date.strftime('%Y-%m-%d')}")
        
        inputs = {
            "topic": topic,
            "personal_message": personal_message,
            "html_template": self.load_html_template(),
            "start_date": start_date,
            "end_date": end_date.strftime("%Y-%m-%d"),
        }
        crew_output = NewsletterGenCrew().crew().kickoff(inputs=inputs)
        
        # Extract content from CrewOutput
        if isinstance(crew_output, CrewOutput):
            # Inspect the structure of crew_output
            st.write("CrewOutput structure:")
            st.write(crew_output)
            
            # Try to access the content (adjust this based on the actual structure)
            if hasattr(crew_output, 'content'):
                return crew_output.content
            elif hasattr(crew_output, 'output'):
                return crew_output.output
            else:
                # If we can't find the content, return the string representation
                return str(crew_output)
        
        return str(crew_output)  # Fallback to string representation if not CrewOutput

    def newsletter_generation(self):
        if st.session_state.generating:
            newsletter_content = self.generate_newsletter(
                st.session_state.topic, st.session_state.personal_message, st.session_state.start_date
            )
            st.session_state.newsletter = newsletter_content

        if st.session_state.newsletter and st.session_state.newsletter != "":
            with st.container():
                st.write("Newsletter generated successfully!")
                st.markdown(st.session_state.newsletter, unsafe_allow_html=True)
                
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
                To generate a newsletter, enter a topic, a personal message, and the start publish date for the news search. \n
                Your team of AI agents will generate a newsletter for you!
                """
            )

            st.text_input("Topic", key="topic", placeholder="World News")

            st.text_area(
                "Your personal message (to include at the top of the newsletter)",
                key="personal_message",
                placeholder="Dear News Reader,",
            )

            # Add a date input for the start publish date
            st.date_input("Start publish date for news search", key="start_date", value=datetime.now() - timedelta(days=7))

            if st.button("Generate Newsletter"):
                st.session_state.generating = True

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

        if "start_date" not in st.session_state:
            st.session_state.start_date = datetime.now() - timedelta(days=7)  # Default to 7 days ago

        self.sidebar()
        self.newsletter_generation()


if __name__ == "__main__":
    NewsletterGenUI().render()