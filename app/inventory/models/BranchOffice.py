from django.db import models


class BranchOffice(models.Model):
    name = models.CharField('Name Branch Office', max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField('Registration date', auto_now_add=True)

    class Meta:
        db_table = 'branchOffice'
        verbose_name = 'BranchOffice'
        verbose_name_plural = 'BranchOffices'

    def __str__(self):
        return self.name
