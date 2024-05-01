Code/
    Doc. md
    Dockerfile
    requirements. txt
    revhire. db
    users. log

    app/    
        dto
        model
        userfolder
        main.py
        database

U can mount the db to your local system while running

docker run -v /revhire/revhire.db:/path/to/container/revhire.db your-image

Or set it in a way that The app. can understand , in this case that is 

/code/revhire.db
