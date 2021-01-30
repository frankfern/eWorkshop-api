from rest_framework.response import Response
from rest_framework import status


def handle_serializers(serializer_class, data, instance=None):
    """This function performs the logic of handling serializers in views"""

    serializer = serializer_class(data=data, instance=instance)
    serializer.is_valid(raise_exception=True)
    serializer.save()


def fresponse(message='Succesful operation'):
    """Returns a success response. Only takes a message as argument"""

    return Response(data={'status': 'success',
                          'code': status.HTTP_200_OK,
                          'message': message
                          }, status=status.HTTP_200_OK)
