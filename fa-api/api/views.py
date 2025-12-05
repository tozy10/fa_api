import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .detect import model
from .models import trapImage
from django.conf import settings

@csrf_exempt
def imageUploadView(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    if "image" not in request.FILES:
        return JsonResponse({"error": "No image file provided"}, status=400)

    # Save uploaded image
    image_file = request.FILES["image"]
    file_path = default_storage.save(image_file.name, image_file)
    print(file_path)
    # Run YOLO detection
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    results = model(full_path)
    

    # Count worms
    boxes = results[0].boxes
    count = len(boxes)

    # Format bounding boxes
    detections = []
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        detections.append({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "confidence": conf,
        })
    trapImage.objects.create(
    image=file_path,
    count=count
)

    return JsonResponse({
        "count": count,
        "detections": detections,
        "image_path": file_path
    })
    
