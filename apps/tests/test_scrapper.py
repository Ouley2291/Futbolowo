from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.files.base import ContentFile

from apps.web_scrapping.main_scrapper import scrape_laczynaspilka

class ParameterValidationTests(TestCase):
    """Tests for parameter validation"""
    
    def test_ekstraklasa_missing_runda_raises_error(self):
        """Should raise ValueError when runda is missing for Ekstraklasa"""
        with self.assertRaises(ValueError) as context:
            scrape_laczynaspilka(
                liga="Ekstraklasa",
                runda=None,
                kolejka="33 (bieżąca)"
            )
        self.assertIn("runda, kolejka", str(context.exception))
    
    def test_ekstraklasa_missing_kolejka_raises_error(self):
        """Should raise ValueError when kolejka is missing for Ekstraklasa"""
        with self.assertRaises(ValueError) as context:
            scrape_laczynaspilka(
                liga="Ekstraklasa",
                runda="Wiosenna",
                kolejka=None
            )
    
    def test_nizsze_ligi_missing_wojewodztwo_raises_error(self):
        """Should raise ValueError when wojewodztwo is missing for Niższe ligi"""
        with self.assertRaises(ValueError) as context:
            scrape_laczynaspilka(
                liga="Niższe ligi",
                wojewodztwo=None,
                klasa="Klasa B",
                grupa="Wałbrzych: Klasa B"
            )
    
    def test_nizsze_ligi_missing_klasa_raises_error(self):
        """Should raise ValueError when klasa is missing for Niższe ligi"""
        with self.assertRaises(ValueError) as context:
            scrape_laczynaspilka(
                liga="Niższe ligi",
                wojewodztwo="dolnośląskie",
                klasa=None,
                grupa="Wałbrzych: Klasa B"
            )
    
    def test_nizsze_ligi_missing_grupa_raises_error(self):
        """Should raise ValueError when grupa is missing for Niższe ligi"""
        with self.assertRaises(ValueError) as context:
            scrape_laczynaspilka(
                liga="Niższe ligi",
                wojewodztwo="dolnośląskie",
                klasa="Klasa B",
                grupa=None
            )
