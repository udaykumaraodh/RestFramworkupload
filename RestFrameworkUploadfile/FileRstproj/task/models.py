from django.db import models
from django.contrib.auth import get_user_model

from django.core.validators import FileExtensionValidator
from .validation import validate_img,validate_xls



# Create your models here.

class UserFile(models.Model):
    User=get_user_model()

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='docs/photos/',validators=(validate_img,))
    xlsdoc=models.FileField(upload_to='docs/xldoc/',validators=(validate_xls,))
    idproof=models.FileField(upload_to='docs/proofs/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])






class SingleUser(models.Model):
    User=get_user_model()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    docfiles=models.FileField(upload_to='singledocs/multifiles/')






