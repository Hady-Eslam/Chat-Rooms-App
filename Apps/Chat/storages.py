from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.apps import apps
import os


class LocalStorage(FileSystemStorage):

    def __init__(self) -> None:
        super().__init__(os.path.join(apps.get_app_config('Chat').path, 'media'))
    

class ProductionStorage(LocalStorage):

    def save(self, name, content, max_length=None):
        return 'rooms/defaultCover.jpg'



def default_storage():
    return ProductionStorage() if settings.PRODUCTION else LocalStorage()
