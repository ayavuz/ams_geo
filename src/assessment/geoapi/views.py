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
        # TODO geo locaties obv eigen user, andere endpoint? of gewoon filter. Misschien checken voor geen anon? Anders wordt alle locaties
        # van alle anon gebruikers opgehaald
        # gebruik geolocation query param in url?


        user_filter = request.query_params.get('user')

        # TODO als je in url user=me hebt filteren?
        if(user_filter=='me'):
            print('ONLY USER LOCATIONS')
            # Anon heeft geen user id dus alle locaties met als user none wordt opgehaald
            # TODO als er tijd over is verbeter dit?
            locations = GeoLocation.objects.filter(user=request.user.id)
        else:
            print('ALL LOCATIONS')
            locations = GeoLocation.objects.all()


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

