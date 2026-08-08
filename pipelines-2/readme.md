# Generating Summary and questions

1. This pipeline deals with generating a summary based on a given topic and then forming quiz type questions on that topic. Internally it consists of three chains.
2. The first pipeline consists of two prompts the first prompt takes the topic name as input and generates a large text on that topic and it passes to the second prompt which then summaries the large text into five or six points
3. The second pipeline also consists of two prompts the first prompt takes the topic name as input and generates a large text on that topic and it passes to the second prompt which then generates 10 quiz type questions based on that text.
4. The third pipeline takes input from pipeline 1 and pipeline 2 and merges them into one single output which is then displayed as the final output.


### **Here is an example of output**
<img width="1517" height="864" alt="image" src="https://github.com/user-attachments/assets/94d8602a-6fbf-428d-81d1-80b09b69aa6e" />
<img width="1522" height="847" alt="image" src="https://github.com/user-attachments/assets/912587b8-a970-4106-a1fe-3b6e9cb616ab" />


**Libraries Used:**

- ```langchain-core```
- ```dotenv```
- ```langchain-groq```
- ```uv```

**LLM Used** - Groq (model = ```llama-3.3-70b-versatile```)
  
