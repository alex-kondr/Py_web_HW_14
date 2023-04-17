from pathlib import Path

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr

from src.services.auth import auth_service
from src.conf.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_FROM_NAME="Contacts service...",
    MAIL_STARTTLS=True, 
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / "templates"
)


async def send_email(email: EmailStr, subject: str, template_name: str, username: str, host: str) -> None:
    """
    The send_email function sends an email to the user with a link that they can click on to verify their account.
        The function takes in four parameters:
            1) email - the user's email address, which is used as both the recipient and subject of the message.
            2) subject - a string containing information about what type of verification this is (e.g., verify_email).
                This will be used as part of our JWT token for authentication purposes later on when we want to verify
                whether this token was created by us and if it has been tampered with since its

    :param email: EmailStr: Specify the email address of the recipient
    :param subject: str: Set the subject of the email
    :param template_name: str: Specify the template to use when sending the email
    :param username: str: Pass the username to the template
    :param host: str: Pass the hostname of the server to the template
    :return: None
    """
    try:
        token_verification = auth_service.create_email_token({"sub": email, "type": subject})
        message = MessageSchema(
            subject=subject,
            recipients=[email],
            template_body={"host": host,
                           "username": username,
                           "token": token_verification},
            subtype=MessageType.html
        )
        
        fm = FastMail(conf)
        await fm.send_message(message, template_name=template_name)
    except ConnectionErrors as err:
        print(err)
