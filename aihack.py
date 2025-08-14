from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

url = input("Enter the news article URL: ") #input URL for the news article

#url = "https://medium.com/data-science-collective/youre-using-chatgpt-wrong-here-s-how-to-prompt-like-a-pro-1814b4243064"
loader = WebBaseLoader(url)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,  
    
) # model currently using

model2 = ChatGoogleGenerativeAI(
    model = "models/gemini-2.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=1,
) #can change to this model also

docs = loader.load()  #loading of document

question = docs[0].page_content


prompt = PromptTemplate(
    
    template= "You are an investigative assistant. Given the text {text} of an online news article, produce a Critical Analysis Report in the following format: " \
    "Provide the core claims if any present in article with heading of core claims, " \
    "Also identify the tone of the article for example 'The language in this article is highly persuasive and uses emotionally charged words like 'disastrous' and 'unprecedented' to frame the narrative.'"\
    "Potential red flags with heading of potential red flags if any, for example:The article heavily relies on a single anonymous 'insider' for its most  significant claims ,Statistical data is mentioned but no link to the source study is provided."\
    "Some verification questions with heading verification question, for example: Can I find other independent reports from reputable sources that corroborate the claims made by the 'insider'?"\
    " Make a heading named 'entity recogination'  identify the key people, organizations,and locations mentioned and suggest what a reader should investigate about them (e.g., Investigate the authors previous work, Look into the funding of The XYZ Institute)?from the given text write in a concise manner"
    
,
    input_variables=['text']
)    # prompt to get desired output
prompt2 = PromptTemplate(
    
    template=' Make a heading named "entity recogination" identify the key people, organizations,and locations mentioned and suggest what a reader should investigate about them (e.g., "Investigate the authors previous work, Look into the funding of "The XYZ Institute")?from the given text {text} write in a concise manner',
    input_variables=['text']
) #promt can we use seperately to find entities in the text because model 2 is more accurate in this task


parser = StrOutputParser() #output parser to parse the output in string format

chain = prompt  | model | parser
response = chain.invoke({ "text": docs[0].page_content})
print(response)


#chain2 is commented out but can be used to get entities from the textseperately
#chain2 = prompt2 | model2 | parser
#response2 = chain2.invoke({"text": docs[0].page_content})
#print(response2)