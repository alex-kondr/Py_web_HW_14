Welcome to App Contact’s documentation!
App Contact’s main
async main.add_process_time_header(request: Request, call_next)
The add_process_time_header function is a middleware function that adds the time it took to process the request in seconds as a header called Process-Time. This can be useful for debugging purposes.

Parameters:
request – Request: Get the request object

call_next – Call the next middleware in the chain

Returns:
A response object with a header

main.read_root()
The read_root function returns a dictionary with the key message and value Hello world!.

Returns:
A dictionary with a single key, message

async main.startup()
The startup function is called when the application starts up. It’s a good place to initialize things that are needed by your app, such as databases or caches.

Returns:
A coroutine, which is a function that returns

App Contact’s database db
src.database.db.get_db()
The get_db function is a context manager that returns the database session. It also ensures that the connection to the database is closed after each request.

Returns:
A database sessionlocal object

Doc-author:
Trelent

App Contact’s repository Contacts
async src.repository.contacts.create_contact(body: ContactBase, user: User, db: Session) → Contact
The create_contact function creates a new contact in the database.

Parameters:
body – ContactBase: Get the data from the request body

user – User: Get the user id from the jwt token

db – Session: Access the database

Returns:
A contact object

async src.repository.contacts.get_contact(contact_id: int, user: User, db: Session) → Contact
The get_contact function is used to retrieve a contact from the database.
It takes in three parameters:
contact_id: The id of the contact you want to retrieve.

user: The user who is requesting this information (used for authorization).

db: A connection to the database that will be used for querying.

Parameters:
contact_id – int: Get the contact from the database

user – User: Check if the user is an admin or moderator, and can therefore view all contacts

db – Session: Access the database

Returns:
A contact object for a given id

async src.repository.contacts.get_contact_by_fields(user: User, db: Session, first_name: str | None = None, last_name: str | None = None, phone: str | None = None, email: str | None = None, days_before_birth: int | None = None) → List[Type[Contact]]
The get_contact_by_fields function is used to search for contacts by any of the following fields: first_name, last_name, phone, email and days_before_birth. The function returns a list of all contacts that match the given criteria.

Parameters:
user – User: Ensure that the user is logged in and has access to the database

db – Session: Pass the database session to the function

first_name – str: Filter the contacts by first name

last_name – str: Filter the contacts by last name

phone – str: Filter the contacts by phone number

email – str: Filter the contacts by email

days_before_birth – int: Filter the contacts by their birthday

Returns:
All contacts that match the specified fields

async src.repository.contacts.get_contacts(skip: int, limit: int, user: User, db: Session) → List[Contact]
The get_contacts function is used to retrieve a list of contacts from the database. The function takes in three parameters: skip, limit, and user. The skip parameter is an integer that specifies how many contacts should be skipped before retrieving the next set of contacts. The limit parameter is an integer that specifies how many contacts should be retrieved at once (the maximum number). Finally, the user parameter represents a User object which contains information about who made this request for contact data.

Parameters:
skip – int: Skip the first n contacts in the database

limit – int: Limit the number of contacts returned

user – User: Check the role of the user making the request

db – Session: Access the database

Returns:
A list of contacts, which is a list of dictionaries

async src.repository.contacts.remove_contact(contact_id: int, user: User, db: Session) → Contact | None
The remove_contact function removes a contact from the database.
Args:
contact_id (int): The id of the contact to be removed. user (User): The user who is removing the contact. db (Session): A connection to our database, used for querying and deleting contacts.

Parameters:
contact_id – int: Identify the contact to be removed

user – User: Check if the user is authorized to delete a contact

db – Session: Access the database

Returns:
The contact that was removed

async src.repository.contacts.update_avatar(contact_id: int, file: UploadFile, user: User, db: Session) → Contact | None
The update_avatar function updates the avatar of a contact. Args: contact_id (int): The id of the contact to update. file (UploadFile): The new avatar image for the user. user (User): The current logged-in user, used to verify that they are updating their own account and not someone else’s.

Parameters:
contact_id – int: Find the contact in the database

file – UploadFile: Upload the avatar to the database

user – User: Check if the user is authorized to update the contact

db – Session: Access the database

Returns:
The updated contact

async src.repository.contacts.update_contact(contact_id: int, body: ContactUpdate, user: User, db: Session) → Contact | None
The update_contact function updates a contact in the database. Args: contact_id (int): The id of the contact to update. body (ContactUpdate): The updated information for the specified user’s contact. user (User): The current logged-in user, used to verify that they are updating their own data and not someone else’s.

