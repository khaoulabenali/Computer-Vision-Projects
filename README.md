# Computer-Vision-Projects

### What Is Computer Vision ?

- Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information. If AI enables computers to think, computer vision enables them to see, observe and understand. (IBM)
- Computer vision works much the same as human vision, except humans have a head start. Human sight has the advantage of lifetimes of context to train how to tell objects apart, how far away they are, whether they are moving and whether there is something wrong in an image.

<img src="/assets/cv.webp" width="500" align="center"/>


### How Does Computer Vision work?
- Computer vision needs lots of data. It runs analyses of data over and over until it discerns distinctions and ultimately recognize images. For example, to train a computer to recognize automobile tires, it needs to be fed vast quantities of tire images and tire-related items to learn the differences and recognize a tire, especially one with no defects.
- Two essential technologies are used to accomplish this: a type of machine learning called deep learning and a convolutional neural network (CNN).
- Machine learning uses algorithmic models that enable a computer to teach itself about the context of visual data. If enough data is fed through the model, the computer will “look” at the data and teach itself to tell one image from another. Algorithms enable the machine to learn by itself, rather than someone programming it to recognize an image.
- A CNN helps a machine learning or deep learning model “look” by breaking images down into pixels that are given tags or labels. It uses the labels to perform convolutions (a mathematical operation on two functions to produce a third function) and makes predictions about what it is “seeing.” The neural network runs convolutions and checks the accuracy of its predictions in a series of iterations until the predictions start to come true. It is then recognizing or seeing images in a way similar to humans.
- Much like a human making out an image at a distance, a CNN first discerns hard edges and simple shapes, then fills in information as it runs iterations of its predictions. A CNN is used to understand single images. A recurrent neural network (RNN) is used in a similar way for video applications to help computers understand how pictures in a series of frames are related to one another.

  
<img src="/assets/hdcvw.png" width="500" height="500" align="center"/>

### Natural Language Processing Algorithms :

- Once your data has been pre-processed, it’s time to move onto the next step: building an NLP algorithm, and training it so it can interpret natural language and perform specific tasks.

- There are two main algorithms you can use to solve NLP problems:

    * A rule-based approach. Rule-based systems rely on hand-crafted grammatical rules that need to be created by experts in linguistics, or knowledge engineers. This was the earliest approach to crafting NLP algorithms, and it’s still used today.

    * Machine learning algorithms. Machine learning models, on the other hand, are based on statistical methods and learn to perform tasks after being fed examples (training data). 

- The biggest advantage of machine learning algorithms is their ability to learn on their own. You don’t need to define manual rules – instead machines learn from previous data to make predictions on their own, allowing for more flexibility.

- Machine learning algorithms are fed training data and expected outputs (tags) to train machines to make associations between a particular input and its corresponding output. Machines then use statistical analysis methods to build their own “knowledge bank” and discern which features best represent the texts, before making predictions for unseen data (new texts):
<img src="/assets/Capture.PNG" width="500" height="500" align="center"/>

### Natural Language Processing Examples :

###### Text Classification :

- Text classification is one of the most basic NLP tasks and consists of assigning categories (tags) to a text, based on its content. Classification models can serve different purposes, for example:


* Sentiment analysis is the process of analyzing emotions within a text and classifying them as positive, negative, or neutral. By running sentiment analysis on social media posts, product reviews, NPS surveys, and customer feedback, businesses can gain valuable insights about how customers perceive their brand.

* Topic classification consists of identifying the main themes or topics within a text and assigning predefined tags. For training your topic classifier, you’ll need to be familiar with the data you’re analyzing, so you can define relevant categories. For example, you might work for a software company, and receive a lot of customer support tickets that mention technical issues, usability, and feature requests.In this case, you might define your tags as Bugs, Feature Requests, and UX/IX.


* Intent detection consists of identifying the purpose, goal, or intention behind a text. It’s an excellent way of sorting outbound sales email responses by Interested, Need Information, Unsubscribe, Bounce, etc. The tag Interested could help you spot a potential sale opportunity as soon as an email enters your inbox!

###### Text Extraction :

- Another example of NLP is text extraction, which consists of pulling out specific pieces of data that are already present in a text. It’s a perfect way to automatically summarize text or find key information. The most common examples of extraction models are:


* Keyword extraction automatically extracts the most important words and expressions within a text. This can provide you with a sort of preview of the content and its main topics, without needing to read each piece.

###### Machine Translation :

- This was one of the first problems addressed by NLP researchers. Online translation tools (like Google Translate) use different natural language processing techniques to achieve human-levels of accuracy in translating speech and text to different languages. Custom translators models can be trained for a specific domain to maximize the accuracy of the results.

###### Topic Modeling :

- Topic modeling is similar to topic classification. This example of natural language processing finds relevant topics in a text by grouping texts with similar words and expressions.

- Since you don’t need to create a list of predefined tags or tag any data, it’s a good option for exploratory analysis, when you are not yet familiar with your data.

###### Natural Language Generation (NLG) :

- Natural language generation, NLG for short, is a natural language processing task that consists of analyzing unstructured data and using it as an input to automatically create content. 

<img src="/assets/C13783_01_04.jpg" width="500" height="500" align="center"/>


### Top NLP Tools to Help You Get Started :
    
* MonkeyLearn
* Google Cloud NLP
* IBM Watson
* Aylien
* Amazon Comprehend
* MeaningCloud
