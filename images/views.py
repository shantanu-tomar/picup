from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser

from .serializers import ImageSerializer


class ImageUpoadView(CreateAPIView):
    parser_class = (FileUploadParser,)
    serializer_class = ImageSerializer
