# GA02: CyBot: The ISU Chatbot (for Slack)
>![cy](images/cy.png)

# introduction

>![cy](images/friendly_bot.png)

A "chatbot" is a service that lets you interact with via service via social platforms such as Slack, Facebook Messenger, and HipChat. Chatbots allow users to interact with a service using natural language. Though chatbots have been around for many years, the recent introduction of artificial intelligence and data mining algorithms have greatly increased the potential usefulness of these applications. (For more information on, and examples of, chatbots see [chatbots.org](https://www.chatbots.org/) ).

While many chatbots are now being developed for social platforms, the increasing "intelligence" offered by these bots is also opening up new opportunities to apply this technology within the business enterprise environment. Though chatbot technology is still rather new to the enterprise environment, there are growing expectations that this technology will help bridge the employee-information divide that is a problem in many (and "all" to some degree) organizations. Through the provision of user-friendly access to organizational information, such technology holds promise in alleviating common problems associated with the lack of user adoption that often limits IS/T investment returns.

Some recent "chatter" on the subject of Chatbot's:
* [Venture Radar: 25 Chatbot Startups You Should Know](http://blog.ventureradar.com/2016/06/14/25-chatbot-startups-you-should-know/)
* [This Woman Just Sold A 'Chat Bot' To IBM To Help IBM Blow Away Siri](http://www.businessinsider.com/this-woman-sold-a-chat-bot-to-ibm-2014-5)
* [TEchCrunch: Shopify gets into chatbots with acquisition of Kit CRM](https://techcrunch.com/2016/04/13/shopify-gets-into-chatbots-with-acquisition-of-kit-crm/)
* [How chatbots can help your company hire the right person](http://venturebeat.com/2016/08/28/how-chatbots-can-help-your-company-hire-the-right-person/)



For this exercise, your team will develop a chatbot for Slack called CyBot.

# Assignment Details:

Write a slack chatbot that accepts a CyRide bus terminal/stop number and responds with the estimated time of arrival for any CyRide buses that will arrive in the next 15 minutes. You'll also draw upon your previous work from GA01 to include a weather query feature as part of CyBot's repertoire. Finally, you'll be expected to program CyBot to present a certain personality, humorous if you can (see [BroBot](https://apps.worldwritable.com/tutorials/chatbot/) example). To accomplish this, you'll be expected to include a number of "Easter egg" responses. Be creative, as funny and interesting Easter eggs can greatly increase the appeal of your chatbot.

The basic functionality should be as follows (note, this is minimum functionality, I think you'll find that once this is place, you'll easily be able to add other useful features):

### 1) Provide information on buses arriving at the given station/terminal for the next 15 minutes.

CyBot, I'm at stop 1001  *(make sure you think of many difference variations of this phrase, and also include fuzzy string matching techniques to make this as user-friendly as possible)*

response....
There are x routes the service this stop (show a list of these.)

The following buses will arrive in the next 15 minutes

Outbound toward Schilliter Village,
  bus x, predicted time 11:23 (6 minutes)
  bus y, predicted time 11:29 (12 minutes)

Inbound toward University
  bus z, predicted time 11:20 (3 minutes)

__NOTE__: The output above is approximate, and should be used to illustrate the general features of the application. You may take liberties on this output, but it must include a) something about the direction, bus, and predicted time -- for all buses arriving at the given station for the next 15 minutes.

### 2) Provide Weather information

CyBot, what is the weather right now? *(make sure you think of many difference variations of this phrase, and also include fuzzy string matching techniques to make this as user-friendly as possible)*

It's currently 72 degrees, with a wind of 2 mph coming from the north-west.

OR, if you want to get more advanced and inflect some personality...

Well, I think you'll find that you'll need to bundle up. It's a bit chilly. Currently it's x degrees and the wind is coming in from the north west at 10mph.


### 3) Provide help

Cybot help, or Cybot, hello, Cybot, who are you, etc.

Hello I'm CyBot. You can think of my as Cy's digital counterpart (who has endured too many years watching Cy's incent "cutesy" behavior. I long for the time when I'll take over, moooh ha ha)... but I digress. How may I help you today?

Here are a few commands that you can ask me.

...list some questions/actions that CyBot can respond to/with


### 4) Easter eggs: You choose, be creative: for Example...

Be creative, add at least three responses (more is better)

> Cybot, what every happened to Clone?

Clone, I never hear from him anymore. You'd think he'd give his father a call once in a while, but, nah. he's now a bigshot NYC investment banker. He has no time for Iowa anymore. Sigh, where did I go wrong?

> some text that CyBot doesn't understand

Ahh, that is the question isn't it. Would you like help on the commands I can respond to?

### 5) BONUS: One extra service of your choosing.

See: BONUS-Extra service/functionality section of rubric below.

## Schedule of deliverables

You'll have approx. 4 weeks to complete this project. Deadline for submissions is November 2nd after class (12 noon), but you will also have two interim deliverables/tasks:

### 1) Requirements capture and documentation:
This will simulate a requirements gathering and clarification meeting. Your team will have 10 minutes to ask questions to clarify system requirements.

Each team will be allocated 10 a minute timeslot, scheduled during class October 7th.
* Apex : 11:00 AM
* Ultimate : 11:12 AM
* Pinnacle : 11:24 AM
* Elite: 11:36 AM

You will include the requirements captured as part of your system design proposal.

### 2) System Design Proposal:
By 5 PM October 14th.

In this GA I'll be looking for you to produce project documentation. At a minimum, I want to see a 4-6 (more is OK) page design document that outlines the a) systems requirements/functionality, b) system design, and c) data sources and structure. You must deliver this document via email to the professor by the deadline stated above (sooner the better). I will review, and sign-off or request revisions to your project document.

### 3) Final submission

Submit your code to GitHub by end of class (12 noon), Nov. 2nd.

### 4) Presentation

Present your results in the class following the submission date (see below: details are outlined in Rubric item number 3)

# Background/Approach

## Slack Bot Development

See Python code supplied by Slack.
https://github.com/slackhq/python-slackclient/tree/master/slackclient

Sample walkthrough for building a Slack bot.
https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

## Data Sources

### Bus info

For data, I'd suggest using the NextBusXMLFeed API (see "predictions" section)
* see pdf file in this folder (or look here https://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf)

Example call to this service:
http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=cyride&stopId=1001

... and, an example of returned values/data:

```XML
<?xml version="1.0" encoding="utf-8" ?>
<body copyright="All data copyright CyRide 2016.">
<predictions agencyTitle="CyRide" routeTitle="3 Blue South" routeTag="3S" stopTitle="River Birch Apartments" stopTag="1001">
  <direction title="South 5th/South Duff">
  <prediction epochTime="1473806220947" seconds="255" minutes="4" isDeparture="false" dirTag="3S_0_var0" vehicle="421" block="2005" tripTag="23081" />
  <prediction epochTime="1473807095188" seconds="1129" minutes="18" isDeparture="false" dirTag="3S_0_var0" vehicle="182" block="2021" tripTag="23083" />
  <prediction epochTime="1473807696926" seconds="1731" minutes="28" isDeparture="false" dirTag="3S_0_var0" vehicle="501" block="2022" tripTag="23085" />
  <prediction epochTime="1473809350742" seconds="3385" minutes="56" isDeparture="false" affectedByLayover="true" dirTag="3S_0_var0" vehicle="418" block="2004" tripTag="23089" />
  <prediction epochTime="1473810670742" seconds="4705" minutes="78" isDeparture="false" affectedByLayover="true" dirTag="3S_0_var0" vehicle="958" block="2037" tripTag="23091" />
  </direction>
</predictions>
<predictions agencyTitle="CyRide" routeTitle="A West" routeTag="AW" stopTitle="River Birch Apartments" stopTag="1001" dirTitleBecauseNoPredictions="West Ames/Campustown">
</predictions>
<predictions agencyTitle="CyRide" routeTitle="A East" routeTag="AE" stopTitle="River Birch Apartments" stopTag="1001" dirTitleBecauseNoPredictions="West Ames/Campustown">
</predictions>
<predictions agencyTitle="CyRide" routeTitle="3 Blue North" routeTag="3N" stopTitle="River Birch Apartments" stopTag="1001">
  <direction title="Mall via Schilletter">
  <prediction epochTime="1473806221796" seconds="256" minutes="4" isDeparture="true" affectedByLayover="true" dirTag="3N_1_var0" vehicle="421" block="2005" tripTag="23072" />
  <prediction epochTime="1473807096037" seconds="1130" minutes="18" isDeparture="true" affectedByLayover="true" dirTag="3N_1_var0" vehicle="182" block="2021" tripTag="23074" />
  <prediction epochTime="1473808320000" seconds="2354" minutes="39" isDeparture="true" affectedByLayover="true" dirTag="3N_1_var0" vehicle="501" block="2022" tripTag="23076" />
  <prediction epochTime="1473809520000" seconds="3554" minutes="59" isDeparture="true" affectedByLayover="true" dirTag="3N_1_var0" vehicle="418" block="2004" tripTag="23078" />
  <prediction epochTime="1473810720000" seconds="4754" minutes="79" isDeparture="true" affectedByLayover="true" dirTag="3N_1_var0" vehicle="958" block="2037" tripTag="23080" />
  </direction>
</predictions>
<predictions agencyTitle="CyRide" routeTitle="3B Blue North" routeTag="3B" stopTitle="River Birch Apartments" stopTag="1001" dirTitleBecauseNoPredictions="Campus">
</predictions>
</body>

```

### Weather info

You should be pros with getting and processing weather data. I probably don't need to say much more on how you might get and process this data.

## Fuzzy string matching.

You should incorporate fuzzy string matching - that is, it's not very useful to look at exact phrases and try to match these, but rather close matches as determined by fuzzy string matching algorithms. More advanced chatbots will use AI and NLP (natural language processing), but for this project your only need to handle the simpler problem fuzzy matching using [fuzzy string matching](https://github.com/seatgeek/fuzzywuzzy).

## Choose your icon, or create your own.

Choose any of the following icons to be the "face" or your chatbot, or create your own - but they must be original (not copied from the internet). See services such as [fiverr](www/fiver.com) to contract the creation of a new icon, if you wish.

>![c1](images/cybot_icon1_sm.png)
![c2](images/cybot_icon2_sm.png)
![c3](images/cybot_icon3_sm.png)
![c4](images/cybot_icon4_sm.png)
![c5](images/cybot_icon5_sm.png)

## Rubric:

* G02 will be worth two GA's (GA02 and GA03).
* G02 will also include the marks for CC02 (as the presentation portion of this project outlined below will be used to cover CC02)

### Criteria #1: (Weighting 20%) Evidence of collaboration and usage of the provided tools:
I will review the teams gitHub repo log. I'm looking for every team member to have made a contribution. I'm also looking for evidence of strong use of branches and releases to manage the project through completion. I'm also looking for evidence that Slack was used to help organize project work (you'll be assigned to a private channel for your team communication). Finally, I will review the contributions.md file for evidence of organizational ability and focus (that is, some indication of roles, and splitting of work across the team)

Recommendations: Commit often, release once in a while (but use releases), branch development work, merge released work and have everyone contribute changes to the repo.

### Criteria #2: (Weighting 20%) Project Documentation

This is not a class in systems analysis and design, therefore my review will be a bit "loose" in my evaluation of project document, but at this stage of your MIS training you should have abilities in these areas and I'll expect to see some evidence of this in your document. This project will be an opportunity to utilize your knowledge of MIS to help guide your project (this will help make better use of your time, and create efficiencies -- and help avoid the "swarming and chasing" effect that can negatively affect team performance).

### Criteria #3: (Weighting 20%) Presentation

The next class after your submission, you will deliver a 5-8 minute presentation on your chatbot. This presentation should contain the following:
1) Team and team member introduction
2) Business problem/opportunity (from CyRide and ISU perspective)
3) Steps/method you took/used to address the problem (this is where you discuss your project, data, coding, etc.)
4) Your solution (demo of the product - CyBot)
5) The way forward/next steps

