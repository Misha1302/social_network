import os
import uuid

from werkzeug.datastructures import FileStorage


class ImagesService:
    IMAGES_DIRECTORY = './files/images'

    def add_image(self, img: FileStorage) -> uuid.UUID:
        msg_id = uuid.uuid4()
        img.seek(0)
        img.save(os.path.join(self.IMAGES_DIRECTORY, str(msg_id) + '.jpg'))
        return msg_id
