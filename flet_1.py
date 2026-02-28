###
# PROYECTO RED DE CODIGO
###

import flet as ft

def main(page: ft.Page):
    page.title = 'Calculator'
    page.window.width = 320
    page.window.height = 450
    page.bgcolor = ft.Colors.GREY_900
    page.window.resizable = False
    page.window.maximizable = False
    

    
    page.add(ft.Row([
        ft.ElevatedButton('1', bgcolor=ft.Colors.TRANSPARENT, color=ft.Colors.WHITE)
    ]))
    
    
   


ft.app(target=main)
