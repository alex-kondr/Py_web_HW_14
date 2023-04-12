from fastapi import UploadFile
import cloudinary
import cloudinary.uploader
import cloudinary.api

from src.conf.config import settings


async def upload_avatar(file: UploadFile, name: str) -> str:
    """
    The upload_avatar function takes in a file and name, uploads the file to cloudinary,
    and returns the url of that image. The function is asynchronous because it uses await.

    :param file: UploadFile: Get the file from the request
    :param name: str: Give the image a unique name
    :return: The url of the uploaded image
    """
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )

    await cloudinary.uploader.upload(file.file, public_id=f"ContactsApp/{name}", overwrite=True,
                                     eager=[{"width": 250, "height": 250, "crop": "fill"}])
    image_info = await cloudinary.api.resource(f"ContactsApp/{name}")
    src_url = image_info["derived"][0]["secure_url"]
    return src_url
