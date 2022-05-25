# See-Suite - Back-end API - Team 2 International Aid Hackathon Application (05.03.2022 to 05.05.2022)

[Click Here to View the Front-End Sister Application](https://github.com/BootsStribling/international-aid-FE)

## ABOUT
This project was constructed as part of an General Assembly Hackathon for an international aid organization called Unlocking Communities. Unlocking Communities is an organization that "...equips entrepreneurs with the education and tools to sell sustainable products that unlock economic, social, and environmental transformation in their communities." More information about Unlocking Communities can be found [here.](https://unlockingcommunities.org/our-mission/)

The Hackathon parameters were to create an application with at least one feature that tracked some portion of the entrepreneur sales or inventory and represent that data to both C-level executives and local entrepreneur managers in low-bandwidth areas of the world. From an engineering standpoint, we created this coupled application to handle data received by other teams' applications, namely Team 1 - (Android Application Development Team), and represent that data as a tracking software to indicate which communties and entrepreneurs needed additional training and support.

From research to presentation of this application we were given 60 hours to work.

## AWARDS -  🎗 🥈 2nd Place 🥈 🎗

## OUR TEAM

- ![Meagan Bleach](./api/public/images/team/meagan-bleach.png) 
  [Meagan Bleach](https://www.linkedin.com/in/meaganbleach/) - UI/UX Designer
- ![Rachel Wynne-Bernstein](./api/public/images/team/rachel-wynne-bernstein.png)
  [Rachel Wynne-Bernstein](https://www.linkedin.com/in/rachelwynnebernstein/) - UI/UX Designer
- ![Talon Krell](./api/public/images/team/talon-krell.png)
  [Talon Krell](https://www.linkedin.com/in/talon-krell/) - UI/UX Designer
- ![Robb Herndon](./api/public/images/team/robb-herndon.png)
[Robb Herndon](https://github.com/robbherndon) - Data Scientist
- ![Najee Simmons](./api/public/images/team/najee-simmons.png)
[Najee Simmons](https://github.com/najeesimmons) - Software Engineer
- ![Haziq Naeem](./api/public/images/team/haziq-naeem.png)
[Haziq Naeem](https://github.com/Haziq12) - Software Engineer
- ![Bredell Evans](./api/public/images/team/bredell-evans.png)
[Bredell Evans](https://github.com/bredy452) - Software Engineer
- ![Boots Stribling](./api/public/images/team/boots-stribling.png)
[Boots Stribling](https://github.com/BootsStribling) - Software Engineer - Scrum Master

## Design
  ### Tech Used
  ![](https://img.shields.io/badge/-FIGMA-F24E1E?style=flat-square&logo=figma5&logoColor=white)

  ![](./public/images/Design-Landing-half.png)
  ![](./public/images/Design-Sales-half.png)

## Front-End Implementation
  ### Tech Used
  ![](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) 
  ![](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3) 
  ![](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) 
  ![](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=React&logoColor=black) 
  ![](https://img.shields.io/badge/-NodeJS-339933?style=flat-square&logo=Node.js&logoColor=white) 
  ![](https://img.shields.io/badge/-React_Router-CA4245?style=flat-square&for-the-badge&logo=react-router&logoColor=white) 
  ![](https://img.shields.io/badge/-Express-404D59?style=flat-square&for-the-badge&logo=express)

  ![](./public/images/Front-end-landing-half.png)
  ![](./public/images/frontend-sales.png)

  * Designed to load quickly and cleanly in low-bandwidth environments, we implemented a pie-chart npm package called [React-Minimal-Pie-Chart](https://www.npmjs.com/package/react-minimal-pie-chart) to make the load weight and time much quicker on the front-end.
  * Accordion style floating nav-bar with buttons to change pie-chart through RESTful API calls to backend for data.

## Back-End Implementation
  ### Tech Used
  ![](https://img.shields.io/badge/-Python3-3776AB?style=flat-square&logo=Python&logoColor=white) 
  ![](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white)
  ![](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
  ![](https://img.shields.io/badge/-Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white)

  ![ERD](./public/images/ERD.png)

  * Using Flask, SQLAlchemy and PostGreSQL we implemented a constructive API focusing on transactions as the most elemental level of the represenation
  * We built routes with queries to the PostGreSQL database to allow for summation of transaction totals for representation.
  * The totals were sent in lightweight JSON format. Data was only one array comprising [Transaction Total, Loan Total, Cash Total]
  * Transaction creation routes were created for eventual integration into Android Mobile App designed by Team 1
  * Python scripting was written for migration of data from Salesforce CSV files to new PostGres Database

## V2 Expectations
  This project, along with the other 4 teams who participated, was handed to Deloitte as a prototype for them to build the working application with. While we do not know the status of that application, we certainly hope that our time and code was used effectively to the aid of those in the countries it was deployed in. 