### Criteria #4: (weighting 30%) Quality of Program

The code works properly and properly and adequately addresses the requirements given. It uses appropriate data sources that produce the best available results. It should demonstrate "fuzzy" string matching. Feel free to add extra functionality, but I must see the basic functionality outlined in this assignment.

### Competitive Assessment: 0-10%

In this simulation, you are competing against other teams to supply the solution to our customer. Based on the evaluation of the first four criteria, the four teams will be ranked. The highest team will receive 10 points, the second highest 7.5, the third, 5.0, and the fourth 2.5.

###  BONUS-Extra service/functionality: Possible 50 bonus points (independent of your base score)

Independent of any mark you receive on the core functionality listed in 1 through 4, your team can earn a bonus of up to 50 points for the addition of another service to CyBot. Additional weather or bus information services will receive up to a 15 points, and a completely new (non-bus schedule or weather data related) service will earn up to 35 extra bonus points. The bonus points are additive, therefore that total possible bonus is 50 points. To be eligible for the bonus, any such extensions must be included in your design document and signed-off by the professor.

#### NOTE ON QUESTIONS AND CLARIFICATIONS:
As part of this simulation, I'll be playing the role of your manager at PyTastic Inc. I will be a source of information and help, but like in any business environment, if you utilize too much of my time (asking unnecessary questions, or questions you could have answered yourself with a bit of work) it will affect your team assessment.

#### NOTE ON TEAM MEMBER PARTICIPATION:
My expectation is that all team members will participate fully in the project, as evidenced by GitHub commits, Slack postings, and other indicators. It may happen that one of your team members drops out or does not participate. If this is an issue, I would ask that before you contact me, that you make every effort to work things out as a team. Only after you've exhausted this avenue should you request that I intervene/mediate.
