import pytest
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from .serializers import SaveDateWriteSerializer, SaveDateReadSerializer, EventTimeSerializer
from .models import SaveDate


class EventTimeSerializerTest(TestCase):
    """Test cases for EventTimeSerializer."""

    def test_valid_event_time(self):
        """Test valid event time data."""
        data = {"label": "Cerimônia", "time": "14:00"}
        serializer = EventTimeSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_time_format(self):
        """Test invalid time format."""
        data = {"label": "Cerimônia", "time": "2:30 PM"}  # Invalid format
        serializer = EventTimeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("time", serializer.errors)

    def test_empty_label(self):
        """Test empty label validation."""
        data = {"label": "", "time": "14:00"}
        serializer = EventTimeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("label", serializer.errors)

    def test_missing_label(self):
        """Test missing label field."""
        data = {"time": "14:00"}
        serializer = EventTimeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("label", serializer.errors)

    def test_missing_time(self):
        """Test missing time field."""
        data = {"label": "Cerimônia"}
        serializer = EventTimeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("time", serializer.errors)

    def test_invalid_hour_format(self):
        """Test invalid hour format."""
        data = {"label": "Cerimônia", "time": "25:00"}  # Invalid hour
        serializer = EventTimeSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_minute_format(self):
        """Test invalid minute format."""
        data = {"label": "Cerimônia", "time": "14:60"}  # Invalid minute
        serializer = EventTimeSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class SaveDateWriteSerializerTest(TestCase):
    """Test cases for SaveDateWriteSerializer."""

    def setUp(self):
        """Set up test data."""
        self.valid_data = {
            "title": "Casamento João e Maria",
            "event_subtitle": "Uma celebração de amor",
            "event_summary": "Venha celebrar conosco este momento especial",
            "event_times": [
                {"label": "Cerimônia", "time": "14:00"},
                {"label": "Cocktail", "time": "15:30"}
            ],
            "event_venue": "Salão de Festas",
            "event_address": "Rua das Flores, 123",
            "event_city": "São Paulo"
        }

    def test_valid_data(self):
        """Test serializer with valid data."""
        serializer = SaveDateWriteSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_missing_required_fields(self):
        """Test serializer with missing required fields."""
        incomplete_data = {
            "title": "Título",
            "event_summary": "Descrição muito curta"  # Too short
        }
        serializer = SaveDateWriteSerializer(data=incomplete_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_summary", serializer.errors)
        self.assertIn("event_venue", serializer.errors)
        self.assertIn("event_address", serializer.errors)
        self.assertIn("event_city", serializer.errors)

    def test_title_too_short(self):
        """Test title validation (minimum 3 characters)."""
        data = self.valid_data.copy()
        data["title"] = "AB"  # Too short
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_event_summary_too_short(self):
        """Test event_summary validation (minimum 10 characters)."""
        data = self.valid_data.copy()
        data["event_summary"] = "Curta"  # Too short
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_summary", serializer.errors)

    def test_event_venue_too_short(self):
        """Test event_venue validation (minimum 3 characters)."""
        data = self.valid_data.copy()
        data["event_venue"] = "Lo"  # Too short
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_venue", serializer.errors)

    def test_event_address_too_short(self):
        """Test event_address validation (minimum 3 characters)."""
        data = self.valid_data.copy()
        data["event_address"] = "En"  # Too short
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_address", serializer.errors)

    def test_event_city_too_short(self):
        """Test event_city validation (minimum 2 characters)."""
        data = self.valid_data.copy()
        data["event_city"] = "A"  # Too short
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_city", serializer.errors)

    def test_empty_event_times(self):
        """Test that event_times cannot be empty."""
        data = self.valid_data.copy()
        data["event_times"] = []
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_times", serializer.errors)

    def test_invalid_event_times_format(self):
        """Test invalid event_times format."""
        data = self.valid_data.copy()
        data["event_times"] = [
            {"label": "Cerimônia", "time": "invalid_time"}
        ]
        serializer = SaveDateWriteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("event_times", serializer.errors)

    def test_optional_fields_omitted(self):
        """Test that optional fields can be omitted."""
        data = {
            "title": "Evento Simples",
            "event_summary": "Descrição válida com mais de 10 caracteres",
            "event_times": [
                {"label": "Evento", "time": "10:00"}
            ],
            "event_venue": "Local",
            "event_address": "Endereço",
            "event_city": "Cidade"
        }
        serializer = SaveDateWriteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_excluded_fields_not_included(self):
        """Test that excluded fields are not included in the serializer."""
        serializer = SaveDateWriteSerializer()
        self.assertNotIn("id", serializer.fields)
        self.assertNotIn("created_at", serializer.fields)
        self.assertNotIn("updated_at", serializer.fields)


class SaveDateReadSerializerTest(TestCase):
    """Test cases for SaveDateReadSerializer."""

    def setUp(self):
        """Set up test data."""
        self.save_date = SaveDate.objects.create(
            title="Test Event",
            event_subtitle="Test Subtitle",
            event_summary="Test description with more than 10 characters",
            event_times={"test": "data"},
            event_venue="Test Venue",
            event_address="Test Address",
            event_city="Test City"
        )

    def test_read_serializer_includes_all_fields(self):
        """Test that read serializer includes all fields."""
        serializer = SaveDateReadSerializer(self.save_date)
        data = serializer.data
        
        self.assertIn("id", data)
        self.assertIn("title", data)
        self.assertIn("event_subtitle", data)
        self.assertIn("event_summary", data)
        self.assertIn("event_times", data)
        self.assertIn("event_venue", data)
        self.assertIn("event_address", data)
        self.assertIn("event_city", data)
        self.assertIn("created_at", data)
        self.assertIn("updated_at", data)

    def test_read_serializer_data_matches_model(self):
        """Test that serializer data matches model data."""
        serializer = SaveDateReadSerializer(self.save_date)
        data = serializer.data
        
        self.assertEqual(data["title"], self.save_date.title)
        self.assertEqual(data["event_subtitle"], self.save_date.event_subtitle)
        self.assertEqual(data["event_summary"], self.save_date.event_summary)
        self.assertEqual(data["event_venue"], self.save_date.event_venue)
        self.assertEqual(data["event_address"], self.save_date.event_address)
        self.assertEqual(data["event_city"], self.save_date.event_city)
