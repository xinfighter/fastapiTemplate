from tortoise import models, fields

from app.utils import crypt


class User(models.Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=100, null=False, encrypt=True)
    age = fields.SmallIntField(default=0, null=False)
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

    def verify_password(self, password):
        """
        密码校验
        :param password:
        :return: True(校验通过)/False(校验失败)
        """
        return crypt.verify(password, self.password)
