# Database Table :

# users
    - first_name
    - last_name
    - username
    - phone
    - email
    - photo
    - password
    - created_at

# Posts
    - title
    - body
    - image
    - category -> forignkey (categorirs)
    - tags -> many to many (tags)
    - created_by -> forignkey (Users)
    _ created_at
    - Updated_at

# Categories
    - name 
    - slug

# Tags
    - name
    - slug

# Comments
    - post -> forignkey (posts)
    - commented_by -> forignkey (users)
    - body 
