# PDF-chatbot 

#### Please write done in bracket if you incorporate these changes. We can track our progress from here. You can also assign someone's name as well. 

Comments from Ratan
1. @Ravi - Please keep all processing regarding classes in a common folder, lets say Processor (Feel free to name)
    - Ravi needs to complete class for QueryProcessor (Engine), Text Processing (Processor)
    - Ratan to add a basic flow and show storing query in DB
2. @Riddhi - Please create a file called server.py / app.py and create Flask Server APIs
    - Adding uploads folder in the project
    - Render the basic interface **(Done)**
3. @Fiza - Please create a User Interface for uploading files and Chat interface **(Done)** 
    - Deliver basic UI 
    - Collaborate with Shubham to give him an independent component
4. @Ravi - Create a QueryProcessor.py class and keep it in Engines folder. **(Sample Done)**
5. @Shubham - Create bash scripts for keeping server up / killin it / restarting it.
    - Shubham to deliver the bash scripts start.sh, kill.sh, restart.sh
6. @Ratan - Creation of DB Layer, Singleton and Factory classes **(Done)**
    - Refactor the code
    - creation of Db plans 

----------------------------------------------------------------------------------------------------------
Comments after Review - Apr 6th, 2020

1. @ Ravi - ChunksModule.py and other files should be moved to Processors Folder. Make sure your inherit Abstract class Processor.py. I have added a basic flow in QueryProcessor class. File upload is working fine now, so you can write a dummy code to fetch files from a folder called **uploads** and process as per your wish.
2. @ Riddhi - File Upload issue has been fixed. Server works fine now. Please follow the steps mentioned in ReadMe.md of Server branch to integrate your code to the master repo.

-Engines
-RestServer
    - Routes.py
-uploads
    -ABC.PDF
-app.py 
**(i have uploaded the app.py and the restServer package)**
URL - https://smartpdfassistant.herokuapp.com
3. @ Shubham - I dont see any commits from your end. May I know your contribution ?
Create Download BAT Script to download Glove and store it in ThirdPartyData Folder.


4. @ Fiza - Is it possible for your end to list down the API that you have hooked up with UI. Will be really appreciable if we could see the UI as I am completely out of sync.
    
    1. '/handleUpload': for uploading pdf
    
    2. '/questions':  to send question from ui to backend

5. @Ratan - Create a basic module for Embeddings. Add Glove as Example.
To All : 
Let's set Elastic Server on our systems post tomorrow's call and start working on a class to use the functionality.
Aim for this week to deploy this code on server. We will implement further the internal working once this is deployed.

Elastic Server function:

- connect to the elastic server(done)
- Create new index for the pdf (done)
- upload dictionary/dataframe
- search for the most probably shard 


-----------------------------------------------------------------------------------------------------------------------------------

Merge from Ratan Singh

- Fixed End to End flow
- Fixed Singleton and ConfigParser Issues; changed the name as per PEP Naming conventions
- Made abstract classes as parent in concrete classes
- Refactored routes.py to app.py and deleted folder RestServer
- Added a class for Reading Glove file
- Refactored the interface of contents of Processors

------------------------------------------------------------------------------------------------------------------------------------

26th May Comments from Srinath

 - With current code, we are able to get answers to questions. i have bypassed glove part, so answers are static. You can try     asking questions by using certain unique keywords. Eg. Jailbreaking ios, etc
 - There are preprocessing issues:
    - when you search for ihound, zips etc., response is the para present above the actual para
    - some titles are not matched to their correct para. this is due to the pdf format
    - i tried with the bishop pdf given by ratan, but for some reason its not getting updated in the db itself

------------------------------------------------------------------------------------------------------------------------------------
