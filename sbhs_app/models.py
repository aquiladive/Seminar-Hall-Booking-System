from django.db import models

class user(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class adminUser(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


#events that admin / placement cell approves to be added to calendar
class approvedEvent(models.Model):
    hall_choices = (
        ("Ramegowda", "Ramegowda Seminar Hall"),
        ("Training", "Training Hall"),
    )

    time_choices = (
        ("9AM-1PM", "9 AM - 1 PM"),
        ("1PM-5PM", "1 PM - 5 PM"),
    )

    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=time_choices, default=time_choices[0])
    description = models.CharField(max_length=300)
    hall = models.CharField(max_length=10, choices=hall_choices, default=hall_choices[0])
    dept = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
    

#events that the dept HOD is trying to book
class event(models.Model):
    hall_choices = (
        ("Ramegowda", "Ramegowda Seminar Hall"),
        ("Training", "Training Hall"),
    )

    time_choices = (
        ("9AM-1PM", "9 AM - 1 PM"),
        ("1PM-5PM", "1 PM - 5 PM"),
    )

    approve_choices = (
        ("False", "False"),
        ("True", "True")
    )

    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=time_choices, default=time_choices[0])
    description = models.CharField(max_length=300)
    hall = models.CharField(max_length=10, choices=hall_choices, default=hall_choices[0])
    dept = models.CharField(max_length=10)
    approval = models.CharField(max_length=5, choices=approve_choices, default=approve_choices[0])

    def __unicode__(self):
        return self.name
