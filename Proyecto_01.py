###
# Proyect_01 Calculadora 
###



# Calculadoraa

import flet as ft


## Configuracion de la ventana 

def main(page: ft.Page):
    page.title = 'Calculadora Teo'
    page.window.width = 350
    page.window.height = 460
    page.window.resizable = False
    page.window.maximizable = False 
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20
    
    
    ## Interfaz de numeros 
    
    visor = ft.TextField(
        value='',
        read_only=True,
        text_align='right',
        text_size=26,
        bgcolor= ft.Colors.GREY_900,
        color=ft.Colors.WHITE,
        expand=True 
        )
    
    
    page.add(visor)
    
    ## Creamos logica de operaciones 
    
    def presionar_boton(e):
        texto = e.control.content.value
        
        if texto == 'C':
            visor.value = ''
            
        elif texto == '⌫':
            if visor.value:
                visor.value = visor.value[:-1]
        
        elif texto == '=':
            try:
                resultado = eval(visor.value)
                visor.value= str(resultado)
            except:
                visor.value = 'Error'

        else:
            visor.value += texto 
               
                
        page.update()
        
        
    
    ## Creamos los botones 
    
    def crear_boton(texto, color=ft.Colors.BLUE_GREY_800):
        return ft.ElevatedButton(
            content=ft.Text(
                texto,
                size=20,
                weight=ft.FontWeight.BOLD,
                color= ft.Colors.WHITE
                ),
                bgcolor=color,
                style=ft.ButtonStyle(
                    
                    shape=ft.RoundedRectangleBorder(radius=30),
                    padding=ft.padding.all(18),
                    overlay_color={
                        ft.ControlState.PRESSED: ft.Colors.WHITE_24,
                    },
                    elevation={
                        ft.ControlState.DEFAULT: 5,
                        ft.ControlState.PRESSED: 1
                    },
                ),
                expand=True,
                animate_scale=ft.Animation(100, "easeOut"),
                on_click=presionar_boton
        )
        
        
    page.add(
    ft.Row(
        [
        crear_boton('C', ft.Colors.RED_700),
        crear_boton('⌫', ft.Colors.BLUE_GREY_600),
        
        ],
        expand=True
    )
)               
    page.add(
        ft.Row([
        crear_boton('1'),
        crear_boton('2'),
        crear_boton('3')

        ],
        expand=True   
     )
)
    page.add(
        ft.Row([
        crear_boton('4'),
        crear_boton('5'),
        crear_boton('6')

        ],
        expand=True   
     )
)    
    page.add(
        ft.Row([
        crear_boton('7'),
        crear_boton('8'),
        crear_boton('9')

        ],
        expand=True   
     )
)
    page.add(
    ft.Row([
        crear_boton('0'),
        crear_boton('=' , ft.Colors.GREEN_700)
    ], expand=True)
)
   
    page.add(
    ft.Row(
        [
        crear_boton('+', ft.Colors.ORANGE_700),
        crear_boton('-', ft.Colors.ORANGE_700),
        crear_boton('*', ft.Colors.ORANGE_700),
        crear_boton('/', ft.Colors.ORANGE_700)
        ],
        expand=True
    )
)

    
  
    
ft.app(target = main)
