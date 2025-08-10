import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import SaveDate


class SaveDateModelTest(TestCase):
    """Test cases for the SaveDate model."""

    def setUp(self):
        """Set up test data."""
        self.valid_event_times = [
            {"label": "Cerimônia", "time": "14:00"},
            {"label": "Cocktail", "time": "15:30"}
        ]

    def test_create_save_date_with_valid_data(self):
        """Test creating a SaveDate with valid data."""
        save_date = SaveDate.objects.create(
            title="Casamento João e Maria",
            event_subtitle="Uma celebração de amor",
            event_summary="Venha celebrar conosco este momento especial",
            event_times=self.valid_event_times,
            event_venue="Salão de Festas",
            event_address="Rua das Flores, 123",
            event_city="São Paulo"
        )
        
        self.assertEqual(save_date.title, "Casamento João e Maria")
        self.assertEqual(save_date.event_subtitle, "Uma celebração de amor")
        self.assertEqual(save_date.event_summary, "Venha celebrar conosco este momento especial")
        self.assertEqual(save_date.event_times, self.valid_event_times)
        self.assertEqual(save_date.event_venue, "Salão de Festas")
        self.assertEqual(save_date.event_address, "Rua das Flores, 123")
        self.assertEqual(save_date.event_city, "São Paulo")
        self.assertIsNotNone(save_date.id)
        self.assertIsNotNone(save_date.created_at)
        self.assertIsNotNone(save_date.updated_at)

    def test_create_save_date_without_optional_fields(self):
        """Test creating a SaveDate without optional fields."""
        save_date = SaveDate.objects.create(
            title="Evento Simples",
            event_summary="Descrição mínima do evento",
            event_venue="Local do Evento",
            event_address="Endereço do Evento",
            event_city="Cidade"
        )
        
        self.assertEqual(save_date.title, "Evento Simples")
        self.assertIsNone(save_date.event_subtitle)
        self.assertEqual(save_date.event_times, {})
        self.assertIsNotNone(save_date.id)

    def test_title_min_length_validation(self):
        """Test that title must have at least 3 characters."""
        with self.assertRaises(ValidationError):
            save_date = SaveDate(
                title="AB",  # Too short
                event_summary="Descrição válida",
                event_venue="Local",
                event_address="Endereço",
                event_city="Cidade"
            )
            save_date.full_clean()

    def test_event_summary_min_length_validation(self):
        """Test that event_summary must have at least 10 characters."""
        with self.assertRaises(ValidationError):
            save_date = SaveDate(
                title="Título Válido",
                event_summary="Curta",  # Too short
                event_venue="Local",
                event_address="Endereço",
                event_city="Cidade"
            )
            save_date.full_clean()

    def test_event_venue_min_length_validation(self):
        """Test that event_venue must have at least 3 characters."""
        with self.assertRaises(ValidationError):
            save_date = SaveDate(
                title="Título Válido",
                event_summary="Descrição válida com mais de 10 caracteres",
                event_venue="Lo",  # Too short
                event_address="Endereço",
                event_city="Cidade"
            )
            save_date.full_clean()

    def test_event_address_min_length_validation(self):
        """Test that event_address must have at least 3 characters."""
        with self.assertRaises(ValidationError):
            save_date = SaveDate(
                title="Título Válido",
                event_summary="Descrição válida com mais de 10 caracteres",
                event_venue="Local",
                event_address="En",  # Too short
                event_city="Cidade"
            )
            save_date.full_clean()

    def test_event_city_min_length_validation(self):
        """Test that event_city must have at least 2 characters."""
        with self.assertRaises(ValidationError):
            save_date = SaveDate(
                title="Título Válido",
                event_summary="Descrição válida com mais de 10 caracteres",
                event_venue="Local",
                event_address="Endereço",
                event_city="A"  # Too short
            )
            save_date.full_clean()

    def test_string_representation(self):
        """Test the string representation of SaveDate."""
        save_date = SaveDate.objects.create(
            title="Test Event",
            event_summary="Test description",
            event_venue="Test Venue",
            event_address="Test Address",
            event_city="Test City"
        )
        
        # Note: The __str__ method references event_date which was removed
        # This test will fail until the __str__ method is fixed
        self.assertIn("Test Event", str(save_date))

    def test_auto_timestamps(self):
        """Test that created_at and updated_at are automatically set."""
        save_date = SaveDate.objects.create(
            title="Timestamp Test",
            event_summary="Testing automatic timestamps",
            event_venue="Test Venue",
            event_address="Test Address",
            event_city="Test City"
        )
        
        self.assertIsNotNone(save_date.created_at)
        self.assertIsNotNone(save_date.updated_at)
        self.assertEqual(save_date.created_at, save_date.updated_at)

    def test_update_timestamp(self):
        """Test that updated_at changes when the object is updated."""
        save_date = SaveDate.objects.create(
            title="Update Test",
            event_summary="Testing update timestamps",
            event_venue="Test Venue",
            event_address="Test Address",
            event_city="Test City"
        )
        
        original_updated_at = save_date.updated_at
        save_date.title = "Updated Title"
        save_date.save()
        
        self.assertNotEqual(original_updated_at, save_date.updated_at)
