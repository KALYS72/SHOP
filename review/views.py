from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Rate
from .permissions import IsAuthorOrReadOnly

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CreateRating(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        user = request.user
        ser = RatingSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        product_id = request.data.get('product')
        if Rate.objects.filter(author=user, product__id=product_id).exists():
            rating = Rate.objects.get(author=user, product__id=product_id)
            rating.value = request.data.get('value')
            rating.save()
        else:
            ser.save()
        return Response(status=201)