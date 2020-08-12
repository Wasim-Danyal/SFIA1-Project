# SFIA1  Forex CRUD Project

**Resources**:

Presentation:https://docs.google.com/presentation/d/1_j8YKTFPiPMVG5PN1A7zjcLkqHM93siFp9QTMU5tOUM/edit#slide=id.g8e59126c67_0_34

Jira Board:[https://wdprojects.atlassian.net/jira/software/projects/SFIA/boards/5](https://wdprojects.atlassian.net/jira/software/projects/SFIA/boards/5)

## Project Brief

The overall project brief I have been assigned is: "To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training." The original idea was to use an API for frequent updates and live tracking on rates as well as allowing users to manually update the rates. Due to the complexity at this stage, only the initial CRUD functionalities were a realistic approach to the project brief. I still wanted to continue with a currency tracker application. After looking at the project scope and comparing it with possibilities in regards to the current stage i am at with learning about the technologies. I decided the best way to tackle the CRUD scope was to design a forex rate tracker application that allows users to create, read, update and delete forex rates, as well as having a relational database between users and rates to meet the requirements for a relational database.

**Additional Requirements**:

 - A Trello board (or equivalent Kanban board tech)
 - Clear documentation
 - Functional CRUD application made in python
 - Test suites and automated tests
 - Code integrated with VCS and working with feature branch model

**My Approach**:
To achieve this my plan was to create a functioning application that allows a user to:
 - **CREATE** new rates by submitting information through a form.
 - **READ** rates information submitted from the form.
 - **UPDATE** existing rates, the user can change values.
 - **DELETE** rates on the rates page, the rate is then deleted from the database.
Users are able to post currency exchange rates and update them, this is viewable by other users so they can keep track of rates. 
## Database Structure
![enter image description here](https://raw.githubusercontent.com/Wasim-Danyal/Forex-Project/docs/documentation/db.png)

The database has a one user to many rates relationship. Users can post multiple rates.

## CI Pipeline
Pictured below is the CI Pipeline used for the integration of this project. The process starts from pushing code to github from my local machine. Via a webhook, Jenkins runs tests previously written in a test environment, if the tests are successful it deploys the application in a production environment with Gunicorn.

![enter image description here](https://raw.githubusercontent.com/Wasim-Danyal/Forex-Project/master/documentation/CIPipeline.png)

## Project Tracking
For project tracking, Jira was used.The reason Jira was chosen was because of the simple and understandable layout. Roadmap, Backlog and other resources are easy to keep track of and graphs are formed in real time. Below is an image of a sprint in progress:
![enter image description here](https://raw.githubusercontent.com/Wasim-Danyal/Forex-Project/docs/documentation/jira.png)
Once backlog is selected for a sprint it goes through multiple points before it is finally complete.

 - *In progress -* User story has been selected and is in progress
 - *Testing -* If User story requires testing for example code, then it is moved here to be tested before being assigned "Done"
 - *Done -* This is the final point where user stories are assigned completion.

## Testing
For testing the coverage report shows 75% coverage. The coverage report is below:


![enter image description here](https://raw.githubusercontent.com/Wasim-Danyal/Forex-Project/docs/documentation/coverage.png)

## Risk Assessment
![enter image description here](https://raw.githubusercontent.com/Wasim-Danyal/Forex-Project/docs/documentation/riskassessment.png)
## Future Improvements

 - Design overhaul to make the front end more aesthetically appealing for the user.
 - Implementation of an API to regularly update with live rates for users to see instead of manually adding rates.
 - Comparison of rates from different sites.
 - Ability for users to "follow" rates and keep track on their own user page.
## Known Issues

 - If a user enters more characters than specified in bid rate or ask rate, they sometimes end up with an error.

## Author 
Wasim Danyal
