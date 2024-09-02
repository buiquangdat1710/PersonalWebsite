import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("🏠_Mainpage.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/1_📚_Experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/2_🎨_Portofolio.py", label="Portofolio", icon="🎨")
    bar4.page_link("pages/3_🌏_Contacts.py", label="Contacts", icon="🌏")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
Coming from someone who wanted to be a mathematician, I realized that my real passion was AI. The field I want to pursue is NLP, but pursuing AI engineering or AI research is still an open question for me. Currently, I want to become an AI researcher but who knows in a few years I can become Fullstack.. **Winter is coming but Q1 may not come with winter**..
              """,
        'name':'Bui Quang Dat', 
        'study':'Posts and Telecommunications Institute of Technology',
        'location':'Hanoi, VN',
        'interest':'NLP, RL, AI Research, AI Engineer',
        'skills':['Python','Java','C/C++','HTML & CSS','Streamlit','Docker','Github','OpenAI API','REST api'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [
              [":green[Member of Training Committee] | ProPTIT Club", "Member", 
              "Jan 2024 – present", "Hanoi, VN", 
              """
              - Teach students about C/C++, Data Structures and Algorithms.
              """, 
              "Club website", "https://proptit.com/"],

              [":blue[Member of AI and Information Security Laboratory]| PTIT", "Ai Researcher", 
              "May 2024 – present", "Hanoi, VN", 
              """
              - Research and experiment with LLMs models to detect vulnerabilities in source code. 
              - Currently I am writing an article with **Assoc. PhD. Do Xuan Cho** and **Assoc. PhD. Nguyen Kim Khoa** on the issue of detecting vulnerabilities in real projects. The results of the article will be updated as soon as possible.
              """,
              "PTIT website", "https://portal.ptit.edu.vn/"],
              ]      

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 
              1:[':green[Seminar From Math to AI] website',  
                """
                - Seminar From Math to AI by two **PhD teachers. Hoang Phi Dung** and **Assoc. PhD. Do Xuan Cho** from Posts and Telecommunications Institute of Technology (PTIT) founded and led. This seminar is especially for PTIT students and is completely free, allowing students to access knowledge without having to worry about costs.
                - The seminar focuses deeply on theory and mathematics, helping students better understand the important theoretical foundations behind algorithms and applications in artificial intelligence. This is a great opportunity for students to explore the connection between mathematics and AI, without having to focus too much on programming or coding. In addition, participating students will receive a certificate after completing the program, recognizing their efforts and achievements during their participation. This is a high-quality learning environment where students can improve the knowledge and skills necessary for fields related to artificial intelligence.
                """],
              2:[':blue[Smart Assistant] website',  
                """
                - Smart Assistant is a website that helps users answer questions using LLMs models. 
                - I use OpenAI company API for this web. Although this is not recommended, I do not have enough time or powerful computer to build the model myself from scratch. Hope to be able to do this in the future.
                - Contact me if you want to have key code. 
                """],
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "0377875465"
email = "buiquangdat1458@gmail.com"
linkedin_link = "https://www.linkedin.com/in/buiquangdat/"
github_link = "https://github.com/buiquangdat1710?tab=repositories"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
