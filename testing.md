## Unit and Functional Testing
### Navigation
Due to the image on the landing page the navigation bar was not easily visible on many screen. ![image](images/user-story-images/pre-login-menu.PNG). I modified the `background-color` on `nav-items`, `dropdown-menu` and `show` classes making the navbar stand out much more clearly.![image](images/user-story-images/new-nav.png)


## User Story Testing
#### Bride or Groom:  
**As a user I want to register an account with administration access.**
When a user chooses to register on the site by clicking the 'bride and groom registration' link in the footer they are presented with the registration screen ![image](user_story_docs/register.png). Once registered the user will need to log in. Behind the scenes the user is created with `is_staff` authority. [admin view of bride or groom user settings](user_story_docs/siobhanbaines _ is_staff_user.pdf) 
**As a user I want to be able to log into the website.**
When a user clicks the login navigation option they are presented with the login screen. ![image](user_story_docs/log-in.png) which takes them to the main menu for the bride and groom ![image](user_story_docs/bride-groom-nav-dropdown.png)
**As a user I want to be able to create a list of all the wedding guests.**
The Maintenance Views menu option has a drop-down menu giving acces to the [Guest List](user_story_docs/guest_list_maint.png) maintenance screen which has the ability to upload a [guest csv file](user_story_docs/guest-list.csv) into to guest model. The search facilty gives a wild card search on the first and last names of the guest. If the user enters the letter `r` in the search box, all guests with the letter r in their name will be displayed.![image](user_story_docs/guest_search.png). 
The guest details can be viewed, changed or deleted by the user. 
**As a user I want to maintain a wedding gift list.**
The gifts maintenance screen has the ability to upload a [gifts csv file](user_story_docs/gift-list.csv)into the gift model.
**As a user I want to use the list of guests who have accept to create the seating plan for the wedding breakfast.**
**As a user I want to keep track of which guests have and have not RSVP'ed.**
The Guest List maintenance screen shows whether or not the guest has accepted, declined or not responded to the invitation.
**As a user I want to keep track of which guests have or have not supplied their menu choices.**
The Guest List maintenance screen shows whether or not the guest has made their selection from the menu choices. To see what those choics are each guest can be viewed individually.
**As a user I want to create a schedule for the day.**
**As a user I want to provide the guests with details of the church.**
**As a user I want to provide the guests with details of the reception.**
**As a user I want to provide the guests with details of accommodation close to the reception.**
**As a user I want to provide the guests with details of local public transport.**
**As a user I want to know who as given a donation so I can thank them after the event.**
**As a user I want to have the ability to stop any Covid19 restrictions being displayed if the restrictions are lifted.**
#### Wedding Guest
**As a user I want to be able to log into the website.**
When a user clicks the login navigation option they are presented with the login screen. ![image](user_story_docs/log-in.png) which takes them to the rsvp menu for the guest ![image](***)
**As a user I want to provide my name and contact details.**
**As a user I want to accept the wedding invitation.**
**As a user I want to decline the wedding invitation.**
**As a user I want to provide details of all members of my party.**
**As a user I want to menu selections for all members of my party.**
**As a user I want to provide details of any specific dietry requirements.**
**As a user I want to choose a present from a list of gift ideas.**
**As a user I want to give a donation as a wedding present.**
**As a user I want confirmation of my invitation acceptance or decline.**
**As a user I want confirmation of my menu choices.**
**As a user I want confirmation of my donation.**
