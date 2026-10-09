# Tarjeta de Carlos Muñoz Alarcón

Abre `index.html` en un navegador. Para publicarla, sube la carpeta completa, incluido `carlos-munoz.vcf`, y conserva la carpeta hermana `imagenes` con `logo-bionativa.png` en el alojamiento de tu elección.

El botón Guardar contacto descarga una vCard 3.0 en UTF-8. El teléfono o la aplicación de contactos pide confirmar la importación; una página web no puede agregar contactos a la agenda sin intervención del usuario. Si el navegador descarga el archivo, ábrelo desde Descargas para importarlo. Al alojarla, configura `.vcf` con Content-Type `text/vcard; charset=utf-8`.

Datos tomados del HTML entregado por el usuario: Carlos Muñoz Alarcón, Bionativa, cmunoz@bionativa.cl, móvil +56958128098 y oficina +56712970696. Cargo actualizado a CEO por indicación del usuario. El original incluye dos destinos de WhatsApp distintos: se utiliza el móvil del botón principal para WhatsApp y el otro número como teléfono de oficina.

El logo oficial usa `../imagenes/logo-bionativa.png`, facilitado por el usuario, en ambas cabeceras y en el fondo. La marca de agua muestra directamente el PNG original, sin trazado, filtros ni cambios de formas o letras; únicamente se reduce su opacidad y se limita su tamaño. El PNG es de 300 × 300 píxeles, por lo que su nitidez al ampliarlo está limitada por esa resolución. Los anteriores archivos de trazado no se utilizan en la página. La fotografía carga desde la dirección original de Obbi; necesita conexión a internet y que ese recurso siga disponible. Los iconos son SVG incluidos en el HTML; no se requieren bibliotecas externas.

El escritorio ocupa todo el ancho de la ventana, con paneles al 46% y 54%. A partir de 1100 píxeles, los enlaces se distribuyen en dos columnas. En teléfonos el contenido se apila. No se fija la altura para permitir el desplazamiento cuando el contenido supera la altura de la ventana.

Compartir usa el menú del dispositivo cuando está disponible. Como alternativa abre un diálogo con WhatsApp, correo y copia del enlace. Publicada, la tarjeta comparte su URL actual; abierta localmente, comparte el perfil original e informa de ello en el diálogo.

No se reprodujeron las llamadas de seguimiento de Obbi ni su token. El HTML original enlaza Guardar contacto a un endpoint de Obbi y no contiene el contenido del archivo descargado. El comportamiento exacto de Tukcards no pudo comprobarse: aquí se implementó una descarga estándar de vCard.

Se verificó la lectura de los archivos creados. La revisión visual en navegador y la importación en teléfonos quedan pendientes por fallos del entorno de ejecución.
