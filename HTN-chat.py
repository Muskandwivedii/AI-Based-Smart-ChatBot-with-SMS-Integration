# MODULES
import pyttsx3
import datetime
import requests
import speech_recognition as sr
from requests import get
from twilio.rest import Client
import re

import gui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)
#print(voices[2].id)
#print(voices[3].id)
#print(voices[4].id)
#print(voices[5].id)
#print(voices[6].id)
#print(voices)
engine.setProperty('voice', voices[1].id)

account_sid = 'AC7198fa532f3973905641d493e86e4f34'
auth_token = '4a6ef7b0edcb5651b0fd2a12a5e4c1e7'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define the phone number to send the message to
to_phone_number = '+919301682453'


def speak(audio):
    gui.speak(audio)
    engine.say(audio)
    engine.runAndWait()
# WISH ME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hey buddy  , Good Morning!")

    elif hour>=12 and hour<18:
      speak("Hey Buddy Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Your Buddy Here, How may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

wishMe()


def run_alpha():
        inpu = takeCommand()
        print(inpu)
        url = "http://api.brainshop.ai/get?bid=157984&key=3S0hhLXZ5GS2KYs4&uid=[uid]&msg=[{}]".format(inpu)
        response = requests.get(url).json()['cnt']
        print(response)
        speak(response)
        
def send_message(message):
    client.messages.create(
        body=message,
        from_='+16698005161',  # Replace with your Twilio phone number
        to=to_phone_number
    )
        
        
def run_alpha():
    inpu = takeCommand();  # Convert input to lowercase for case-insensitive comparisons.
    print(inpu)
    
        # Check if the input contains "Hy" and send a message if it does


    # Create an array (list) of questions
    whatisDip = [
        "how long have you been feeling this way",
        "depression kya hai" ,
        "what does the term depression actually mean",
        "can you explain the concept of depression to me",
        "how would you define depression?",
        "could you provide a definition of depression?",
        "what exactly is meant by the term 'depression'?",
        "can you describe what depression is?",
        "what is your understanding of the term 'depression'?",
        "could you clarify what depression is all about?",
        "what's the definition of depression in your own words?",
        "how do you define depression?",
        "can you break down the concept of depression for me?",
        "what does depression entail?",
        "in simple terms, what is depression?",
        "how would you characterize depression?",
        "could you shed some light on what depression is?",
        "tell me, what is depression?",
        "what's your take on the definition of depression?",
        "define depression for me, please.",
        "explain the meaning of depression, if you can.",
        "what's the essence of depression"
    ]
    
    nowwaht = [
        "ab kya, main toh pehle se hi udaas hoon.",
        "aur ab? Main toh pehle se hi depression mein hoon.",
        "iska kya ab? Main toh already dipressed hoon.",
        "kya farak padta hai ab, main toh udas hi hoon.",
        "aur ab mujhe kya, main toh udas hi hoon.",
        "ab samajh nahi aata, main toh pehle se hi depress hoon.",
        "aur batao, main toh pehle hi depression mein hoon.",
        "kya karun ab, main toh already udas hoon.",
        "koi Fark Nahin Padta Main To Pahle Se Hi depressed hun",
        "aur ab kya karein, main toh udas hi hoon."
    ]
    
    
    # Create a list (array) of phrases
    kyakru = [
        "main ise kis se baat karun",
        "kya main ise kisise discuss kar sakta hoon",
        "yeh kise ke saath share karun",
        "kis vyakti se main yeh baat karun",
        "isse kis vyakti ke saath vyakhya karu",
        "main Kis Se discuss karun",
        "kis vyakti ke saath main yeh vichar vyakt karu",
        "kis vyakti ke saath main yeh jaankari sanjoya karu",
        "kis dost ko yeh jaankari deni chahiye",
        "kis vyakti ko yeh samjhaa doon"
        "i am not feeling well"
        "i'm not feeling great.",
        "i'm not doing so well.",
        "i'm feeling under the weather.",
        "i'm not in the best of health.",
        "i'm a bit off today.",
        "i'm feeling a bit unwell.",
        "i'm not at my best right now.",
        "i'm not feeling up to par.",
        "i'm feeling a little sick.",
        "i'm not in top form today.",
        "i'm feeling a touch queasy.",
        "i'm not feeling very good.",
        "i'm not feeling too hot.",
        "i'm not feeling my usual self.",
        "i'm a bit out of sorts.",
        "i'm feeling a tad off.",
        "i'm not in the best condition.",
        "i'm feeling somewhat poorly.",
        "i'm not feeling quite myself today.",
        "i'm experiencing some discomfort."
    ]
    
    depression_symptom_questions = [
    "what are the typical signs and symptoms of depression",
    "can you explain the common physical symptoms of depression",
    "what emotional symptoms are often associated with depression",
    "are there any behavioral changes that are characteristic of depression",
    "how can I recognize if I'm experiencing symptoms of depression",
    "what are the early warning signs of depression",
    "can you list the most prevalent indicators of depression",
    "what might I expect in terms of cognitive symptoms if I have depression",
    "are there any social or interpersonal symptoms associated with depression",
    "what is the difference between feeling sad and having clinical depression",
    "can you describe how depression can affect a person's daily life",
    "what are the physical manifestations of depression that I should be aware of",
    "how do the symptoms of depression vary from person to person",
    "what are some less common symptoms of depression that I should still watch out for",
    "do symptoms of depression tend to worsen over time if left untreated",
    "can you discuss the relationship between anxiety and depression symptoms",
    "what is the duration of depressive symptoms on average",
    "are there any specific triggers or factors that can exacerbate depression symptoms",
    "can depression cause physical health problems as well",
    "how can I differentiate between situational sadness and clinical depression based on symptoms"
]
    
    depression_thoughts = [
    "how can i manage my depressive thoughts",
    "what are some strategies to deal with depressive thoughts",
    "how do i handle my depressive thoughts",
    "what can i do to combat depressive thoughts",
    "what are effective ways to cope with depressive thoughts",
    "how can i address my depressive thoughts",
    "what methods can help me cope with depressive thoughts",
    "how do i deal with my depressive thoughts",
    "what techniques can i use to manage depressive thoughts",
    "how can i overcome my depressive thoughts",
    "what steps should i take to manage depressive thoughts",
    "how can i lessen the impact of depressive thoughts",
    "what are some ways to alleviate depressive thoughts",
    "how do i navigate through my depressive thoughts",
    "what can i do to handle my depressive thoughts better",
    "how can i find relief from depressive thoughts",
    "what strategies should i employ to cope with depressive thoughts",
    "how can i reduce the frequency of depressive thoughts",
    "what are some tips for dealing with depressive thoughts",
    "how do i cope with my recurring depressive thoughts",
    "what techniques can i use to cope with depressive thoughts",
    "how can i gain control over my depressive thoughts",
    "what are some methods for managing depressive thoughts",
    "how do i combat my persistent depressive thoughts",
    "what steps can i take to address depressive thoughts",
    "how can i improve my mental state with depressive thoughts",
    "what are effective ways to handle depressive thoughts",
    "how can i find solace from my depressive thoughts",
    "what strategies can i adopt to cope with depressive thoughts",
    "how can i deal with my ongoing depressive thoughts"
    ]

    managing_depression = [
    "what self-help methods can assist with depression management",
    "are there any DIY approaches to deal with depression",
    "how can I help myself in managing depression",
    "what are some self-guided ways to cope with depression",
    "are there any techniques for self-help in depression management",
    "what self-help strategies are effective for depression",
    "how can I self-manage my depression effectively",
    "what are some self-reliant methods for handling depression",
    "are there any do-it-yourself techniques for depression management",
    "how can I use self-help to deal with my depression",
    "what are self-guided approaches to managing depression",
    "are there any self-help remedies for coping with depression",
    "how can I independently manage my depression",
    "what self-help practices can aid in depression management",
    "are there any self-directed strategies for depression coping",
    "how can I help myself with dealing with depression",
    "what are some self-reliance methods for depression management",
    "are there any DIY approaches to managing depression",
    "how can I utilize self-help to cope with depression",
    "what are self-guided techniques for depression management",
    "are there any self-help solutions for handling depression",
    "how can I self-administer my depression management",
    "what are some self-guidance methods for depression coping",
    "are there any self-directed approaches to deal with depression",
    "how can I empower myself in managing depression",
    "what are self-help strategies for effective depression management",
    "are there any self-help measures for depression coping",
    "how can I engage in self-management of depression",
    "what are some self-help tactics for handling depression",
    "are there any self-guided steps for dealing with depression"
    ]
    
    questions = [
    "Do you have any book suggestions for coping with depression",
    "Could you recommend resources to help with depression",
    "Are there any good books for managing depression that you can suggest",
    "What are some helpful resources for dealing with depression",
    "Can you point me to books or materials that address depression",
    "Do you know of any resources that could assist with depression",
    "Could you share books or resources for handling depression",
    "Are there any recommended books for tackling depression",
    "What resources can you recommend for managing depression",
    "Do you have any suggestions for books on coping with depression",
    "Are there any useful resources for dealing with depression that you know of",
    "Could you provide guidance on books or materials for depression",
    "Can you suggest any good books or resources for depression",
    "Do you know of any recommended materials for managing depression",
    "What books or resources would you suggest for coping with depression",
    "Could you recommend any materials to assist with depression",
    "Are there any books or resources you'd suggest for dealing with depression",
    "Do you have any reading recommendations for managing depression",
    "What resources do you recommend for coping with depression",
    "Can you suggest any helpful books for handling depression",
    "Are there any valuable resources for dealing with depression that you can recommend",
    "Could you share some books or materials for managing depression",
    "Do you know of any well-regarded books on coping with depression",
    "Can you point me to resources that address depression effectively",
    "What are some trusted books or resources for dealing with depression",
    "Do you have any favorite books for managing depression",
    "Are there any top resources for coping with depression that you'd recommend",
    "Could you provide some suggestions for books or materials on depression",
    "Can you recommend any books or resources for effectively dealing with depression",
    "What books or resources have been helpful for others in managing depression"
]

    treatment_questions = [
        "What are the available treatments for depression",
        "Can you list the options for treating depression",
        "What treatments exist for managing depression",
        "Are there any methods to address depression",
        "How can one seek treatment for depression",
        "What are the ways to treat depression",
        "Could you provide information on depression treatment options",
        "What are the recommended treatments for depression",
        "Are there effective ways to manage depression",
        "What are the possible treatments for dealing with depression",
        "Can you outline the treatment choices for depression",
        "How can depression be treated",
        "What are some therapeutic options for depression",
        "What are the strategies for handling depression",
        "Are there any interventions for depression",
        "What methods can be used to treat depression",
        "Can you suggest ways to alleviate depression",
        "What are the available therapies for depression",
        "Are there any medical treatments for managing depression",
        "What are the options for seeking help with depression",
        "How can one access treatment for depression",
        "What are the potential therapies for dealing with depression",
        "Can you describe the treatments for depression",
        "What are the approaches to treat depression",
        "Are there any recommended methods for managing depression",
        "What are the treatment modalities for depression",
        "Can you explain the available treatment choices for depression",
        "How can I find help for depression",
        "What are the standard treatments for dealing with depression",
        "Are there any effective remedies for depression",
        "What are the available options for addressing depression"
    ]

    counselor_questions = [
        "How do I locate a therapist or counselor for depression",
        "What's the process for finding a therapist for depression",
        "How can I search for a counselor to help with depression",
        "Where can I find a therapist or counselor specializing in depression",
        "What steps should I take to find a therapist for my depression",
        "How do I go about finding a counselor for depression",
        "What's the best way to find a therapist for depression",
        "Where can I seek help in finding a therapist for my depression",
        "How can I connect with a counselor for help with depression",
        "What resources are available for finding a therapist or counselor for depression",
        "What are the options for locating a therapist to address depression",
        "How can I access therapy or counseling services for my depression",
        "Where can I get information on finding a therapist for depression",
        "What are the recommended methods for finding a therapist or counselor for depression",
        "How can I start the process of finding a therapist to treat my depression",
        "Where should I begin my search for a counselor for depression",
        "How can I find a qualified therapist to help with my depression",
        "What are the first steps to take when searching for a therapist for depression",
        "How do I initiate the search for a counselor to address my depression",
        "Where can I get assistance in finding a therapist or counselor for depression",
        "What are the best practices for finding a therapist for depression",
        "How can I access mental health services for my depression",
        "Where can I seek guidance on finding a therapist or counselor for depression",
        "How can I reach out to professionals who specialize in depression",
        "What resources are available to help me locate a therapist for my depression",
        "How do I start the process of finding a counselor to address my depression",
        "Where can I find information on therapist directories for depression",
        "How can I get in touch with therapists who specialize in treating depression",
        "What steps can I follow to find a therapist or counselor for depression",
        "Where can I find reputable sources for locating a therapist to help with my depression",
        "How can I access therapy services for my depression"
    ]

    relaxation_techniques = [
        "What relaxation methods can help alleviate anxiety and depression",
        "Are there any techniques to reduce anxiety and depression through relaxation",
        "How can I use relaxation to manage anxiety and depression",
        "What are some relaxation strategies for reducing anxiety and depression",
        "Can you suggest ways to relax and alleviate anxiety and depression",
        "What methods can be employed to relax and combat anxiety and depression",
        "Are there effective relaxation techniques for anxiety and depression",
        "How can I incorporate relaxation into my routine to reduce anxiety and depression",
        "What are some practices for relaxation that can help with anxiety and depression",
        "Can you recommend relaxation approaches to alleviate anxiety and depression",
        "What relaxation exercises are useful for managing anxiety and depression",
        "Are there any proven relaxation methods to reduce anxiety and depression",
        "How can I incorporate relaxation practices into my daily life to combat anxiety and depression",
        "What are some relaxation tips for coping with anxiety and depression",
        "Can you suggest techniques for relaxation that specifically target anxiety and depression",
        "What are the best ways to relax and reduce anxiety and depression",
        "Are there any relaxation exercises that can be beneficial for anxiety and depression",
        "How can I integrate relaxation strategies into my routine to alleviate anxiety and depression",
        "What are some relaxation practices to help manage anxiety and depression",
        "Can you provide guidance on relaxation techniques for reducing anxiety and depression",
        "What relaxation methods have been effective in treating anxiety and depression",
        "How can I use relaxation as a tool to reduce symptoms of anxiety and depression",
        "What are some relaxation techniques that have shown promise in addressing anxiety and depression",
        "Can you recommend specific relaxation exercises for managing anxiety and depression",
        "What are the most recommended relaxation strategies for anxiety and depression",
        "How can I incorporate relaxation techniques into my daily life to reduce anxiety and depression",
        "What relaxation practices are known to be effective for anxiety and depression",
        "Are there any relaxation techniques that are particularly helpful for anxiety and depression",
        "How can I use relaxation as a means to cope with anxiety and depression",
        "What are some relaxation methods that have proven successful in alleviating anxiety and depression"
    ]

    mindfulness_questions = [
        "What is mindfulness and its role in depression management",
        "Can you explain how mindfulness is related to alleviating depression",
        "Tell me about mindfulness and its benefits for depression.",
        "How does mindfulness practice assist in dealing with depression",
        "What is the connection between mindfulness and managing depression",
        "Explain how mindfulness can be a tool for addressing depression.",
        "Tell me about mindfulness and its impact on depression treatment.",
        "How can mindfulness techniques aid in reducing depression",
        "What are the advantages of mindfulness for individuals dealing with depression",
        "Can you elaborate on how mindfulness practices help with depression",
        "Tell me more about mindfulness and its application in depression relief.",
        "What role does mindfulness play in coping with depression",
        "Describe mindfulness and its potential to alleviate depression symptoms.",
        "How does practicing mindfulness contribute to managing depression",
        "Can you provide insights into the relationship between mindfulness and depression",
        "Tell me about mindfulness and its relevance in the context of depression.",
        "How can mindfulness practices be beneficial for individuals with depression",
        "Explain the concept of mindfulness and its impact on depression.",
        "Tell me how mindfulness can assist those struggling with depression.",
        "What is mindfulness, and how does it relate to dealing with depression",
        "Can you detail how mindfulness practices aid in depression management",
        "Tell me about mindfulness and its significance in reducing depression.",
        "How does mindfulness fit into the toolkit for addressing depression",
        "Explain how mindfulness techniques can be helpful for individuals with depression.",
        "Tell me about mindfulness and its role as a coping mechanism for depression.",
        "What are the practical applications of mindfulness in the context of depression",
        "How can mindfulness be integrated into a holistic approach to depression treatment",
        "Tell me more about mindfulness and its therapeutic effects on depression.",
        "What is mindfulness, and how can it be a part of strategies to manage depression",
        "Explain how mindfulness practices can be utilized to alleviate depression symptoms.",
        "Tell me about mindfulness and its potential to positively impact those with depression."
    ]
    
    differences_questions = [
    "How does depression differ from other mental health issues",
    "Can you explain the distinctions between depression and other mental disorders",
    "What sets depression apart from other psychological conditions",
    "What are the contrasts between depression and other mental health disorders",
    "In what ways is depression distinct from other mental health conditions",
    "How can I differentiate depression from other mental health issues",
    "What are the unique characteristics of depression compared to other mental disorders",
    "What are the differences between depression and other mental health challenges",
    "Can you outline the disparities between depression and other psychological conditions",
    "How do the symptoms of depression differ from those of other mental health disorders",
    "What are the distinguishing factors between depression and other mental health conditions",
    "How can I recognize the distinctions between depression and other psychological issues",
    "What are the key disparities between depression and other mental health ailments",
    "Can you describe the differences between depression and other mental disorders",
    "How can I identify the specific features that differentiate depression from other mental health conditions",
    "What are the distinguishing symptoms that separate depression from other psychological disorders",
    "What are the contrasts in treatment approaches for depression compared to other mental health conditions",
    "How does the prevalence of depression compare to that of other mental health disorders",
    "What are the differences in the causes and risk factors between depression and other mental health conditions",
    "How do the outcomes and prognosis of depression differ from those of other mental health disorders",
    "What are the distinctions in the impact on daily life between depression and other mental health issues",
    "How can I discern between the emotional experiences of depression and those of other mental health conditions",
    "What are the differences in coping strategies for depression as opposed to other mental health disorders",
    "How do the diagnostic criteria for depression compare to those of other mental health conditions",
    "What are the variations in the age of onset between depression and other mental health disorders",
    "How can I differentiate between the cognitive patterns seen in depression versus those in other mental health conditions",
    "What are the differences in the prevalence of comorbidity between depression and other mental health issues",
    "How do the gender-specific aspects of depression compare to those of other mental health disorders",
    "What are the disparities in the societal stigma surrounding depression and other mental health conditions",
    "How can I distinguish between the genetic and environmental factors influencing depression versus those affecting other mental health conditions"
]
    
    struggling_questions = [
    "What can I do to help a loved one dealing with depression",
    "How do I offer support to someone I care about who has depression",
    "What are some ways to be there for a loved one with depression",
    "Can you provide guidance on supporting someone struggling with depression",
    "How can I assist a family member or friend coping with depression",
    "What should I say or do to support someone with depression",
    "How can I best help my loved one who is experiencing depression",
    "What actions can I take to be a supportive presence for someone with depression",
    "What strategies can I use to comfort and aid my loved one with depression",
    "Can you suggest ways to provide emotional support to someone battling depression",
    "How can I be a source of strength for my loved one with depression",
    "What should I avoid saying or doing when supporting someone with depression",
    "How can I create a safe and understanding environment for a loved one with depression",
    "What resources can I recommend to my loved one to help with their depression",
    "How can I encourage my friend or family member to seek professional help for their depression",
    "What are some signs that my loved one might be experiencing depression",
    "How can I educate myself about depression to better support my loved one",
    "What are the key considerations when offering support to someone with depression",
    "How can I be patient and understanding when my loved one is struggling with depression",
    "What are some self-care strategies for me as a caregiver to prevent burnout while supporting my loved one with depression",
    "How can I maintain open and empathetic communication with my loved one who has depression",
    "What are some practical ways to assist with daily tasks for someone with depression",
    "How can I encourage healthy habits and routines for my loved one dealing with depression",
    "What can I do to promote a sense of hope and motivation in my loved one with depression",
    "How can I be a source of emotional strength without enabling my loved one's depression",
    "What are some community resources or support groups that can benefit my loved one with depression",
    "How can I balance supporting my loved one with taking care of my own well-being",
    "What are the potential challenges in supporting a loved one with depression, and how can I address them",
    "How can I reassure my loved one that seeking help for their depression is a positive step",
    "What are some success stories or experiences of individuals who have supported loved ones through depression"
]

    mentalhealth_questions = [
        "What exercises or activities can I engage in to boost my mental health",
        "How can I improve my mental well-being through specific exercises or activities",
        "Can you recommend some mental health-enhancing exercises or activities",
        "What are some effective exercises or activities for enhancing mental health",
        "Are there any specific exercises or activities that can positively impact mental health",
        "What types of exercises or activities are known to promote mental well-being",
        "How can I incorporate exercises or activities into my routine to support my mental health",
        "What are some practical exercises or activities for nurturing mental health",
        "Can you provide guidance on exercises or activities that benefit mental health",
        "What exercises or activities have been shown to have a positive effect on mental health",
        "How can I use exercises or activities as tools for improving my mental health",
        "What are the benefits of incorporating certain exercises or activities into my daily life for mental health",
        "Can you suggest exercises or activities that can help manage stress and anxiety",
        "What exercises or activities can aid in reducing symptoms of depression and anxiety",
        "How do exercises or activities contribute to better emotional and psychological well-being",
        "Can you recommend exercises or activities that promote relaxation and mental clarity",
        "What exercises or activities can enhance resilience and coping skills for mental health challenges",
        "How can I make exercise or activity a sustainable part of my mental health routine",
        "What role does physical activity play in improving mental health",
        "Can you suggest specific exercises or activities for managing stress and building mental resilience",
        "What exercises or activities can be incorporated into daily life for overall mental well-being",
        "How can I establish a balance between exercise or activity and mental health maintenance",
        "What are some mindfulness exercises or activities that can positively impact mental health",
        "Can you recommend exercises or activities that promote a sense of purpose and fulfillment for mental health",
        "How can I find motivation to engage in exercises or activities that benefit my mental health",
        "What exercises or activities can help improve self-esteem and self-confidence for better mental health",
        "Can you provide examples of exercises or activities that enhance mindfulness and mental clarity",
        "How can I tailor exercises or activities to my individual mental health needs and goals",
        "What are some enjoyable and sustainable exercises or activities for long-term mental well-being",
        "Can you suggest exercises or activities that are suitable for beginners looking to improve their mental health"
    ]

    connection_questions = [
        "How does diet relate to depression",
        "Can you explain the link between depression and dietary choices",
        "What is the connection between the foods we eat and depression",
        "How does one's diet impact their risk of developing depression",
        "Can you discuss how dietary habits influence mental health, particularly depression",
        "What role does nutrition play in the development and management of depression",
        "How are diet and depression intertwined",
        "Can you elaborate on the relationship between diet and depressive symptoms",
        "What are the ways in which our food choices can affect our mood and depression",
        "How can dietary patterns contribute to the onset or prevention of depression",
        "Tell me about the impact of diet on depression and vice versa.",
        "What dietary factors should individuals be mindful of when dealing with depression",
        "How can certain foods and nutrients influence the severity of depressive episodes",
        "What are the key nutritional considerations in managing and treating depression",
        "Can you discuss the role of gut health in the connection between diet and depression",
        "How can one make dietary changes to support their mental health and alleviate depression",
        "Tell me about the research findings on the effects of diet on depression.",
        "What dietary strategies can individuals employ to reduce their risk of depression",
        "How do specific foods and nutrients affect neurotransmitters related to depression",
        "Can you provide examples of a depression-fighting diet",
        "How can a person's eating habits influence their overall emotional well-being, including depression",
        "What are the potential consequences of a poor diet on mental health and depression",
        "Tell me about the role of inflammation and dietary choices in depression.",
        "How can an individual's diet be tailored to help manage and recover from depression",
        "Can you explain how nutrient deficiencies may contribute to or exacerbate depression",
        "What dietary advice or interventions are recommended for individuals with depression",
        "How can diet modifications complement traditional treatments for depression",
        "Tell me about the impact of sugar and processed foods on depression.",
        "What are the dietary changes that individuals with depression should consider making",
        "How do lifestyle factors, including diet, interact with genetic predisposition to depression",
        "Can you provide insights into the influence of a Mediterranean diet on depression prevention and management"
    ]
    
    professional_questions = [
    "when should i seek professional help for my depression",
    "how do i determine if it's time to consult a professional for my depression",
    "at what point should i consider professional assistance for my depression",
    "when do i know it's necessary to seek help for my depression",
    "what are the signs that indicate i should seek professional help for depression",
    "when does my depression require professional intervention",
    "how can i tell if it's the right time to get professional help for my depression",
    "what are the indicators that i should reach out to a professional for my depression",
    "when is it appropriate to seek professional assistance for my depression",
    "how do i recognize when i should seek professional support for depression",
    "when does depression warrant professional treatment",
    "what are the cues that suggest i should seek professional help for my depression",
    "when is the right moment to consult a professional about my depression",
    "how can i tell if my depression necessitates professional help",
    "when should i start considering professional treatment for my depression",
    "what are the red flags that indicate i should seek professional help for depression",
    "when do i need to reach out to a professional for my depression",
    "how do i know if it's time to get professional assistance for my depression",
    "when should i think about professional support for my depression",
    "what are the triggers that suggest i should seek professional help for my depression",
    "when is the appropriate time to seek professional treatment for my depression",
    "how can i determine if my depression requires professional help",
    "when should i take the step to consult a professional about my depression",
    "what are the cues that tell me i should seek professional help for depression",
    "when do i realize it's time to get professional assistance for my depression",
    "how do i identify when it's time to seek professional support for my depression",
    "when should i start considering professional intervention for my depression",
    "what are the warning signs that indicate i should seek professional help for my depression",
    "when do i need to consider professional treatment for my depression",
    "how can i assess if it's time to reach out to a professional for my depression"
]
    
    strategies_questions = [
    "what are some strategies for managing depressive episodes",
    "how can I cope with depressive episodes",
    "what methods are effective for dealing with depressive episodes",
    "what are some ways to handle depressive episodes",
    "what can I do to manage depressive episodes",
    "how should I address depressive episodes",
    "what techniques help with depressive episodes",
    "how can I mitigate the impact of depressive episodes",
    "what steps can I take during depressive episodes",
    "what are some approaches for dealing with depressive episodes",
    "what are the best practices for managing depressive episodes",
    "what are some tips for handling depressive episodes",
    "what are effective strategies for coping with depressive episodes",
    "how do I navigate depressive episodes",
    "what actions should I consider during depressive episodes",
    "how can I best respond to depressive episodes",
    "what are some recommended ways to manage depressive episodes",
    "how can I better deal with depressive episodes",
    "what are some coping mechanisms for depressive episodes",
    "how should I manage and overcome depressive episodes",
    "what are some helpful methods for handling depressive episodes",
    "how can I improve my resilience during depressive episodes",
    "what are some practical solutions for managing depressive episodes",
    "how can I regain control during depressive episodes",
    "what strategies can I employ to overcome depressive episodes",
    "how can I find relief from depressive episodes",
    "what are some steps I can take to alleviate depressive episodes",
    "how can I maintain well-being during depressive episodes",
    "what are some ways to stay proactive when dealing with depressive episodes",
    "how can I develop a plan to manage depressive episodes",
]
    
    managing_questions = [
    "why is sleep important in managing depression",
    "what role does sleep play in dealing with depression",
    "how does sleep impact the management of depression",
    "what is the significance of sleep in depression management",
    "why should I focus on sleep when managing depression",
    "how does sleep affect depression and its management",
    "what are the connections between sleep and depression management",
    "why is quality sleep crucial for those with depression",
    "how does sleep quality influence depression management",
    "what are the benefits of prioritizing sleep in depression management",
    "why should I pay attention to my sleep patterns when dealing with depression",
    "how does sleep deprivation worsen depression symptoms",
    "what happens when sleep is neglected in depression management",
    "why is it necessary to address sleep issues in depression treatment",
    "how does sleep impact mood and emotions in depression",
    "what are the consequences of sleep disturbances in depression management",
    "why is a consistent sleep schedule important for those with depression",
    "how does sleep hygiene contribute to managing depression",
    "what are the effects of sleep on cognitive function in depression",
    "why is sleep therapy often recommended for individuals with depression",
    "how does sleep affect the overall well-being of someone with depression",
    "what is the relationship between sleep quality and depression remission",
    "why do sleep disturbances often accompany depression",
    "how does sleep affect the brain chemistry in depression",
    "what is the science behind the importance of sleep in managing depression",
    "why do changes in sleep patterns serve as indicators of depression",
    "how does sleep play a role in resilience against depression",
    "what are the psychological benefits of sufficient sleep in depression management",
    "why is sleep considered a natural antidepressant",
    "how does sleep influence the effectiveness of depression treatments",
    "what are the practical strategies for improving sleep in the context of depression",
]
    
    signs_questions = [
    "what are some signs that my depression is getting worse",
    "how can I recognize if my depression is worsening",
    "what are the indicators that my depression may be getting worse",
    "what are some red flags for a deteriorating depression",
    "how do I know if my depression is progressing",
    "what signs should I watch for if my depression is worsening",
    "what are the signals of worsening depression",
    "how can I tell if my depression is getting more severe",
    "what are some cues that my depression is deteriorating",
    "what are some symptoms of a worsening depression",
    "how do I identify if my depression is getting worse",
    "what should I be aware of if my depression is worsening",
    "what are some indications that my depression is deteriorating",
    "how can I detect if my depression is getting worse",
    "what are some warning signs of a deepening depression",
    "what are the markers of a worsening depression",
    "how do I notice if my depression is progressing",
    "what are some clues that my depression is getting more severe",
    "what are some flags for a deteriorating depression",
    "how can I sense if my depression is worsening",
    "what are some signals of a worsening depression",
    "how can I gauge if my depression is getting worse",
    "what are some hints that my depression is deteriorating",
    "what are some signs indicating that my depression is worsening",
    "how can I spot if my depression is getting worse",
    "what are some symptoms suggesting a worsening depression",
    "how do I determine if my depression is getting worse",
    "what should I look out for if my depression is worsening",
    "what are some signs hinting at a deteriorating depression",
    "how can I observe if my depression is getting worse",
]




    
    

    alert = ["commit" , "sucied" , "help" ]
    
    # what is dipression
    if any(whatisDip in inpu for whatisDip in whatisDip):
        speak("Depression is a mood disorder that causes a persistent feeling of sadness and loss of interest. Also called major depressive disorder or clinical depression, it affects how you feel, think and behave and can lead to a variety of emotional and physical problems.")
            
    if any(alert in inpu for alert in alert):
        send_message("Hi Muskan! Richa Wants to commets sucide.. call Police: 100 ")

    # mujha dipression ha me kya kruj ab     
    elif any(nowwaht in inpu for nowwaht in nowwaht):
        speak("Talk to Someone: Reach out to a trusted friend, family member, or counselor. Sharing your feelings with someone you trust can provide relief.")    
    
    elif any(kyakru in inpu for kyakru in kyakru):
        speak("To share your thoughts, you can talk to someone you trust or someone you want to communicate your thoughts with. like you know himanshu ")
           
    elif any(depression_symptom_questions in inpu for depression_symptom_questions in depression_symptom_questions):
            speak("Depression symptoms include persistent sadness, changes in sleep and appetite, fatigue, and negative thinking. Consult a healthcare professional for diagnosis and treatment if experiencing these signs.")
        
    elif any(depression_thoughts in inpu for depression_thoughts in depression_thoughts):
        speak("To cope with depressive thoughts, consider seeking support from a mental health professional and confiding in trusted friends or family members. Additionally, practicing mindfulness techniques and engaging in regular physical activity can help improve your mood and manage depressive symptoms.")
    
    elif any(managing_depression in inpu for managing_depression in managing_depression):
        speak("These may include practicing mindfulness, regular exercise, maintaining a healthy diet, seeking social support, setting achievable goals, and utilizing relaxation techniques, but it's essential to consult with a mental health professional to tailor a self-help plan that suits your specific needs.")
           
    elif any(questions in inpu for questions in questions):
        speak("There are several excellent resources for dealing with depression,books like David D. Burns and Stephen S. Ilardi. Additionally, websites like the National Institute of Mental Health (NIMH) and organizations like the Depression and Bipolar Support Alliance (DBSA) offer valuable information and support for individuals managing depression.")
       
    elif any(treatment_questions in inpu for treatment_questions in treatment_questions):
        speak("Treatment options for depression can include therapy (such as cognitive-behavioral therapy or interpersonal therapy), medication (like antidepressants), lifestyle changes (including exercise and a balanced diet), and support groups. The most effective treatment plan often depends on the individual's specific needs and should be determined in consultation with a mental health professional.")
          
    elif any(counselor_questions in inpu for counselor_questions in counselor_questions):
        speak("To find a therapist or counselor for depression, you can start by contacting your primary care physician for recommendations or searching online therapist directories. You can also reach out to your insurance provider to inquire about in-network mental health professionals, or consider seeking referrals from friends, family, or support groups in your community.")
           
    elif any(relaxation_techniques in inpu for relaxation_techniques in relaxation_techniques):
        speak("Relaxation techniques for reducing anxiety and depression can include deep breathing exercises, progressive muscle relaxation, mindfulness meditation, yoga, and guided imagery. These practices can help calm the mind, reduce stress, and improve overall emotional well-being when incorporated into your daily routine.")
          
    elif any(mindfulness_questions in inpu for mindfulness_questions in mindfulness_questions):
        speak("Mindfulness is a practice that involves paying deliberate attention to the present moment without judgment. It can help with depression by promoting self-awareness, reducing rumination, and enhancing emotional regulation, ultimately leading to a greater sense of control over depressive symptoms and improved overall well-being.")
          
    elif any(differences_questions in inpu for differences_questions in differences_questions):
        speak("Depression is characterized by persistent feelings of sadness, hopelessness, and a loss of interest in daily activities, while other mental health conditions, such as anxiety disorders, bipolar disorder, and schizophrenia, have distinct symptom profiles and diagnostic criteria. The differences between these conditions lie in their specific symptoms, duration, and underlying causes, which require careful assessment by mental health professionals for accurate diagnosis and treatment planning.")
           
    elif any(struggling_questions in inpu for struggling_questions in struggling_questions):
        speak("To support a loved one struggling with depression, it's essential to offer empathy, active listening, and reassurance without judgment. Encourage them to seek professional help, accompany them to appointments if needed, and be patient as they navigate their journey toward recovery.")
         
    elif any(mentalhealth_questions in inpu for mentalhealth_questions in mentalhealth_questions):
        speak("Engaging in regular physical exercise, such as walking, jogging, or yoga, can help improve mental health by reducing stress, boosting mood, and increasing the release of feel-good neurotransmitters. Additionally, mindfulness activities like meditation and deep breathing exercises can enhance emotional well-being, reduce anxiety, and promote mental clarity when practiced consistently.")
           
    elif any(connection_questions in inpu for connection_questions in connection_questions):
        speak("Research suggests that diet plays a significant role in depression, with evidence indicating that a balanced diet rich in whole foods, such as fruits, vegetables, lean proteins, and omega-3 fatty acids, may reduce the risk of depression and improve mood. Conversely, diets high in processed foods, sugar, and unhealthy fats have been associated with a higher likelihood of depression and worsened symptoms, highlighting the importance of mindful dietary choices for mental well-being.")
           
    elif any(professional_questions in inpu for professional_questions in professional_questions):
        speak("Knowing when to seek professional help for depression depends on the severity and duration of your symptoms. If your depression significantly impairs your daily functioning, persists for several weeks, or leads to thoughts of self-harm or suicide, it's crucial to reach out to a mental health professional for evaluation and support.")

    elif any(strategies_questions in inpu for strategies_questions in strategies_questions):
        speak("Managing depressive episodes often involves a combination of strategies, including seeking professional help from a therapist or psychiatrist and engaging in self-care practices such as regular exercise, maintaining a healthy diet, and practicing mindfulness or meditation. Additionally, building a strong support network of friends and family can provide emotional assistance during these episodes.")

    elif any(managing_questions in inpu for managing_questions in managing_questions):
        speak("Sleep is of paramount importance in managing depression as it plays a vital role in regulating mood, emotional stability, and cognitive function. Insufficient or poor-quality sleep can exacerbate depressive symptoms, making it essential for individuals with depression to prioritize healthy sleep habits as part of their overall treatment plan.")

    elif any(signs_questions in inpu for signs_questions in signs_questions):
        speak("Warning signs that your depression may be worsening can include increased feelings of hopelessness, persistent thoughts of self-harm or suicide, significant changes in appetite or sleep patterns, withdrawal from social activities, and a marked decline in energy and motivation. It's crucial to reach out to a mental health professional if you notice these signs or if your symptoms intensify, as they can help you adjust your treatment plan and provide necessary support.")









    elif 'time' in inpu:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")

    elif 'weather' in inpu:
        # Add code to fetch weather information and respond.
        pass
    
    else:
        speak("Your voice is not clear !! speak again")




gui.set_speak_command(run_alpha)
gui.mainloop()
