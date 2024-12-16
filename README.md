# NLP_ChatBot

Purpose of this project is to gain an understanding of NLP and build a foundation for AI. I built this 
project to incoporate it with my resume website that I am currently building. I plan to take what I learned from this project and 
add it onto my website. This chatbot will be able to answer questions based on my resume and the details I added for 
the bot to learn more about me. 

I am using Ollama for this project and langchain. Once I gain more of an understanding of Ollama and Embeddings, I
will add on to a streamlit and hopefully publish it. I will give it a simple framework such as Streamlit. I also created two bots.
One that is able to scrape data from a website and another bot that is able to scrape data from a pdf file. 

The website bot is able to take a link from the website and scrape the p tags. I will need to improve this bot because it 
does miss out on details such as certain products. It is also unable to bypass certain websites due to security and not having
headers. There will be more updates as I continue this project. The package I used was BeautifulSoup to scrape the html file. 

The second bot I worked was the one designed for my website. This bot scrapes the pdfs in the file such as the interest.pdf and 
resume.pdf. I attend to use this bot as an extension of my website. In order to scrape a PDF you must use a package called
PyPDFDirectoryLoader. This will allow you to scrape pdfs and load it into your llm. 
