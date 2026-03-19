import flet as ft
from config import color_letras,color_pagina,color_botones,sitiosElegidos,color_boton_presionado,filesElegidos,urlElegidos

def agregarSeleccion(e,nombre,lista):

    if nombre in lista:
        e.control.bgcolor = color_botones
        lista.remove(nombre)
    else:
        lista.append(nombre)
        e.control.bgcolor = color_boton_presionado  # Color de "activado"

    # Refresca el componente en la pantalla
    e.control.update()

class BotonSeleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bt = ft.ElevatedButton(text=nombre,
                                    color=color_letras,
                                    bgcolor=color_botones)
class BotonSitio(BotonSeleccion):
    def __init__(self, nombre):
        super().__init__(nombre)   # hereda TODO lo general
        self.bt.on_click = lambda e: agregarSeleccion(e, nombre,sitiosElegidos)

class BotonFiles(BotonSeleccion):
    def __init__(self, nombre):
        super().__init__(nombre)   # hereda TODO lo general
        self.bt.on_click = lambda e: agregarSeleccion(e, nombre,filesElegidos)

class BotonUrl(BotonSeleccion):
    def __init__(self, nombre):
        super().__init__(nombre)   # hereda TODO lo general
        self.bt.on_click = lambda e: agregarSeleccion(e, nombre,urlElegidos)


class ElTitulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tit = ft.Text(f"{nombre}",color=color_letras,weight=ft.FontWeight.W_900)

# Contenido info de operadores

columna_infoOpe = ft.Column([
                    ft.Text('Comillas: ""',size=23,weight=ft.FontWeight.W_900,color=color_letras),
                    ft.Text("Búsqueda exacta. Obliga a Google a buscar la frase tal cual está escrita, respetando el orden.",color=color_letras,size=20),
                    ft.Text('Ejemplo: "Quijote de la mancha"',color=color_letras,size=20),
                    ft.Text('Exclusión: -',size=23,weight=ft.FontWeight.W_900,color=color_letras),
                    ft.Text("Elimina resultados que contengan una palabra específica. Limpia la basura.",color=color_letras,size=20),
                    ft.Text('Ejemplo: "Buscar documentos que NO contengan la palabra “resumen" --> -resumen',color=color_letras,size=20),
                    ft.Text('Comodín *', size=23, weight=ft.FontWeight.W_900, color=color_letras),
                    ft.Text("Funciona para completar una frases.", color=color_letras, size=20),
                    ft.Text('"la vida es * y dura"', color=color_letras,size=20),
                    ft.Text("FUNCIONA PARA TODOS LOS CAMPOS",color="RED",size=20),

],scroll=ft.ScrollMode.AUTO)


content_inoOpe = ft.Container(
    content=columna_infoOpe,
    bgcolor=color_pagina,
    expand=True,
    border_radius=9,
    padding=10,
    border=ft.border.all(3, "BLACK"),
    alignment=ft.alignment.top_center)



# Contenido de site:

columna_sitios = ft.Column([
            ElTitulo("🏢 Empresas y sector privado").tit,
            ft.Row([BotonSitio(".com").bt,BotonSitio("com.ar").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio(".net").bt,BotonSitio(".org").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("🎓 Gobiernos y organismos").tit,
            ft.Row([BotonSitio(".gov").bt,BotonSitio(".gob.ar").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio(".edu").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("‍💻 Código y desarrollo").tit,
            ft.Row([BotonSitio("github.com").bt,BotonSitio("gitlab.com").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("🗣️ Foros y comunidades").tit,
            ft.Row([BotonSitio("stackoverflow.com").bt,BotonSitio("reddit.com").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio("answers.microsoft.com").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("📰 Noticias y medios").tit,
            ft.Row([BotonSitio("lanacion.com.ar").bt,BotonSitio("derechadiario.com.ar").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio("tn.com.ar").bt,BotonSitio("clarin.com").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("☁️ Servicios en la nube").tit,
            ft.Row([BotonSitio("drive.google.com").bt,BotonSitio("docs.google.com").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio("onedrive.live.com").bt,BotonSitio("dropbox.com").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("📱 Redes sociales").tit,
            ft.Row([BotonSitio("facebook.com").bt,BotonSitio("instagram.com").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio("x.com").bt,BotonSitio("youtube.com").bt],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([BotonSitio("linkedin.com").bt,BotonSitio("tiktok.com").bt],alignment=ft.MainAxisAlignment.CENTER),

            ElTitulo("Mis sitios").tit

],horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO)


contentSitios = ft.Container(
    content=columna_sitios,
    bgcolor=color_pagina,
    expand=True,
    border_radius=9,
    padding=10,
    border=ft.border.all(3, "BLACK"),
    alignment=ft.alignment.top_center)

# Contendio del filetype:

column_files = ft.Column([
                    ElTitulo("📄 Documentos").tit,
                    ft.Row([BotonFiles("pdf").bt,BotonFiles("docx").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("doc").bt,BotonFiles("xls").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("xlsx").bt,BotonFiles("csv").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ElTitulo("🗃️ Backups y comprimidos").tit,
                    ft.Row([BotonFiles("zip").bt,BotonFiles("rar").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("tar").bt,BotonFiles("gz").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("bak").bt,BotonFiles("backup").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ElTitulo("🧑‍💻 Código y configs").tit,
                    ft.Row([BotonFiles("txt").bt,BotonFiles("log").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("conf").bt,BotonFiles("cfg").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("yml").bt,BotonFiles("yaml").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("json").bt,BotonFiles("xml").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ElTitulo("🛢️ Bases de datos").tit,
                    ft.Row([BotonFiles("sql").bt, BotonFiles("db").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("sqlite").bt, BotonFiles("mdb").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ElTitulo("🌐 Web y front").tit,
                    ft.Row([BotonFiles("html").bt, BotonFiles("js").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("css").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ElTitulo("🖼️ Imágenes").tit,
                    ft.Row([BotonFiles("jpg").bt, BotonFiles("png").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([BotonFiles("svg").bt, BotonFiles("gif").bt],alignment=ft.MainAxisAlignment.CENTER),
                    ElTitulo("Mis sitios").tit

],horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO)

contenidoFiles = ft.Container(
    content=column_files,
    bgcolor=color_pagina,
    expand=True,
    border_radius=9,
    padding=10,
    border=ft.border.all(3, "BLACK"),
    alignment=ft.alignment.top_center)

# Contenido del inurl

columna_url = ft.Column([ElTitulo("url interesante").tit,
                                ft.Row([BotonUrl("admin").bt,BotonUrl("login").bt],alignment=ft.MainAxisAlignment.CENTER),
                                ElTitulo("Mis sitios").tit
                                ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO)

contenidoUrl = ft.Container(
    content=columna_url,
    bgcolor=color_pagina,
    expand=True,
    border_radius=9,
    padding=10,
    border=ft.border.all(3, "BLACK"),
    alignment=ft.alignment.top_center)
