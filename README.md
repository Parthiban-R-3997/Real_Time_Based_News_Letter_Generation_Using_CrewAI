## AI-Powered Real-Time Newsletter Generation

Welcome to the NewsletterGen Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. The goal is to enable agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

This project is a Streamlit application that leverages AI agents to generate customized newsletters based on real-time news data. It uses the CrewAI framework to coordinate a team of AI agents that research, edit, and design newsletters on specified topics.

## Deployed Link

Newsletter Generation App is Deployed And Available [Here](https://realtimebasednewslettergeneration.streamlit.app/)


## Screenshots

![crew_1](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/187984bf-a3fc-49cd-9b20-841629baaa12)
![crew_2](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/5419b9d9-2558-49e0-a4c4-e95eaab78b0f)
![crew_3](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/05aabb8b-2f64-4caa-a174-0a8dd7f1ab69)
![crew_4](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/b550c8fe-518a-48ef-9d3b-0cbd998df00a)
![crew_5](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/fd342956-f0cf-490c-8090-0727f877c77a)
![crew_6](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/edcde6df-03fe-4928-8ebb-2d7a806aa592)
![crew_7](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/ea7e67c4-d69c-4075-b2c9-49e1f2d7b69b)


## Key Features
- **Real-Time News Integration**: Utilizes the Exa API to fetch the latest news articles on specified topics based on semantic meaning and not by keyword search.
- **AI-Driven Content Creation**: Employs a team of AI agents to research, curate, and edit content for the newsletter.
- **Customizable Topics**: Users can input any topic of interest to generate a relevant newsletter.
- **Date Range Selection**: Allows users to specify a start date for news searches, ensuring up-to-date content.
- **Personalized Messaging**: Includes an option to add a custom personal message at the top of the newsletter.
- **HTML Newsletter Generation**: Produces a fully formatted HTML newsletter ready for distribution.
- **One-Click Download**: Enables users to download the generated newsletter as an HTML file.


## Project Uniqueness
This project stands out due to its innovative approach to newsletter creation:

- **AI Agent Collaboration**: Utilizes the CrewAI framework to orchestrate a team of AI agents, each with specialized roles in the newsletter creation process.
- **Real-Time Data Integration**: Incorporates the latest news by leveraging the Exa API, ensuring newsletters are always current and relevant.
- **Flexible Content Generation**: Adapts to any topic specified by the user, making it versatile for various industries and interests.
- **Streamlined User Experience**: Offers a simple, intuitive interface for users to generate complex, AI-crafted newsletters with minimal input.
- **Scalable Architecture**: Designed to handle multiple simultaneous requests and can be easily extended to include additional features or data sources.


## How It Works
User Input: Users specify a topic, personal message, and start date for news search.

- **Research Agent**: Searches for and analyzes recent news articles on the specified topic.
- **Editor Agent**: Curates and refines the content, ensuring relevance and coherence.
- **Designer Agent**: Formats the content into an attractive HTML newsletter template.
- **Output**: Users can preview and download the generated newsletter as an HTML file.


## Impact
This tool revolutionizes the newsletter creation process by:

Reducing the time and effort required to create high-quality, topical newsletters.
Ensuring content is always fresh and relevant, improving reader engagement.
Allowing for rapid creation of newsletters on any topic, enhancing responsiveness to current events.
Providing a scalable solution for businesses and individuals who need to produce regular, customized newsletters.
By automating the research, writing, and design processes, this application empowers users to create professional-grade newsletters without the need for a dedicated content team or extensive time investment.


Consider the following diagram to understand how multi agents are built:

![Agent Architecture](https://github.com/Parthiban-R-3997/Chat_With_Multiple_SQL_Databases/assets/26496805/21e0998b-4d39-4ac2-b47b-cc332bdbca2d)


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your  `ANTHROPIC_API_KEY` into the `.env` file**

- Modify `src/newsletter_gen/config/agents.yaml` to define your agents
- Modify `src/newsletter_gen/config/tasks.yaml` to define your tasks
- Modify `src/newsletter_gen/crew.py` to add your own logic, tools and specific args
- Modify `src/newsletter_gen/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run newsletter_gen
```

This command initializes the newsletter-gen Crew, assembling the agents and assigning them tasks as defined in your configuration.


## Understanding Your Crew

The newsletter-gen Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## Contributing

Contributions to this project are welcome! If you have any ideas, bug fixes, or improvements, feel free to submit a pull request. Please ensure that your code adheres to the project's coding standards and is well-documented.

## License

This project is licensed under the [MIT License](LICENSE).
