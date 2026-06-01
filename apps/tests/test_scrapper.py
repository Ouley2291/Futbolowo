import json
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.files.base import ContentFile

from apps.web_scrapping.main_scrapper import scrape_laczynaspilka

class ParameterValidationTests(TestCase):
    """Tests for parameter validation"""
    
    def test_nizsze_ligi_missing_all_parameters(self):
        """Should raise ValueError with missing parameters"""
        with self.assertRaises(ValueError) as context:
            scrape_laczynaspilka(
                liga=None,
                wojewodztwo=None,
                klasa=None,
                grupa=None
            )
