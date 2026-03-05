import flet as ft

def crear_campos(etiquetas):
    
    campos =[]
         
    for etiqueta in etiquetas:
        campos.append(ft.TextField(value="", border=12, width=250, label=etiqueta))
    
    return campos

def calcular_intereses(e,monto):
    return monto *.01













def main(page: ft.Page):
    page.title = 'Calculator'
    page.window.width = 320
    page.window.height = 450
    page.bgcolor = ft.Colors.INDIGO_300
    page.window.resizable = False
    page.window.maximizable = False
    
    
    
    def actualizar(e):
        
        campos = crear_campos(["monto", "interes por dia"])
        pedido = int(monto.value)
        
        page.clean()
        contenedor.content =ft.Column(
        controls=[*campos, ft.ElevatedButton("calcular con pago diario", bgcolor=ft.Colors.AMBER, width=250,on_click=calcular_interes) ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER  
        )
        campos[0].value = pedido
        campos[1].value = "un por ciento por dia"
        page.add(contenedor)
        page.update() 
        
    def calcular_pago(e):
        page.clean()
        campos = crear_campos(["dia","monto", "interes", "total"])
        contenedor.content =ft.Column(
        controls=[*campos, ft.ElevatedButton("calcular con pago diario", bgcolor=ft.Colors.AMBER, width=250,on_click=calcular_interes) ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER  
        )
        pedido = int(monto.value)
        dia = 1
        interes = calcular_intereses(e,pedido)
        campos[0].value = dia
        campos[1].value = pedido
        campos[2].value = interes
        campos[3].value = pedido + interes
        page.add(contenedor)
        page.update() 
        
        
            
           
    
    def calcular_interes():
        campos = crear_campos(["dia","monto", "interes", "total"])
        pedido = int(monto.value)
        
        
        page.clean()
        contenedor.content =ft.Column(
        controls=[*campos, ft.Row(controls=[ft.ElevatedButton("calcular con pago diario", bgcolor=ft.Colors.AMBER, width=125, on_click=calcular_intereses),
                                            ft.ElevatedButton("pagos", bgcolor=ft.Colors.AMBER, width=125, on_click=calcular_pago)]) ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER  
        )
        
        campos[0].value = 0
        campos[1].value = pedido
        campos[2].value = 0
        campos[3].value = pedido
        
        
         
        page.add(contenedor)
        page.update()  
                
    
        
            
    
    
    
    monto = ft.TextField(value="", border=12, width=250, label="solicitud")
    monto.hint_text = "ingresa el monto a solicitar"
    
    boton = ft.ElevatedButton("solicitar", bgcolor=ft.Colors.AMBER, on_click=actualizar, width=250)
    
    
    contenedor = ft.Container(
        content=ft.Column(
            controls=[monto, boton],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER  
        ),
        expand=True,
        alignment=ft.Alignment.CENTER  
    )
    
    page.add(contenedor)

ft.app(target=main)