Parameters:
contact_id – int: Identify the contact to be deleted

body – ContactUpdate: Pass the updated contact information to the function

user – User: Get the user id from the jwt token

db – Session: Access the database

Returns:
The updated contact

async src.repository.contacts.update_email_contact(contact_id: int, body: ContactEmailUpdate, user: User, db: Session) → Contact | None
The update_email_contact function updates the email of a contact in the database.

Parameters:
contact_id – int: Identify the contact to be updated

body – ContactEmailUpdate: Pass the new email address to be updated

user – User: Check if the user is authorized to update a contact

db – Session: Pass in the database session

Returns:
The updated contact

App Contact’s repository Groups
async src.repository.groups.create_group(body: GroupModel, user: User, db: Session) → Group
The create_group function creates a new group in the database.

Parameters:
body – GroupModel: Create a new group

user – User: Get the user id from the token

db – Session: Access the database

Returns:
A group object

async src.repository.groups.get_group(group_id: int, db: Session) → Group | None
The get_group function takes in a group_id and a database session, and returns the Group object with that id. If no such group exists, it returns None.

Parameters:
group_id – int: Specify the group id of the group that is being queried

db – Session: Pass the database session to the function

Returns:
The group object

async src.repository.groups.get_groups(skip: int, limit: int, db: Session) → List[Type[Group]]
The get_groups function returns a list of groups from the database.

Parameters:
skip – int: Skip a certain number of records

limit – int: Limit the number of groups returned

db – Session: Pass the database session to the function

Returns:
A list of group objects

async src.repository.groups.remove_group(group_id: int, user: User, db: Session) → Group | None
The remove_group function removes a group from the database.
Args:
group_id (int): The id of the group to be removed. user (User): The user who owns the group to be removed. db (Session): A connection to our database, used for querying and deleting groups.

Parameters:
group_id – int: Identify the group to be removed

user – User: Get the user id of the group owner

db – Session: Access the database

Returns:
The group that was removed

async src.repository.groups.update_group(group_id: int, body: GroupUpdate, user: User, db: Session) → Group | None
The update_group function updates a group in the database.
Args:
group_id (int): The id of the group to update. body (GroupUpdate): The updated information for the specified Group object. user (User): The User object that is making this request, used to verify ownership of this Group object.

Parameters:
group_id – int: Identify the group to be deleted

body – GroupUpdate: Pass the name of the group to be updated

user – User: Check if the user is authorized to delete a group

db – Session: Access the database

Returns:
The updated group object

App Contact’s repository Users
async src.repository.users.confirmed_email(user: User, db: Session) → None
The confirmed_email function is called when a user confirms their email address. It sets the confirmed field of the User object to True, and commits it to the database.

Parameters:
user – User: Pass the user object to the function

db – Session: Access the database

Returns:
None, because it does not have a return statement

async src.repository.users.create_user(body: UserModel, db: Session) → User
The create_user function creates a new user in the database.
Args:
body (UserModel): The UserModel object containing the data to be inserted into the database. db (Session): The SQLAlchemy Session object used to interact with our PostgresSQL database.

Parameters:
body – UserModel: Validate the request body

db – Session: Access the database

Returns:
A user object

async src.repository.users.get_user_by_email(email: str, db: Session) → Type[User] | None
The get_user_by_email function takes in an email and a database session, and returns the user associated with that email. If no such user exists, it returns None.

Parameters:
email – str: Pass the email address of the user to be retrieved

db – Session: Pass the database session to the function

Returns:
The first user with the given email, or none if no such user exists

async src.repository.users.save_new_password(user: User, password_hash: str, db: Session) → None
The save_new_password function takes a user object, a password hash, and the database session as arguments. It then sets the user’s password to be equal to the new password hash. Finally, it commits this change to the database.

Parameters:
user – User: Get the user object from the database

password_hash – str: Pass in the hashed password

db – Session: Pass the database session to the function

Returns:
None

async src.repository.users.update_avatar(email: str, url: str, db: Session) → Type[User] | None
The update_avatar function updates the avatar of a user in the database.

Parameters:
email – str: Identify the user

url – str: Update the avatar url of a user

db – Session: Pass the database session to the function

Returns:
A user object, or none if the user was not found

async src.repository.users.update_token(user: User, token: str | None, db: Session) → None
The update_token function updates the refresh token for a user.

Parameters:
user – User: Get the user’s id

