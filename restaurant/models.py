from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} {self.surname} ({self.position})"


class Menu(models.Model):
    date_upload = models.DateField(auto_now_add=True)
    description = models.TextField()
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu",
    )
    voters = models.ManyToManyField(Employee, blank=True)

    class Meta:
        ordering = ("-date_upload",)
        unique_together = (("date_upload", "restaurant"),)

    def __str__(self) -> str:
        return f"{self.restaurant.name} - {self.date_upload}"
