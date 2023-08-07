#Tercera Pre-Entrega Lambezat

Autor: Lucas Lambezat
Nombre: Tercera Pre-Entrega - Lambezat L.

*NOTA: LUEGO DE HABER CARGADO LA 3º ENTREGA EN ESTE REPOSITORIO, SE QUISO SUBIR UNA NUEVA VERSIÓN ELIMINANDO LA PREVIA, LO QUE RESULTÓ
EN EL BORRADO DE LA VERSIÓN LOCAL DEL PROYECTO, Y LA VERSIÓN DEL REPOSITORIO. ES POR ESTE MOTIVO QUE EL CRUD SE ENCUENTRA REALIZADO CON
VISTAS BASADAS EN CLASE EN LUGAR DE BASADAS EN FUNCIONES COMO ERA LA VERSION ORIGINAL, YA QUE ESTA ES UNA VERSIÓN QUE CORRESPONDE A LO
QUE SE PRETENDE ENTREGAR EN EL PROYECTO FINAL. EN SÍNTESIS: SE PERDIÓ LA VERSIÓN SUBIDA DE LA TERCERA PRE ENTREGA.

OBJETIVO DEL TP PRESENTADO:

Se tiene el proyecto llamado "proyecto", el mismo contiene una app llamada aplicación que trabaja con el patrón MVT.
La aplicación será utilizada dentro de una empresa industrial para registrar los nuevos equipos en la planta, registrar los
mantenimientos realizados a cada uno de ellos, de forma de tener un historial, y finalmente los diferentes empleados activos. 



MODELS

  Dentro del archivo MODELS.PY se encuentran los siguientes 3 modelos: 

        1. Mantenimiento
        2. Equipo
        3. Empleado 


VIEWS

  Dentro del archivo VIEWS.PY se encuentra la lógica de la aplicación.
  El mismo cuenta con diferentes funciones que tomarán como argumento la request y de acuerdo a esta y gracias a la función render, 
  se devolverá un template personalizado. 
  
  En la versión original de la 3ºPre-Entrega se tenían VISTAS BASADAS EN FUNCIONES para mostrar, por ejemplo, la lista de equipos. 
  En esta nueva versión se trabaja con VISTAS BASADAS EN CLASES (CBV), que permiten realizar el CRUD de cada uno de los modelos.

  Cada función tendrá asociada una ruta/dirección. Las mismas se encuentran definidas en el archivo urls.py dentro de la aplicación, 
  y tendrán un "name" que permitirá identificarlas y llamarlas desde los diferentes botones creados en los templates.

  Las funciones o clases para cada modelo son:

    1. ModeloList -> Muestra una lista de los objetos que pertenecen a dicho modelo. 
    2. ModeloCreate -> Crea un nuevo objeto del modelo correspondiente a partir de los datos ingresados en un formulario.
    3. ModeloDetail -> Muestra los detalles de un objeto determinado de un modelo.
    4. ModeloUpdate -> Permite modificar los datos de un objeto determinado ya creado.
    5. ModeloDelete -> Elimina un objeto de un modelo, con previa confirmación.
    6. buscar_modelo -> Busca en la BD un objeto del modelo de acuerdo a una referencia ingresada en un formulario.



TEMPLATES

  Cada función/clase tendrá su plantilla que mostrará el HTML.
  La plantilla de la página principal se llama "index.html" y contendrá los diferentes botones en su parte superior que permiten 
  el acceso a las áreas de equipos, mantenimientos y empleados. 

  HERENCIA DE TEMPLATES

  Los templates correspondientes a las vistas basadas en clase del tipo LISTA, serán hijas de la plantilla index.html heredando las 
  secciones de Header, Footer y el aspecto general, y teniendo a su vez cierta personalización con, por ejemplo, el título, la imagen 
  de fondo del título, y el contenido general.

      HERENCIA PARA LA PLANTILLA DEL FORMULARIO DE CREACIÓN DE UN NUEVO EQUIPO:
          
      index.html   --->   equipo_list.html    ---->   equipo_form.html

PRUEBA DE LA PÁGINA WEB

    1. Luego de que este corriendo el servidor, ingresar a la dirección del sitio http://127.0.0.1:8000/aplicacion/
    2. Una vez en la página principal clickear en "REGISTRO".
    3. Crear un usuario con un nombre de usuario, contraseña y email.
    4. Al ser redirigido a la página principal, clickear en "LOGIN" e iniciar sesión con los datos ingresados previamente.
    5. Una vez dentro del sistema dirigirse al apartado de "EQUIPOS" en el menú superior.
    6. Crear un nuevo equipo en la BD, clickeando en "Nuevo Registro de Equipo" e ingresando luego los datos solicitados.
    7. Una vez creado el equipo, clickear en la lista el símbolo de la lupa para acceder a los detalles, luego presionar el botón "Volver".
    8. Modificar los datos, clickeando en el símbolo del lápiz con el cuaderno.
    9. Buscar el equipo creado, clickeando en "Búsqueda de Equipo" e ingresando la referencia. Luego presionar el botón "Volver".
    10. Eliminar el equipo creado, confirmando en el mensaje.
    11. Repetir los pasos 5-10 para los modelos restantes (Empleados y Mantenimientos).
    12. Cerrar sesión.



FUTURAS MODIFICACIONES
- Agregado del modelo Publicacion/Post.
- Sistema de registro de usuarios e inicio de sesión en el sistema.
- Modificación de datos del perfil de usuario, incluyendo avatar.
