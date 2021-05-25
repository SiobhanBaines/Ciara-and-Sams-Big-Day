# **Ciara and Sam's Big Day**

## **Project Outline** 
This is my final project as part of the Full Stack Development Diploma with Code Institute, acreditted by Edinburgh Napier University. 

The remit for this project was to build "Full Stack Frameworks with Django".

This site will provide the bride and groom with the ability to provide their wedding guests with all the information they need for the day and a mechanism to accept or decline the invitation, decide which menu choices each memeber in the guests party want and chose a wedding gift, whether that is a physical item or a monetary donation. The bride and groom will have all the information they need to chase any guests who have not replied to the invitation and arrange the table seating based on the guests who have accepted.

``` Mock up Image ```
![image](static/documentation_files/images/ami_responsivedesign.png)
You can find the original website here []().

---

<a></a>

## Table of contents 
* [UX](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Colors](#colors)
        * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

<a></a>

### **User Goals**

* The landing page should have a romantic wedding feel for the couple and provide some details about the occaision to the guests who will be invited to create an account.
* The website must 
  * be responsive on all types of devices including mobile phones, tables and desktops.
  * have the ability to maintain the guest list, menu, gift list and schedule for the day including venue details.
  * have the ability to make financial transactions, i.e. allow the guests to give money as a wedding gift. 
  * have details about the local area including alternative accommodation an public transport information.
  * include any Covid19 requirements which can be switched of if no longer needed.
* The website must be visually appealing to the bride and groom.

[Back to Top](#table-of-contents)

<a></a>

### **User Stories**

#### Bride or Groom:  
* #BR-US1	 - As a user I want to register an account with administration access.
* #BR-US2	 - As a user I want to be able to log into the website.
* #BR-US3	 - As a user I want to be able to create a list of all the wedding guests.
* #BR-US4	 - As a user I want to maintain the menu options for the day.
* #BR-US5	 - As a user I want to mainttain a wedding gift list.
* #BR-US6	 - As a user I want to use the list of guests who have accept to create the seating plan for the wedding breakfast.
* #BR-US7	 - As a user I want to keep track of which guests have and have not RSVP'ed.
* #BR-US8    - As a user I want to keep track of which guests have or have not supplied their menu choices.
* #BR-US9	 - As a user I want to create a schedule for the day.
* #BR-US10	 - As a user I want to provide the guests with details of the church.
* #BR-US11   - As a user I want to provide the guests with details of the reception.
* #BR-US12   - As a user I want to provide the guests with details of accommodation close to the reception.
* #BR-US13   - As a user I want to provide the guests with details of local public transport.
* #BR-US14   - As a user I want to know who as given a donation so I can thank them after the event.
* #BR-US15   - As a user I want to have the ability to stop any Covid19 restrictions being displayed if the restrictions are lifted.

#### Wedding Guest
* #WG-US1	 - As a user I want to register an account.
* #WG-US2	 - As a user I want to be able to log into the website.
* #WG-US3	 - As a user I want to provide my name and contact details.
* #WG-US4	 - As a user I want to accept the wedding invitation.
* #WG-US5	 - As a user I want to decline the wedding invitation.
* #WG-US6	 - As a user I want to provide details of all members of my party.
* #WG-US7	 - As a user I want to menu selections for all members of my party.
* #WG-US8	 - As a user I want to provide details of any specific dietry requirements.
* #WG-US9	 - As a user I want to choose a present from a list of gift ideas.
* #WG-US10   - As a user I want to give a donation as a wedding present.
* #WG-US11   - As a user I want confirmation of my invitation acceptance or decline.
* #WG-US12   - As a user I want confirmation of my menu choices.
* #WG-US13   - As a user I want confirmaiton of my donation. 

<a></a>


[Back to Top](#table-of-contents)

<a></a>

### **User Requirements and Expectations**

<a></a>

#### Requirements

* Easy to navigate by having a responsive navigation bar and various links to other pages througout the site.
* Romantic design in keeping with the bride and grooms chosen colour scheme.
* Bride and Groom
   * Easy maintenance of the guest list, the wedding breakfast menu, the schedule, covid19 restrictions and the gift list.
* Guests 
   * need to be able to easily RSVP the invitation.
   * be able to give a wedding gift
   * update their contact details
   * If the guests accept the invitation they will need to 
      * be able to choose from the menu options for each member of their party. 
* Provide location information of the ceremony and receiption
* Provide other local information

<a></a>

#### Expectations

* When clicking on links to external pages, I expect them to open in a different window.
* When the guests click the GUEST button I expect them to be taken to the RSVP page.
* I expect an email to be sent to the bride and groom and specfic flags to be updated when
   * the guest have RSVP'ed
   * the guest have selected from the menu options
   * if the guest sends a monetory donation including the amount of that donation
   * if a guest selects to buy a gift
* I expect the bride and groom to be able to search on the guest list by the various flags to check the status


[Back to Top](#table-of-contents)

<a></a>

### **Design Choices**

In designing this site I want to incorporate the bride and grooms colour scheme (mint green and peach) with the rustic but romantic feel of the venue with it's open beams and stunning views across the golf course. To make it special to Ciara and Sam a photograph of them will appear on the landing page.

##### Church 
[St Margaret Clitherow](http://stmargaretclitherowyork.org.uk/)
<a></a>

##### Receiption
[Sandburn Hall](https://www.sandburnhall.co.uk/)

#### Colors

The colours of the site are taken from the colour scheme the bride and groom have decided on which is mint green and peach. I have chosen to make the main colour off-white to keep the site bright and airy without being stark that would come with bright white as the main colour.
I initially used this ![image]() and [icolorpalette](https://icolorpalette.com/) to create a colour palette but the colours were muted in the palette.

* Peach #FFE5B4 RGB(255,229,180)
* Mint #D1FEC5 RGB(209,254,197)

<a></a>


#### Fonts
In order to find appropriate fonts for my website, I have visited [Google Fonts](https://fonts.google.com/ "Google Fonts") to explore the various options.
For the initials of the bride and groom I will use a cursive font -tbd
For the titles and subtitles, I will use the font []() tbd
and for the main text I have used [](). tbd

<a></a>

#### Structure


[Back to Top](#table-of-contents)

--- 
<a></a>

## **Wireframes, Flowcharts and Database Structure**

### **Wireframes**
I used [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website.   
For each page I created 3 wireframes: desktop, tablet and mobile.



### **Flowcharts**


### **Database Structure**


[Back to Top](#table-of-contents)

---

<a></a>

## **Features**

<a></a>

### **Existing Features**



<a></a>

### **Features to be implemented**


[Back to Top](#table-of-contents)

<a></a>

## **Technologies used**

<a></a>

### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

<a></a>

### **Libraries and Frameworks**

* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)
* [Stripe](http://stripe.com/)

### **Tools**
* [Django](https://www.djangoproject.com/)
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [techsini](http://techsini.com/)
* jshint


[Back to Top](#table-of-contents)

<a></a>

## Testing
Testing of this site can be found [here](testing.md) in a seperate file

## Bugs
Bugs of this site can be found [here](bugs.md) in a seperate file


## **Deployment**

### Local Deployment



    
### To deploy your project on Heroku, use the following steps: 

[Back to Top](#table-of-contents)

<a></a>

## **Credits**

