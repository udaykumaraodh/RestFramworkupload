import os
from django.core.exceptions import ValidationError

def validate_img(value):
    ext=os.path.splitext(value.name)[1]
    valid_ext=['.jpg','.JPG','.JPEG','.jpeg']
    if not ext.lower() in valid_ext:
        raise ValidationError('please choose image format only')



def validate_xls(value):
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.xlsx','.xls']
    if not ext.lower() in valid_ext:
        raise ValidationError('xls format only')