token – Optional[str]: Specify that the token parameter is optional

db – Session: Pass the database session to the function

Returns:
None

async src.repository.users.update_user(body: UserUpdate, user: User, db: Session) → User
The update_user function updates a user in the database.
Args:
body (UserUpdate): The updated user information. user (User): The current version of the User object to be updated. db (Session): A connection to the database that will be used for updating and refreshing data.

Parameters:
body – UserUpdate: Get the data from the request body

user – User: Get the user from the database

db – Session: Access the database

Returns:
A user object

App Contact’s router Auth
async src.routes.auth.confirmed_email(token: str, db: Session = Depends(get_db)) → dict
The confirmed_email function is used to confirm a user’s email address.
It takes in the token that was sent to the user’s email and checks if it is valid. If it is, then we set the confirmed field of that user to True.

Parameters:
token – str: Get the email and type from the token

db – Session: Get the database session

Returns:
The message that the email has been confirmed

async src.routes.auth.forgot_password(body: RequestEmail, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)) → dict
The forgot_password function is used to send an email to the user with a link to reset their password. The function takes in a RequestEmail object, which contains the user’s email address. It then checks if the user exists and if they have confirmed their account (if not, it raises an exception). If everything is okay, it sends them an email with instructions on how to reset their password.

Parameters:
body – RequestEmail: Get the email from the request body

background_tasks – BackgroundTasks: Add a task to the background tasks queue

request – Request: Get the base_url of the application

db – Session: Get the database session

Returns:
A dict with a message

async src.routes.auth.login(body: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_db)) → dict
The login function is used to authenticate a user.
It takes in the username and password of the user, and returns an access token if successful. The access token can be used to make requests on behalf of that user.

Parameters:
body – OAuth2PasswordRequestForm: Get the username and password from the request body

db – Session: Access the database

Returns:
A dictionary with the access token, refresh token and bearer

async src.routes.auth.refresh_token(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer), db: Session = Depends(get_db)) → dict
The refresh_token function is used to refresh the access token.
The function takes in a refresh token and returns an access_token, a new refresh_token, and the type of token.

Parameters:
credentials – HTTPAuthorizationCredentials: Get the access token from the request header

db – Session: Get the database session

Returns:
A dictionary with the new access_token, refresh_token and token type

async src.routes.auth.request_email(body: RequestEmail, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)) → dict
The request_email function is used to send a confirmation email to the user.
The function takes in an email address and sends a confirmation link to that address. If the user does not exist, it returns an error message.

Parameters:
body – RequestEmail: Validate the request body

background_tasks – BackgroundTasks: Add a task to the background tasks queue

request – Request: Get the base_url of the application

db – Session: Pass the database session to the repository functions

Returns:
A message to the user if they are already confirmed

async src.routes.auth.reset_password(token: str, body: UpdatePassword, db: Session = Depends(get_db)) → dict
The reset_password function takes a token and a body as arguments. The token is used to verify the user’s email address, while the body contains the new password. If verification fails, an HTTP 400 error is raised. Otherwise, the function saves the new password in database.

Parameters:
token – str: Get the email and type of token from the database

body – UpdatePassword: Get the new password from the user

db – Session: Pass the database session to the function

Returns:
A dict with a message

async src.routes.auth.singup(body: UserModel, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)) → dict
The singup function creates a new user in the database.
It takes an email, username and password as input parameters. The function returns a JSON object with the newly created user’s information.

Parameters:
body – UserModel: Validate the data sent by the user

background_tasks – BackgroundTasks: Add a task to the background tasks queue

request – Request: Get the host url to send in the email

db – Session: Get the database session

Returns:
A dictionary with the user and a message

