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
* US-01	 - As a user I want to register an account with administration access.
* US-02	 - As a user I want to be able to log into the website.
* US-03	 - As a user I want to be able to create a list of all the wedding guests.
* US-04	 - As a user I want to maintain the menu options for the day.
* US-05	 - As a user I want to mainttain a wedding gift list.
* US-06	 - As a user I want to use the list of guests who have accept to create the seating plan for the wedding breakfast.
* US-07	 - As a user I want to keep track of which guests have and have not RSVP'ed.
* US-08   - As a user I want to keep track of which guests have or have not supplied their menu choices.
* US-09	 - As a user I want to create a schedule for the day.
* US-10	 - As a user I want to provide the guests with details of the church.
* US-11   - As a user I want to provide the guests with details of the reception.
* US-12   - As a user I want to provide the guests with details of accommodation close to the reception.
* US-13   - As a user I want to provide the guests with details of local public transport.
* US-14   - As a user I want to know who as given a donation so I can thank them after the event.
* US-15   - As a user I want to have the ability to stop any Covid19 restrictions being displayed if the restrictions are lifted.

#### Wedding Guest
* US-16	 - As a user I want to register an account.
* US-17	 - As a user I want to be able to log into the website.
* US-18	 - As a user I want to provide my name and contact details.
* US-19	 - As a user I want to accept the wedding invitation.
* US-20	 - As a user I want to decline the wedding invitation.
* US-21	 - As a user I want to provide details of all members of my party.
* US-22	 - As a user I want to menu selections for all members of my party.
* US-23	 - As a user I want to provide details of any specific dietry requirements.
* US-24	 - As a user I want to choose a present from a list of gift ideas.
* US-25   - As a user I want to give a donation as a wedding present.
* US-26   - As a user I want confirmation of my invitation acceptance or decline.
* US-27   - As a user I want confirmation of my menu choices.
* US-28   - As a user I want confirmaiton of my donation. 

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
I initially used this ![image](documentation/images/colour_scheme.jpg) and [icolorpalette](https://icolorpalette.com/) to create a colour palette but the colours were muted in the palette so went back to the image and selected each of the block colours to find the closest match.

The main background colour will be #FCFCF4 which is almost white and will create a bright and airy feel to the site

* Peach #FFE5B4 RGB(255,229,180)
* * **** FBC8B7     251, 200, 183
* Mint #D1FEC5 RGB(209,254,197)
* * ****B7E0D2 183, 224, 210
* Light Grey #C7C8CA  RGB(199, 200, 202)

<a></a>


#### Fonts
In order to find appropriate fonts for my website, I have visited [Google Fonts](https://fonts.google.com/ "Google Fonts") to explore the various options.

For the initials of the bride and groom I will use the cursive font [Lovers Quarrel](https://fonts.google.com/specimen/Lovers+Quarrel?category=Handwriting&preview.text=C%20%26%20S&preview.text_type=custom#standard-styles), for the titles and subtitles I will use the font [Italianno](https://fonts.google.com/specimen/Italianno?preview.text=GUEST%20Login&preview.text_type=custom&slant=8#standard-styles) tbd
and for the main text I will use [Nunito](https://fonts.google.com/specimen/Nunito?preview.text=GUEST%20Login&preview.text_type=custom&stylecount=11)
`<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Italianno&family=Lovers+Quarrel&family=Nunito:wght@200&display=swap" rel="stylesheet">`
`font-family: 'Italianno', cursive;
font-family: 'Lovers Quarrel', cursive;
font-family: 'Nunito', sans-serif;`
<a></a>

#### Structure
##### Landing / Home Page
    The landing page is designed to welcome the visitors and encouraging them to engage with the site. There will be an image of the bride and groom and some images and highlevel details of the ceremony and reception venues. There will be a `Guests` button which will take the guests to the RSVP page.
    **Our Story Section**
    A small introduction to the bride and groom with a full width carousel of images of the happy couple.
    **Location Section**
    Will show some of the history of York and a map of the area.
    **Covid19 Section**
    The current Covid19 restrictions will be shown here assuming they will still be needed by the date of the wedding.
##### Guest Login
    The guests will be asked to login using a unique identifier, which will be on the wedding invitation and to confirm the postcode where the invitation was sent. From here they will automatically be taken to the RSVP page
##### RSVP Page
    The first time the guest logs in, they will be asked to accept or decline the invitation and there will be the opportunity to leave a message. Subsequently the guest will have a navigation menu where they will have access to the menu, the gifts, the full venue details, the schedule of the day and useful local information. If a guest has declined the invitation they will still have access to buy a gift if they desire.
##### Guests Menu Page
    The guests version of the menu page will have the menu options list and the names of all the guest in that party. There will also be a box under each name to give details of any allergies or special dietry requirements. Sandburn Hall have said they will do their best to accommodate all dietry requirements.  
##### Venue
    Contains some information about the church where the ceremony will be held and about the receiption venue. There will be an image of each venue and the GoogleMaps location.
##### Gifts Page
    This page will have details of any specific gifts the bride and groom would like where the guest wants to buy a present instead of giving the bride and groom money. There will be a donation box for the guest to gift the bride and groom money using **Stripe payments**
##### Wedding Schedule Page
    Full details of the expected schedule of the day will be details here. * time the ceremony starts
    * time of arrival at the reception venue
    * time of the wedding breakfast
    * time of the room turn around
    * time of the evening celebration commences 
##### Guest List Pages
    The guest list page will consist of 3 pages.
    * the main page will allow the bride and groom to view
        * the guests names
        * the number of confirmed guests in that party
        * whether they have accepted or declined the invitation
        * if they selected their menu choices
    * Page 2 will give the bride and groom the ability to add, change and delete guests
    * Page 3 will allow the bride and groom to see the menu choices and what gifts have been selected
##### Menu Maintenance Page
    The bride and groom will be able to add details about the starters, main course and deserts they have chosen for the wedding breakfast.
##### Gift Maintenance Page
    The bridge and groom will 

[Back to Top](#table-of-contents)

--- 
<a></a>

## **Wireframes, Flowcharts and Database Structure**

### **Wireframes**
I used [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website.   
For each page I created 3 wireframes: desktop, tablet and mobile.
**[Landing Page](documentation/wireframes/landing.pdf)**
**[Guest Login](documentation/wireframes/guest_login.pdf)**
**[RSVP Page](documentation/wireframes/rsvp.pdf)**
**[Accepted Page](documentation/wireframes/accepted.pdf)**
**[Declined Page](documentation/wireframes/declined.pdf)**
**[Venue Page](documentation/wireframes/venue.pdf)**
**[Guests Menu Page](documentation/wireframes/guest_menu.pdf)**
**[Guests Gifts Page](documentation/wireframes/guest_gift.pdf)**
**[Bride and Groom Login]()**
**[Guests Wedding Schedule Page](documentation/wireframes/guest_schedule.pdf)**
**[Guest List Enquiry Page]()**
**[Guest List Maintenance Page]()**
**[Menu Maintenance Page](documentation/wireframes/menu_maintenance.pdf)**
**[Gift Maintenance Page](documentation/wireframes/gift_maintenance.pdf)**
**[Wedding Schedule Entry Page](documentation/wireframes/schedule_maintenance.pdf)** 

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

