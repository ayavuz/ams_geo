from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import GeoLocation
from.serializers import GeoLocationSerializer


class GeoLocationView(APIView):
    """
    GET en POST van GEO location
    """

    def get_queryset(self):
        return GeoLocation.objects.all()

    def get(self, request):
        # Geo locaties obv eigen user, andere endpoint? of gewoon filter. Misschien checken voor geen anon? 
        # Anders worden alle locaties van alle anon gebruikers opgehaald. Gebruik query param.


        user_filter = request.query_params.get('user')

        if(user_filter=='me'):
            # Anon heeft geen user id dus alle locaties met als user none wordt opgehaald
            # TODO als er tijd over is verbeter dit?
            locations = GeoLocation.objects.filter(user=request.user.id)
        else:
            locations = GeoLocation.objects.all()


        # TODO filter afstand
        distance = request.query_params.get('distance')
        if distance:
            pass


        serializer = GeoLocationSerializer(locations, many=True)


        return Response(serializer.data)
    


    def post(self, request):
        print('request data', request.data)

        # TODO get lat - long data from request as JSON? And then create the Point object and assign to geolocation

        serializer = GeoLocationSerializer(data=request.data)
        if serializer.is_valid():
            # TODO later user=request.user?
            serializer.save()

        print('BLABLABLALB')

        return Response(serializer.data, status=status.HTTP_201_CREATED)

