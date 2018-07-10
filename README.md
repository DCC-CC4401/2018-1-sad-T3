# Tarea 3: SAD Development 2018-1 CC4401 Ingeniería de Software

Proyecto Git para la _Tarea 3_ del grupo 5 **__SAD Development__**.

Instrucciones para ejecutar el proyecto:

1. Activar el entorno virtual (o crear uno en caso de no existir)

2. Instalar las dependencias usando: `pip install -r requirements.txt`

3. Si es la primera vez que se ejecuta el proyecto, realizar las migraciones correspondientes utilizando `python manage.py migrate`

4. Ejecutar usando `python manage.py runserver`
     
*Nota: Para servir los archivos estáticos, debe mantenerse activo el modo de desarrollo, es decir, no modificar la variable debug en **settings.py**.*


### Nota acerca del admin de Django:

Para utilizar el administrador de *Django* para crear modelos, no basta con un *superuser*, hay que modificar el campo *is_staff*. Esto puede hacerse como sigue:
+ En la carpeta del proyecto, ejecutar `python manage.py createsuperuser`

+ Asumiendo que se creó con el correo admin@cei.cl, ejecutar `python manage.py shell` y luego en Python los siguientes comandos:

~~~~python
from mainApp.models import User
u = User.objects.get(email='admin@cei.cl')
u.is_staff = True
u.save()
~~~~
