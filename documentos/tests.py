
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Documentos
from .serializers import SongsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def criar_documento(CPFOUCNPJ="", NOME="" , CELULAR ="" ,  RESULTADOCONSULTAS ="    "):
        if CPFOUCNPJ != "" and CELULAR != "":
            Documentos.objects.create(CPFOUCNPJ=CPFOUCNPJ, NOME=NOME, CELULAR = CELULAR , RESULTADOCONSULTAS =  RESULTADOCONSULTAS)

    def setUp(self):
        # add test data
        self.criar_documento("like glue", "sean paul")
        self.criar_documento("simple song", "konshens")
        self.criar_documento("love is wicked", "brick and lace")
        self.criar_documento("jam rock", "damien marley")


class GetAllDocumentosTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("documentos-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Documentos.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