App Contact’s router Contacts
async src.routes.contacts.create_contact(body: ContactBase, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → Contact
The create_contact function creates a new contact in the database.

Parameters:
body – ContactBase: Get the data from the request body

current_user – User: Get the user that is currently logged-in

db – Session: Pass the database session to the repository

Returns:
A contact object

async src.routes.contacts.find_contacts_by_fields(first_name: str | None = None, last_name: str | None = None, phone: str | None = None, email: str | None = None, days_before_birth: int = 7, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → List[Type[Contact]]
The find_contacts_by_fields function is used to find contacts by first name, last name, phone number and email. It also allows the user to specify how many days before a contact’s birthday they want to be notified.

Parameters:
first_name – str: Specify the first name of the contact to be found

last_name – str: Find the contact by last name

phone – str: Search for a contact by phone number

email – str: Find a contact by email

days_before_birth – int: Find contacts that have their birthdays in the next 7 days

current_user – User: Get the current user

db – Session: Pass the database session to the repository layer

Returns:
A list of contacts

async src.routes.contacts.read_contact(contact_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → Contact
The read_contact function is used to retrieve a single contact from the database. It takes in an integer representing the ID of the contact, and returns a Contact object.

Parameters:
contact_id – int: Specify the contact id

current_user – User: Get the current user from the database

db – Session: Pass the database session to the repository layer

Returns:
The contact object

async src.routes.contacts.read_contacts(skip: int = 0, limit: int = 9, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → List[Contact]
The read_contacts function returns a list of contacts.

Parameters:
skip – int: Skip the first n contacts

limit – int: Limit the number of contacts returned

current_user – User: Get the current user from the token

db – Session: Pass the database session to the repository layer

Returns:
A list of contacts

async src.routes.contacts.remove_contact(contact_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → Contact
The remove_contact function removes a contact from the database.

Parameters:
contact_id – int: Specify the contact to be deleted

current_user – User: Get the current user from the database

db – Session: Pass the database session to the repository layer

Returns:
The contact that was deleted

async src.routes.contacts.update_avatar(contact_id: int, file: UploadFile = File(PydanticUndefined), current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → Contact
The update_avatar function updates the avatar of a contact.
The function takes in an integer representing the id of the contact to be updated, and a file object containing information about the new avatar image.

Parameters:
contact_id – int: Identify the contact to be updated

file – UploadFile: Upload the file to the server

current_user – User: Get the current user

db – Session: Pass the database session to the repository layer

Returns:
A contact object

async src.routes.contacts.update_contact(body: ContactUpdate, contact_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → Contact
The update_contact function updates a contact in the database.
The function takes an id of the contact to update, and a ContactUpdate object containing all fields that should be updated.

Parameters:
body – ContactUpdate: Get the data from the request body

contact_id – int: Specify the id of the contact to be deleted

current_user – User: Get the current user from the database

db – Session: Pass the database session to the repository

Returns:
A contact object

App Contact’s router Groups
async src.routes.groups.create_group(body: GroupModel, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) → Group
async src.routes.groups.read_group(group_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) → Type[Group]
The read_group function will return a group with the given ID.

Parameters:
group_id – int: Get the group from the database

db – Session: Get the database session

current_user – User: Check if the user is a member of the group

Returns:
A group

async src.routes.groups.read_groups(skip: int = 0, limit: int = 9, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) → List[Type[Group]]
The read_groups function returns a list of groups.

Parameters:
skip – int: Skip the first n groups

limit – int: Limit the number of groups returned

db – Session: Pass the database session to the repository layer

current_user – User: Get the current user

Returns:
A list of groups

async src.routes.groups.remove_group(group_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) → Group
The remove_group function removes a group from the database.
It requires an admin or moderator to be logged in, and it takes a group_id as input. If the user is not an admin or moderator, they will receive a 403 error code. If there is no such group with that id, they will receive a 404 error code.

Parameters:
group_id – int: Find the group to be updated

db – Session: Get a database session

current_user – User: Get the user that is currently logged in

Returns:
The removed group

async src.routes.groups.update_group(body: GroupUpdate, group_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) → Group
The update_group function updates a group in the database.

Parameters:
body – GroupUpdate: Update the group

group_id – int: Find the group to be deleted

db – Session: Get the database session

current_user – User: Check if the user is an admin or moderator

Returns:
A group object

App Contact’s router Users
async src.routes.user.read_users_me(current_user: User = Depends(get_current_user)) → User
The read_users_me function returns the current user.

Parameters:
current_user – User: Pass the user object to the function

Returns:
The current_user object, which is a user instance

async src.routes.user.update_avatar_user(file: UploadFile = File(PydanticUndefined), current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → User
The update_avatar_user function updates the avatar of a user.

Parameters:
file – UploadFile: Get the file that was uploaded by the user

current_user – User: Get the current user from the database

db – Session: Get the database session

Returns:
A user object

async src.routes.user.update_profile(body: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) → User
The update_profile function updates the user’s profile.

Parameters:
body – UserUpdate: Pass the user information to be updated

current_user – User: Get the user that is currently logged in

db – Session: Pass the database session to the repository

Returns:
A user object

App Contact’s services Auth
class src.services.auth.Auth
Bases: object

ALGORITHM = 'crypt'
SECRET_KEY = 'secret_key'
async create_access_token(data: dict, expires_delta: float | None = None)
The create_access_token function creates a new access token.
Args:
data (dict): A dictionary containing the claims to be encoded in the JWT. expires_delta (Optional[float]): An optional timedelta of seconds for the token’s expiration time.

Parameters:
self – Represent the instance of the class

data – dict: Pass in the data that will be encoded into the jwt

expires_delta – Optional[float]: Set the expiration time of the access token

Returns:
An encoded access token

create_email_token(data: dict)
The create_email_token function takes a dictionary of data and returns a token. The token is created by encoding the data with the SECRET_KEY and ALGORITHM, and adding an iat (issued at) timestamp and exp (expiration) timestamp to it.

Parameters:
self – Represent the instance of the class

data – dict: Pass in the data that will be encoded into a jwt

Returns:
A token

async create_refresh_token(data: dict, expires_delta: float | None = None)
The create_refresh_token function creates a refresh token for the user.
Args:
data (dict): A dictionary containing the user’s id and username. expires_delta (Optional[float]): The number of seconds until the token expires, defaults to None.

Parameters:
self – Represent the instance of the class

data – dict: Pass the user id to the function

expires_delta – Optional[float]: Set the expiry time of the refresh token

Returns:
A refresh token that is encoded using the jwt library

async decode_refresh_token(refresh_token: str)
The decode_refresh_token function is used to decode the refresh token. It takes in a refresh_token as an argument and returns the email of the user who owns that token. If there is no such user, it raises an HTTPException with status code 401 (Unauthorized) and detail &quot;Could not validate credentials&quot;.

Parameters:
self – Represent the instance of the class

refresh_token – str: Pass in the refresh token that was sent from the client

Returns:
The email of the user who is trying to refresh their access token

async get_current_user(token: str = Depends(OAuth2PasswordBearer), db: Session = Depends(get_db))
The get_current_user function is a dependency that will be used in the
protected endpoints. It takes a token as an argument and returns the user if it’s valid, or raises an exception otherwise.

Parameters:
self – Access the class attributes

token – str: Get the token from the authorization header

db – Session: Pass the database session to the function

Returns:
A user object

async get_email_type_from_token(token: str)
The get_email_type_from_token function takes a token as an argument and returns the email address and type of user associated with that token. If the token is invalid, it raises an HTTPException.

Parameters:
self – Represent the instance of the class

token – str: Decode the token

Returns:
A tuple of email and type

get_password_hash(password: str)
The get_password_hash function takes a password as input and returns the hash of that password. The hash is generated using the pwd_context object, which is an instance of Flask-Bcrypt Bcrypt class.

Parameters:
self – Represent the instance of the class

password – str: Pass in the password that is to be hashed

Returns:
A password hash

oauth2_scheme = <fastapi.security.oauth2.OAuth2PasswordBearer object>
pwd_context = <CryptContext>
r = Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>
verify_password(plain_password: str, hashed_password: str)
The verify_password function takes a plain-text password and hashed password as arguments. It then uses the pwd_context object to verify that the plain-text password matches the hashed one.

Parameters:
self – Represent the instance of the class

plain_password – str: Pass in the plain text password that is entered by the user

hashed_password – str: Pass in the hashed password from the database

Returns:
A boolean value of true or false

App Contact’s services Email
async src.services.email.send_email(email: EmailStr, subject: str, template_name: str, username: str, host: str) → None
The send_email function sends an email to the user with a link that they can click on to verify their account.
The function takes in four parameters:
email - the user’s email address, which is used as both the recipient and subject of the message.

subject - a string containing information about what type of verification this is (e.g., verify_email).
This will be used as part of our JWT token for authentication purposes later on when we want to verify whether or not this token was created by us and if it has been tampered with since its

Parameters:
email – EmailStr: Specify the email address of the recipient

subject – str: Set the subject of the email

template_name – str: Specify the template to use when sending the email

username – str: Pass the username to the template

host – str: Pass the hostname of the server to the template

Returns:
None

App Contact’s services Upload Avatar
async src.services.upload_avatar.upload_avatar(file: UploadFile, name: str) → str
The upload_avatar function takes in a file and name, uploads the file to cloudinary, and returns the url of that image. The function is asynchronous because it uses await.

Parameters:
file – UploadFile: Get the file from the request

name – str: Give the image a unique name

Returns:
The url of the uploaded image

Indices and tables
Index

Module Index

Search Page