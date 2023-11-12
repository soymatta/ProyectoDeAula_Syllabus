
# Base de datos
Esta es una explicación detallada de algunos campos que pueden ser algo implicitos.
Arriba de los campos habrá un encabezado con la tabla a la que pertenecen.
Los campos que no aparezcan referenciados en este documento son campos explicitos, es decir, que no necesitan mayor explicación para ser entendibles. Ejemplo: Name, se sabe que name hace referencia al nombre de un registro en una tabla X, o email, que se conoce que hace referencia al correo electronico de una entidad.

Sin mas dilación, aquí los campos que necesitan una explicación extra:

# Tabla: users
**status:** El campo que indica si la cuenta del usuario está activa o no, al ser booleano, toma dos valores: 1 y 0, referenciando Verdadero (*True*) y falso (*False*).

**subjects:** Este campo es un Array-String, es decir, una lista en forma de string ( '[ ]' ), que indica todas las materias en las que un profesor está a cargo, es Nullable debido a que un profesor recién ingresado al sistema puede no tener materias aún.

**faculties:** Este campo es un Array-String también. Indica todas las facultades a las que un profesor hace parte.

**image:** Este campo referencia la imagen que tiene el usuario, pero se guarda como URL. El valor por defecto está por definirse. Un ejemplo puede ser: imagen.png

**last_update:** Este campo hace referencia a la ultima vez que un profesor hizo cambios dentro del Syllabus. Los cambios pueden ser apreciados desde el control de versiones.


# Tabla: subjects
**faculties:** Array-String. Hace referencia a todas las facultades en las que está una materia.

**teachers:** Array-String. Hace referencia a todos los profesores que tienen una materia encargada.

**content:** El contenido pragmatico de una materia, este aparecerá mucho mas organizado en el apartado de Syllabus.


# Tabla: faculties
**subjects:** Array-String. Todas las materias que conforman una facultad.

**teachers:** Array-String. Todos los profesores pertenecientes a una facultad.

# Tabla: syllabus
Aquí debo hacer un parentesis... La mayoría de campos de esta tabla referencian un "apartado" del Syllabus. Es decir, para que se entienda mejor... Un Numero Romano. Estos "apartados" van desde el ciclo (I:1) hasta la bibliografía (X:10), es decir, hay 10 apartados y cada uno es un campo en la base de datos. Su traducción es directa, por lo que no tengo que especificar demasiado. Algunos de estos campos son Strings normales, sin más, sin embargo, hay otros que son un dato de tipo MAP reconvertido a String, es decir, un objeto o diccionario en forma de String ( '{ }' ), por lo que me limitaré a explicar estos ultimos, referenciando cuales serán sus LLAVES y VALORES.

Aquí una URL de referencia [https://aulasvirtuales.unilibre.edu.co/pluginfile.php/58154/mod_resource/content/7/MICROCURR%C3%8DCULO%20Ingenier%C3%ADa%20del%20Software%20II.pdf]. Cuando se aprecie una especie de tabla dividida en dos se sabe que es un tipo Map-String. La columna izquierda de la tabla hace referencia a las llaves y la columna derecha a los valores.

**identification:** Algunos ejemplos de la relación de las llaves con los valores son: 

## Llave ||| Valor
|----------------|
Codigo      02607
Semestre    Sexto

Y así con los demás. Es importante ver el link para que se aprecie con detalle y se entienda mejor.

**evaluation:** Con este campo pasa algo curioso. Como se puede apreciar en la imagen proporcionada arriba, este apartado con el numero romano IX (9) contiene dos columnas referenciadas como: PORCENTAJE y ESTRATEGIAS.
El chiste es que cada CORTE referenciado debajo de la columna porcentaje sea una LLAVE, pero si hay varias filas de texto en la columna de ESTRATEGIAS, entonces... ¿Cuales son su valores? Bueno... Cada CORTE es otro Map-String (si, con sus propias llaves y valores). 

'''
evaluation = {
    'cortes': {
        'primer_corte': {
            'key1': 'texto referenciado debajo de la columna ESTRATEGIAS'
        },
        'segundo_corte': {
            'key1': 'same',
            'key2': 'segunda linea de texto (si la hay).'
        },
        'tercer_corte': {
            'key1': 'same'
        }
    }
}
'''

Sinceramente, no espero que se haya entendido del todo, de todas formas, yo me encargaré de esa parte.

# Tabla: versions
**owner:** Hace referencia al campo "responsable" que aparece al final del documento cuyo link fue proporcionado arriba. Es simplemente el nombre del admin o profesor que hizo el cambio referenciado en un registro de la tabla.


# Para terminar...
Cualquier duda me la pueden comentar al privado o en el grupo, hay cosas que claramente son complicadas de explicar y por ende, aún más dificiles de entender, por lo que espero que me las hagan saber.
