from rest_framework.views import APIView
from rest_framework.response import Response
from .models import trapImage

from .detect import count_worms

class imageUploadview(APIView):
    def post(self, request):
        file = request.FILES.get("image")
        
        if file is None:
            return Response({"error": "No image provided"}, status=400)
        img_obj = trapImage.objects.create(image= file)
        
        worm_count = count_worms(img_obj.image.path)
        img_obj.worm_count = worm_count
        img_obj.save()
        
        return Response({
             "message": "Image received",
            "worm_count": worm_count,
            "timestamp": img_obj.timestamp,
            "image_url": img_obj.image.url
        }, status=201)