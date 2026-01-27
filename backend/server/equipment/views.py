# Create your views here.
import os
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.conf import settings

from .models import EquipmentDataset
from data_logic.analyzer import analyze_csv


@api_view(['GET','POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_csv(request):
    if request.method == 'GET':
        return Response({"message": "Use POST to upload a CSV file"})
    """
    API to upload CSV, analyze it, store summary, and return result.
    """

    if 'file' not in request.FILES:
        return Response({"status": "error", "message": "No file provided"}, status=400)

    csv_file = request.FILES['file']

    # Save file temporarily
    upload_dir = os.path.join(settings.BASE_DIR, "uploads")
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, csv_file.name)

    with open(file_path, 'wb+') as destination:
        for chunk in csv_file.chunks():
            destination.write(chunk)

    # Analyze CSV
    result = analyze_csv(file_path)

    if result.get("status") == "error":
        return Response(result, status=400)

    # Store in database
    dataset = EquipmentDataset.objects.create(
        file_name=csv_file.name,
        total_equipment=result["total_equipment"],
        avg_flowrate=result["avg_flowrate"],
        avg_pressure=result["avg_pressure"],
        avg_temperature=result["avg_temperature"]
    )

    # Keep only latest 5 records
    all_records = EquipmentDataset.objects.order_by('-uploaded_at')
    if all_records.count() > 5:
        for old in all_records[5:]:
            old.delete()


    return Response(result)

@api_view(['GET'])
def history(request):
    datasets = EquipmentDataset.objects.order_by('-uploaded_at')[:5]

    data = []
    for d in datasets:
        data.append({
            "file_name": d.file_name,
            "uploaded_at": d.uploaded_at,
            "total_equipment": d.total_equipment,
            "avg_flowrate": d.avg_flowrate,
            "avg_pressure": d.avg_pressure,
            "avg_temperature": d.avg_temperature
        })

    return Response({
        "status": "success",
        "count": len(data),
        "history": data
    })

