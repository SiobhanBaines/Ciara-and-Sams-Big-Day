### Site Users Creation
As part of this project I needed to create some Users automatically into django. Initially I started by trying to create a model and found I would need to Hash the password. I also wanted to create a UUID for each of the guest users. I tried multiple different ideas from [StackOverflow](https://stackoverflow.com/search?q=upload+users+to+django) and read lots of the [django](https://docs.djangoproject.com/en/3.2/topics/auth/) documentation. After many hours I talked to Code Institutes tutor support team and one of the main issues was I did not need to create a model for the users.json table because it already existed as standard. 
When I ran the `python3 manage.py loaddata users` command I still got an error but this was related to the encoder my git environment was using. It was using `UFT-8 with BOM` and needed to user `UFT-8`. 
Once the users were loaded, the next step was to change the passwords to be hashed and the username to be a 6 character UUID using `uuid.uuid4().hex[:6].upper()`.

Complete change of plan. I'm going to create the users from the upload of the guest list. That way it is all inside the app instead of trying to createheroku logs --tail them outside of it. This also puts the ownership of the data bak onto the person uploading it.

I originally had the upload process as part of a modal but nothing I did seemed to get it to load into admin/. I raised a call with tutor support and Jo @ CI gave me this link [upload-csv](https://ramramesh1374.medium.com/upload-csv-using-django-bulk-create-c75b28fc19f0) This helped witht he format of the view but I still had issues with the urls. Eventually I realise I had 2 get processes which was why the post view was not being processed. 

