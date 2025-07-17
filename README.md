# Chatroom Project Using Django Rest Framework

## User app


### /user/signup

#### POST 
   - username
   - password
   - first_name
   - last_name
   - email
   

### /user/login

#### POST 
   - username
   - password


### /user/profile

#### PUT: edit profile

   - first_name
   - last_name
   

### /user/list

#### GET: get users list




## Chat app


### /chat/conversation

#### POST
   - conversation_name
   - members (list of user IDs)


#### GET: list of all conversations


### /chat/message

#### POST
   - conversation_id
   - text 
 
 
#### PUT: edit
   - message_id
   - text


#### GET: return all messages of conversation_id
