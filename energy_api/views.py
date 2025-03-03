from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
import random

class EnergyDataView(APIView):
    def get(self, request):
        #  dummy data
        dummy_data = [
            {
                "timestamp": "2025-03-01T00:00:00Z",
                "energyForm": "electricity",
                "systemType": "building A",
                "consumption": 1500,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-03-01T01:00:00Z",
                "energyForm": "electricity",
                "systemType": "building A",
                "consumption": 1600,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-02-28T00:00:00Z",
                "energyForm": "electricity",
                "systemType": "building B",
                "consumption": 1000,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-02-28T01:00:00Z",
                "energyForm": "electricity",
                "systemType": "building B",
                "consumption": 1100,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-03-01T00:00:00Z",
                "energyForm": "electricity",
                "systemType": "store A",
                "consumption": 800,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-02-28T01:00:00Z",
                "energyForm": "electricity",
                "systemType": "store B",
                "consumption": 900,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-03-02T00:00:00Z",
                "energyForm": "electricity",
                "systemType": "production warehouse A",
                "consumption": 2000,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-02-27T01:00:00Z",
                "energyForm": "electricity",
                "systemType": "production warehouse B",
                "consumption": 2200,
                "unit": "kWh"
            },
            # Heat data
            {
                "timestamp": "2025-03-01T00:00:00Z",
                "energyForm": "heat",
                "systemType": "building A",
                "consumption": 500,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-02-28T01:00:00Z",
                "energyForm": "heat",
                "systemType": "building A",
                "consumption": 550,
                "unit": "kWh"
            },
            # Cold data
            {
                "timestamp": "2025-03-01T00:00:00Z",
                "energyForm": "cold",
                "systemType": "store A",
                "consumption": 300,
                "unit": "kWh"
            },
            {
                "timestamp": "2025-02-28T01:00:00Z",
                "energyForm": "cold",
                "systemType": "store A",
                "consumption": 350,
                "unit": "kWh"
            },
            # Gas data
            {
                "timestamp": "2025-03-01T00:00:00Z",
                "energyForm": "gas",
                "systemType": "building A",
                "consumption": 200,
                "unit": "m³"
            },
            {
                "timestamp": "2025-02-28T01:00:00Z",
                "energyForm": "gas",
                "systemType": "building B",
                "consumption": 250,
                "unit": "m³"
            },
            # Water data
            {
                "timestamp": "2025-03-01T00:00:00Z",
                "energyForm": "water",
                "systemType": "building A",
                "consumption": 100,
                "unit": "m³"
            },
            {
                "timestamp": "2025-02-28T01:00:00Z",
                "energyForm": "water",
                "systemType": "building B",
                "consumption": 120,
                "unit": "m³"
            }
        ]
        return Response(dummy_data)