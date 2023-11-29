from django.db import models

#git remote set-url origin git@github.com:angmunpri/decide-angmunpri.git

class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id', 'voter_id'),)
