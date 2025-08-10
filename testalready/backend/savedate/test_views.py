import pytest
import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import SaveDate


class SaveDateAPITest(TestCase):
    """Test cases for SaveDate API endpoints."""

    def setUp(self):
        """Set up test data and client."""
        self.client = APIClient()
        self.url = reverse('savedate-list-create')
        
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

    def test_create_save_date_success(self):
        """Test successful creation of a SaveDate."""
        response = self.client.post(
            self.url,
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('data', response.data)
        self.assertIn('message', response.data)
        
        # Verify the data was saved correctly
        saved_data = response.data['data']
        self.assertEqual(saved_data['title'], self.valid_data['title'])
        self.assertEqual(saved_data['event_subtitle'], self.valid_data['event_subtitle'])
        self.assertEqual(saved_data['event_summary'], self.valid_data['event_summary'])
        self.assertEqual(saved_data['event_times'], self.valid_data['event_times'])
        self.assertEqual(saved_data['event_venue'], self.valid_data['event_venue'])
        self.assertEqual(saved_data['event_address'], self.valid_data['event_address'])
        self.assertEqual(saved_data['event_city'], self.valid_data['event_city'])
        
        # Verify the object was created in database
        self.assertEqual(SaveDate.objects.count(), 1)
        save_date = SaveDate.objects.first()
        self.assertEqual(save_date.title, self.valid_data['title'])

    def test_create_save_date_without_optional_fields(self):
        """Test creating SaveDate without optional fields."""
        minimal_data = {
            "title": "Evento Simples",
            "event_summary": "Descrição válida com mais de 10 caracteres",
            "event_times": [
                {"label": "Evento", "time": "10:00"}
            ],
            "event_venue": "Local do Evento",
            "event_address": "Endereço do Evento",
            "event_city": "Cidade"
        }
        
        response = self.client.post(
            self.url,
            data=json.dumps(minimal_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')

    def test_create_save_date_missing_required_fields(self):
        """Test creating SaveDate with missing required fields."""
        incomplete_data = {
            "title": "Título",
            "event_summary": "Descrição muito curta"  # Too short
        }
        
        response = self.client.post(
            self.url,
            data=json.dumps(incomplete_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_summary', response.data)
        self.assertIn('event_venue', response.data)
        self.assertIn('event_address', response.data)
        self.assertIn('event_city', response.data)
        self.assertIn('event_times', response.data)

    def test_create_save_date_title_too_short(self):
        """Test creating SaveDate with title too short."""
        data = self.valid_data.copy()
        data["title"] = "AB"  # Too short
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_create_save_date_summary_too_short(self):
        """Test creating SaveDate with event_summary too short."""
        data = self.valid_data.copy()
        data["event_summary"] = "Curta"  # Too short
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_summary', response.data)

    def test_create_save_date_venue_too_short(self):
        """Test creating SaveDate with event_venue too short."""
        data = self.valid_data.copy()
        data["event_venue"] = "Lo"  # Too short
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_venue', response.data)

    def test_create_save_date_address_too_short(self):
        """Test creating SaveDate with event_address too short."""
        data = self.valid_data.copy()
        data["event_address"] = "En"  # Too short
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_address', response.data)

    def test_create_save_date_city_too_short(self):
        """Test creating SaveDate with event_city too short."""
        data = self.valid_data.copy()
        data["event_city"] = "A"  # Too short
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_city', response.data)

    def test_create_save_date_empty_event_times(self):
        """Test creating SaveDate with empty event_times."""
        data = self.valid_data.copy()
        data["event_times"] = []
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_times', response.data)

    def test_create_save_date_invalid_event_times_format(self):
        """Test creating SaveDate with invalid event_times format."""
        data = self.valid_data.copy()
        data["event_times"] = [
            {"label": "Cerimônia", "time": "invalid_time"}
        ]
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_times', response.data)

    def test_create_save_date_invalid_time_format(self):
        """Test creating SaveDate with invalid time format."""
        data = self.valid_data.copy()
        data["event_times"] = [
            {"label": "Cerimônia", "time": "2:30 PM"}  # Invalid format
        ]
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_times', response.data)

    def test_list_save_dates_empty(self):
        """Test listing SaveDates when none exist."""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_list_save_dates_with_data(self):
        """Test listing SaveDates when data exists."""
        # Create a SaveDate first
        SaveDate.objects.create(
            title="Test Event",
            event_summary="Test description with more than 10 characters",
            event_times={"test": "data"},
            event_venue="Test Venue",
            event_address="Test Address",
            event_city="Test City"
        )
        
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Event")

    def test_create_save_date_invalid_json(self):
        """Test creating SaveDate with invalid JSON."""
        response = self.client.post(
            self.url,
            data="invalid json",
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_save_date_wrong_content_type(self):
        """Test creating SaveDate with wrong content type."""
        response = self.client.post(
            self.url,
            data=self.valid_data,
            content_type='text/plain'
        )
        
        # Django REST Framework should handle this gracefully
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE])

    def test_create_save_date_malformed_event_times(self):
        """Test creating SaveDate with malformed event_times."""
        data = self.valid_data.copy()
        data["event_times"] = "not a list"  # Should be a list
        
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('event_times', response.data)
