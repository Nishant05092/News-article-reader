Skeptical News Article Analysis Tool
<p align="center"><strong>AI-powered analyzer</strong> that evaluates online news articles for credibility, tone, and red flags using Google’s Gemini models through LangChain.</p> <p align="center"> <a href="https://www.python.org/downloads/release/python-3110/"> <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-blue.svg"> </a> <a href="https://ai.google.dev/gemini-api/docs"> <img alt="Gemini API" src="https://img.shields.io/badge/Gemini%20API-2.5--flash-orange.svg"> </a> <a href="https://github.com/langchain-ai/langchain"> <img alt="LangChain" src="https://img.shields.io/badge/LangChain-Framework-green.svg"> </a> </p>
Contents

Overview

Architecture

Installation and Setup

Prerequisites

Quick Setup

Configuration

How it Works

Directory Layout

Example Output

Contributing

License

Overview

The Skeptical News Article Analysis Tool helps users critically evaluate online news articles without bias.
It fetches article text directly from the web and uses Google’s Gemini models via LangChain to:

Identify core claims and main themes.

Detect tone, bias, and persuasive language.

Highlight potential red flags and logical fallacies.

Suggest fact-checking questions for deeper verification.

Perform Named Entity Recognition (NER) to extract people, organizations, and places for further investigation.

The goal is to empower users to think critically, not to judge content as true or false.

Architecture
<table> <tr> <td>

Flow

Load the Google Gemini API key from .env.

Accept a news article URL as input.

WebBaseLoader scrapes and parses the article text.

PromptTemplate guides the Gemini model for structured analysis.

The LangChain pipeline runs analysis and NER sequentially.

Results are displayed with claims, tone, red flags, and entity insights.

</td> <td>

Key Modules

main.py
Entry point; orchestrates the full analysis pipeline.

prompts.py
Contains templates for critical analysis and entity recognition.

loaders.py
Handles web scraping using LangChain’s WebBaseLoader.

.env
Stores the Google API key securely.

</td> </tr> </table>
Installation and Setup
Prerequisites

Python 3.11+

A valid Gemini API key (create via Google AI Studio
)

Quick Setup
# Clone the repository
git clone https://github.com/<your-username>/skeptical-news-analyzer.git
cd skeptical-news-analyzer

# Install dependencies
pip install -r requirements.txt


Then create a .env file with your API key:

GOOGLE_API_KEY=your_api_key_here

Configuration

You can switch between Gemini models by editing main.py:

model_name = "gemini-2.5-flash"   # Fast and cost-efficient
# model_name = "gemini-2.5-pro"   # More detailed and accurate

How it Works

Load Environment Variables
The script reads your API key using dotenv.

Fetch Article
WebBaseLoader scrapes and parses text from the provided URL.

Initialize Models

gemini-2.5-flash: fast and lightweight

gemini-2.5-pro: deeper NER analysis

Define Prompts

Prompt 1: Analyze tone, claims, red flags, and verification questions.

Prompt 2: Extract named entities for deeper investigation.

Execute Chains
LangChain sequentially runs both models and outputs structured insights.

Directory Layout
skeptical-news-analyzer/
├── main.py
├── prompts.py
├── loaders.py
├── .env
├── requirements.txt
└── README.md

Example Output

Core Claims:

The article claims that XYZ happened due to ABC.

Tone Analysis:

Uses emotionally charged language such as “catastrophic” and “shocking”.

Potential Red Flags:

Relies heavily on unnamed sources.

Verification Questions:

Can this be confirmed by another credible outlet?

Entities:

John Doe — Investigate past statements.

XYZ Institute — Check funding transparency.

Contributing

Contributions are welcome!
Fork the repo, create a branch, make your changes, and submit a pull request.
Feel free to DM for collaboration or to request an API key for testing.

License

This project is licensed under the MIT License.
