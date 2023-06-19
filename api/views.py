from django.views import View
from .models import Prueba
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
class PruebaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id)>0:
            pruebas = list(Prueba.objects.filter(id_prueba = id).values())
            if len(pruebas)>0:
                prueba = pruebas[0]
                datos = {'message': "OK", 'data':prueba}
            else:
                datos = {'message': "Prueba no encontrada"}
            return JsonResponse(datos)
        else:
            pruebas = list(Prueba.objects.values())
            if len(pruebas)>0:
                datos = {'message': "OK", 'data':pruebas}
            else:
                datos = {'message': "Pruebas no encontradas"}
            return JsonResponse(datos)
    
    def post(self, request):
        jsonData = json.loads(request.body)
        Prueba.objects.create(
            edad = jsonData['edad'],
            fecha = jsonData['fecha'],
            descripcion = jsonData['descripcion'],
            total = jsonData['total']
        )
        datos = {'message': "Prueba creado con exito"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsonData = json.loads(request.body)
        pruebas = list(Prueba.objects.filter(id_prueba = id).values())
        if len(pruebas)>0:
            prueba = Prueba.objects.get(id_prueba = id)
            prueba.edad = jsonData['edad']
            prueba.fecha = jsonData['fecha']
            prueba.descripcion = jsonData['descripcion']
            prueba.total = jsonData['total']
            prueba.save()
            datos = {'message': "Prueba actualizada con exito"}
        else:
            datos = {'message': "Prueba no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        pruebas = list(Prueba.objects.filter(id_prueba = id).values())
        if len(pruebas)>0:
            Prueba.objects.filter(id_prueba = id).delete()
            datos = {'message': "Prueba eliminada con exito"}
        else:
            datos = {'message': "Prueba no encontrada"}
        return JsonResponse(datos)
