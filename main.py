import flet as ft
from config import (color_pagina, color_letras, sitiosElegidos, color_boton_presionado,
                    lista_de_botones_sitio,lista_de_botones_files,urlElegidos,lista_de_botones_url,filesElegidos)
from sitios import (contentSitios, columna_sitios, BotonSitio, contenidoFiles,BotonSeleccion,
                    column_files, BotonFiles, contenidoUrl, columna_url, BotonUrl, content_inoOpe, ElTitulo)

# ================================= PAGINA PRINCIPAL =======================
def main(page: ft.Page):
    page.bgcolor = color_pagina

    class PaginaPrincipal:
        def __init__(self,contenido):
            self.contenido = contenido
            self.contenedor = ft.Container(
                content=contenido,
                bgcolor=color_pagina,
                expand=True,
                border_radius=9,
                padding=30,
                border=ft.border.all(5, "BLACK"),
                alignment=ft.alignment.top_center)


    Titulo = ft.Text("Búsquedas avanzadas",theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,weight=ft.FontWeight.W_900,color=color_letras,expand=True)

    # ===================== Aca estan las opciones para elegir y escribir ===================
    # Primera opcion, la de que se requiere buscar
    busquedaEscribir = ft.TextField(expand=True,color=color_letras,label="Buscar",
                                    border_color="#397185",label_style=ft.TextStyle(color=color_letras))
    infoOperadores = ft.AlertDialog(
        modal=True, bgcolor=color_pagina,
        title=ft.Text("Operadores logicos", color=color_letras, weight=ft.FontWeight.W_900),
        content=content_inoOpe, adaptive=True,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: page.close(infoOperadores)),
        ],
        actions_alignment=ft.MainAxisAlignment.END)

    bt_infoOpe = ft.IconButton(icon=ft.Icons.INFO_OUTLINED,
                                icon_color=ft.Colors.BLACK,
                                icon_size=40,
                                on_click=lambda e: page.open(infoOperadores))

    # SEGUNDA OPCION, ELEGIR SITIO DE BUSQUEDA SITE

    def cerrarVentana(totalSeleccionado,lista,ventana):
        totalSeleccionado.value = f"{lista}"
        page.update()
        page.close(ventana)

    def agregarMiSeleccion(entrada,listaBotones,contenido,listaElegida,totalSeleccionado,esteBoton):

        if entrada.value in listaBotones:
            pass
        else:
            if entrada.value != "":
                new_bt = esteBoton(entrada.value).bt
                new_bt.bgcolor = color_boton_presionado
                contenido.controls.append(new_bt)
                listaElegida.append(entrada.value)
                totalSeleccionado.value = f"{listaElegida}"
                listaBotones.append(entrada.value)

        page.update()


    sitiosVentana = ft.AlertDialog(
        modal=True,bgcolor=color_pagina,
        title=ft.Text("Sitios mas comunes",color=color_letras,weight=ft.FontWeight.W_900),
        content=contentSitios,adaptive=True,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e:cerrarVentana(sitioTotal,sitiosElegidos,sitiosVentana)),
        ],
        actions_alignment=ft.MainAxisAlignment.END)

    sitioEscribir = ft.TextField(expand=True,color=color_letras,label="Sitio",border_color="#397185",label_style=ft.TextStyle(color=color_letras))
    sitioAgregar = ft.IconButton(icon=ft.Icons.ADD,
                    icon_color=ft.Colors.BLACK,
                    icon_size=40,
                    on_click=lambda e: agregarMiSeleccion(sitioEscribir,lista_de_botones_sitio,columna_sitios,sitiosElegidos,sitioTotal,BotonSitio),
                                 )
    sitioBuscar = ft.IconButton(icon=ft.Icons.SEARCH,
                    icon_color=ft.Colors.BLACK,
                    icon_size=40,
                    on_click=lambda e: page.open(sitiosVentana)
                        )

    sitioTotal = ft.Text(sitiosElegidos,color=color_letras)

    # TERCERA OPCION FILETYPE

    filesVentana = ft.AlertDialog(
        modal=True, bgcolor=color_pagina,
        title=ft.Text("Tipos de archivos mas comunes", color=color_letras, weight=ft.FontWeight.W_900),
        content=contenidoFiles, adaptive=True,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: cerrarVentana(filesTotal,filesElegidos,filesVentana)),
        ],
        actions_alignment=ft.MainAxisAlignment.END)

    fileEscribir = ft.TextField(expand=True,color=color_letras,label="Tipo de archivo",border_color="#397185",label_style=ft.TextStyle(color=color_letras))
    fileAgregar = ft.IconButton(icon=ft.Icons.ADD,
                                 icon_color=ft.Colors.BLACK,
                                 icon_size=40,
                                 on_click=lambda e: agregarMiSeleccion(fileEscribir,lista_de_botones_files,column_files,filesElegidos,filesTotal,BotonFiles),
                                 )
    fileBuscar = ft.IconButton(icon=ft.Icons.SEARCH,
                                icon_color=ft.Colors.BLACK,
                                icon_size=40,
                                on_click=lambda e: page.open(filesVentana)
                                )

    filesTotal = ft.Text(filesElegidos,color=color_letras)

    # CUARTA PARTE, inurl

    urlVentana = ft.AlertDialog(
        modal=True, bgcolor=color_pagina,
        title=ft.Text("inurl", color=color_letras, weight=ft.FontWeight.W_900),
        content=contenidoUrl, adaptive=True,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: cerrarVentana(urlTotal,urlElegidos,urlVentana)),
        ],
        actions_alignment=ft.MainAxisAlignment.END)


    urlEscribir = ft.TextField(expand=True,color=color_letras,label="Por url",border_color="#397185",label_style=ft.TextStyle(color=color_letras))
    urlAgregar = ft.IconButton(icon=ft.Icons.ADD,
                                icon_color=ft.Colors.BLACK,
                                icon_size=40,
                                on_click=lambda e: agregarMiSeleccion(urlEscribir,lista_de_botones_url,columna_url,urlElegidos,urlTotal,BotonUrl))
    urlBuscar = ft.IconButton(icon=ft.Icons.SEARCH,
                                icon_color=ft.Colors.BLACK,
                                icon_size=40,
                                on_click=lambda e: page.open(urlVentana))

    urlTotal = ft.Text(urlElegidos,color=color_letras)

    # QUINTA PARTE, intex: / allintex:
    porFraceIntext = ft.CupertinoSwitch(
            label="Frace",
            value=True)

    intextEscribir = ft.TextField(expand=True,color=color_letras,label="Buscar por palabra/s o frace",
                                  border_color="#397185",label_style=ft.TextStyle(color=color_letras))

    # SEXTA PARTE, intitle: / allintitle:

    titleEscribir = ft.TextField(expand=True,color=color_letras,label="Buscar por palabra/s o frace en titulos",
                                 border_color="#397185",label_style=ft.TextStyle(color=color_letras))
    porFraceTitle = ft.CupertinoSwitch(
        label="Frace",
        value=True)

    # BOTONES FINALES

    def limpiar():
        busquedaEscribir.value = ""
        sitioEscribir.value = ""
        fileEscribir.value = ""
        urlEscribir.value = ""
        intextEscribir.value = ""
        titleEscribir.value = ""

        sitiosElegidos.clear()
        filesElegidos.clear()
        urlElegidos.clear()

        sitioTotal.value = ""
        filesTotal.value = ""
        urlTotal.value = ""

        resultadoFinal.value = ""

        page.update()

    def convertirLista(lista,cmd):
        if len(lista) == 0:
            return ""
        elif len(lista) == 1:
            resultado = f"{cmd}:{lista[0]}"
            return resultado
        else:
            resultado = f"{cmd}:"
            for i in range(len(lista)):
                pre = f" OR {cmd}:"
                if i == 0:
                  resultado = resultado + lista[i]
                  continue

                resultado = resultado + pre + lista[i]
            return "("+ resultado + ")"

    def convertirFrace(valorCupertino,entrada,junto,separado):
        if entrada.value == "":
            return ""

        if valorCupertino.value == True:
            textoJunto = junto + " " + f'"{entrada.value}"'
            return "(" + textoJunto + ")"
        else:
            lista = entrada.value.split(" ")
            textoSeparado = separado
            for i in lista:
                textoSeparado = textoSeparado + " " + i
            return "(" + textoSeparado + ")"

    def ConvertirResultadoFinal():

        parteSitio = convertirLista(sitiosElegidos,"site")
        parteFile = convertirLista(filesElegidos,"filetype")
        parteUrl = convertirLista(urlElegidos,"inurl")
        parteIntext = convertirFrace(porFraceIntext,intextEscribir,"intext:","allintext:")
        parteIntitle = convertirFrace(porFraceTitle,titleEscribir,"intitle:","allintitle:")

        consultaCompleta = (busquedaEscribir.value + " " + parteSitio + " " + parteFile + " " + parteUrl + " "
                            + parteIntext + " " + parteIntitle)
        resultadoFinal.value = consultaCompleta
        page.update()

    bt_clear = ft.ElevatedButton(text="Limpiar",bgcolor="#E86D5A",color=color_letras,on_click=lambda e:limpiar())
    bt_convertir = ft.ElevatedButton(text="Convertir",bgcolor="#6784E6",color=color_letras,on_click=lambda e:ConvertirResultadoFinal())

    resultadoFinal = ft.TextField(expand=True,color=color_letras,label="Resultado",multiline=True,
                                  border_color="#397185",label_style=ft.TextStyle(color=color_letras))

    def copiar_al_portapapeles(e, texto):
        # Accedemos a la página para usar el portapapeles del sistema
        page.set_clipboard(texto)

    bt_copiar = ft.IconButton(icon=ft.Icons.COPY_ALL,
                                icon_color=ft.Colors.BLACK,
                                icon_size=40,
                                on_click=lambda e: copiar_al_portapapeles(e,resultadoFinal.value))

    paginaUno = PaginaPrincipal(
        ft.Column([ Titulo,
                            ft.Row([busquedaEscribir,bt_infoOpe]),
                            ft.Row([sitioEscribir,sitioAgregar,sitioBuscar]),
                            sitioTotal,

                            ft.Row([fileEscribir,fileAgregar,fileBuscar]),
                            filesTotal,

                            ft.Row([urlEscribir,urlAgregar,urlBuscar]),
                            urlTotal,

                            ft.Row([intextEscribir,porFraceIntext]),
                            ft.Row([titleEscribir,porFraceTitle]),
                            ft.Row([bt_clear,bt_convertir],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                            ft.Row([resultadoFinal,bt_copiar])

                   ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO,
                     alignment=ft.MainAxisAlignment.START )).contenedor
    page.add(paginaUno)

ft.app(target=main)
