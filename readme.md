Skeptical News Article Analysis Tool

Create your Gemini API key compatible with gemini-2.5-flash model to run the ai application or DM me for API key.



***Overview***

This project is a Python-based tool that takes the URL of an online news article, fetches its content, and uses Google’s Gemini models through LangChain to perform a skeptical analysis of the article.
The tool:

Identifies the core claims in the article.

Detects tone and persuasive language.

Highlights potential red flags.

Suggests verification questions for fact-checking.

Performs Named Entity Recognition (NER) to extract key people, organizations, and locations, along with investigation suggestions.

The approach allows users to evaluate the credibility of news content without making final judgments, empowering them to ask the right questions.

***Features***

Dynamic URL Input – Users enter the URL of the news article at runtime.

Web Scraping with WebBaseLoader – Automatically fetches the text content of the article.

Critical Analysis Prompting – Uses a custom PromptTemplate to guide the LLM in producing structured output.

Named Entity Recognition (NER) – Optionally runs a separate, more accurate model for extracting key entities.

Chain Execution – Allows running two LangChain pipelines sequentially for different analysis purposes.

***Technology Stack***

Python 3.x

LangChain – For chaining prompts, models, and parsers.

Google Generative AI API (Gemini) – For text analysis.

dotenv – To manage API keys securely.

langchain_community.document_loaders.WebBaseLoader – To fetch and parse online articles.

***Steps or Approach the solution***
Here’s your condensed point-wise version:

1.Load Environment Variables – Store Google API key in .env and load with load_dotenv().

2.User Input for URL – Use input() to accept a news article URL dynamically.

3.Load Article Content – Use WebBaseLoader(url).load() to fetch and store article text.

4.Initialize Models –

gemini-2.5-flash for fast, cost-efficient analysis.

gemini-2.5-pro for detailed, accurate entity recognition.

5.Define Prompts –

Prompt 1: Critical analysis (claims, tone, red flags, verification questions, entities).

Prompt 2: Entity recognition only.

6.Create LangChain Pipelines – Build chains using prompt | model | parser and invoke with article text.

7.Sequential Execution – Optionally run both chains if high entity accuracy is required.


***How to run***
Install dependencies:

pip install langchain langchain_community langchain_google_genai python-dotenv


Create a .env file with your Google API key.

Run the script:

python main.py


Enter a news article URL when prompted.

***Output example***
Core Claims:
- XYZ happened due to ABC.

Tone Analysis:
The article uses emotionally charged words like "catastrophic"...

Potential Red Flags:
- Relies on a single anonymous source.

Verification Questions:
- Can I find other reports from reputable outlets?

Entity Recognition:
- John Doe (Investigate past work)
- The XYZ Institute (Look into funding sources)
