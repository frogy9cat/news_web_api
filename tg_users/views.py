from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django.utils.timezone import make_aware
from datetime import datetime

from .models import TelegramUsers
from .serializers import TelegramUsersSerializer



class TelegramUsersListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TelegramUsersSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        # Получаем последние три новости, отсортированные по полю created_at
        queryset = TelegramUsers.objects.all().order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


class TelegramUsersFilteredRetriveAPIView(generics.RetrieveAPIView):
    queryset = TelegramUsers.objects.all()
    serializer_class = TelegramUsersSerializer
    permission_classes = (permissions.AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        try:
            # Extract the date range from kwargs
            date_range = kwargs["dates"]
            start_date_str, end_date_str = date_range.split("-")
            
            # Convert the strings to datetime objects
            start_date = datetime.strptime(start_date_str, "%Y%m%d")
            end_date = datetime.strptime(end_date_str, "%Y%m%d")

            # Convert to timezone-aware datetime objects
            start_date_aware = make_aware(datetime.combine(start_date, datetime.min.time()))
            end_date_aware = make_aware(datetime.combine(end_date, datetime.max.time()))

            # Filter by the created_at field within the date range
            result = TelegramUsers.objects.filter(created_at__range = (start_date_aware, end_date_aware))

            if not result.exists():
                return Response({"result": "No TelegramUsers found in the specified date range."})
            
            serialized_result = TelegramUsersSerializer(result, many=True).data
            return Response(data={"result": serialized_result})
        
        except ValueError as ve:
            return Response({"result": "Invalid date format. Use YYYYMMDD-YYYYMMDD."}, status=status.HTTP_400_BAD_REQUEST) 
        
        except Exception as e:
            # Обработка других ошибок
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TelegramUsersRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TelegramUsers.objects.all()
    serializer_class = TelegramUsersSerializer
    permission_classes = (permissions.AllowAny,)

