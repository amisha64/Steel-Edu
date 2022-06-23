from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.linear_model import LinearRegression

import joblib

# Create your models here.
COUNTRYNAME = (
    (1, 'India'),
)

CATEGORIES = (
    (1, 'Non-Alloy Finished Steel'),
)

STATES = (
    (1, 'Jammu and Kashmir'),
    (2, 'Andhra Pradesh'),
    (3, 'Arunachal Pradesh'),
    (4, 'Assam'),
    (5, 'Bihar'),
    (6, 'Chhattisgarh'),
    (7, 'Goa'),
    (8, 'Gujarat'),
    (9, 'Haryana'),
    (10, 'Himachal Pradesh'),
    (11, 'Jharkhand'),
    (12, 'Karnataka'),
    (13, 'Kerala'),
    (14, 'Madhya Pradesh'),
    (15, 'Maharashtra'),
    (16, 'Manipur'),
    (17, 'Meghalaya'),
    (18, 'Mizoram'),
    (19, 'Nagaland'),
    (20, 'Odisha'),
    (21, 'Punjab'),
    (22, 'Rajasthan'),
    (23, 'Sikkim'),
    (24, 'Tamil Nadu'),
    (25, 'Telangana'),
    (26, 'Tripura'),
    (27, 'Uttar Pradesh'),
    (28, 'Uttarakhand'),
    (29, 'West Bengal'),
    (30, 'Chandigarh'),
    (31, 'Delhi'),
)

STEELTYPE = (
    (0, 'Bars and Rods'),
    (1, 'Stainless Steel'),
    (2, 'HR Coil'),
    (3, 'Galvanized Iron Coil'),
)
class Data(models.Model):
    country = models.PositiveIntegerField(choices=COUNTRYNAME, null=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2017), MaxValueValidator(2026)], null = True)
    category = models.PositiveIntegerField(choices=CATEGORIES, null=True)
    state = models.PositiveIntegerField(choices=STATES, null=True)
    type = models.PositiveIntegerField(choices=STEELTYPE, null=True)
    consumption = models.FloatField(null= True, blank = True)
    date = models.DateTimeField(auto_now_add=True)

    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/mllrmodel (2).joblib')
        self.consumption = ml_model.predict([[self.country, self.year, self.category, self.state, self.type]])
        return super().save(*args, *kwargs)

    class Meta:
       ordering = ['-date']
    
    