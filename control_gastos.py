import flet as ft


def main(page: ft.Page):
    page.title = "Control de Gastos"
    page.bgcolor = "#F0F4F8"
    page.padding = 20
    page.scroll = "auto"

    
    gastos = []


    txt_descripcion = ft.TextField(
        label="Descripción",
        hint_text="Ej. Supermercado",
        expand=True,
        border_radius=10,
    )
    txt_monto = ft.TextField(
        label="Monto ($)",
        hint_text="0.00",
        width=150,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10,
    )
    dd_categoria = ft.Dropdown(
        label="Categoría",
        width=180,
        border_radius=10,
        options=[
            ft.dropdown.Option("Alimentación"),
            ft.dropdown.Option("Transporte"),
            ft.dropdown.Option("Entretenimiento"),
            ft.dropdown.Option("Salud"),
            ft.dropdown.Option("Hogar"),
            ft.dropdown.Option("Otros"),
        ],
        value="Otros",
    )

    
    lbl_total = ft.Text(
        "Total: $0.00",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="#2D3748",
    )

    
    lista_gastos = ft.Column(spacing=8, scroll="auto", expand=True)

    
    lbl_error = ft.Text("", color="red", size=13)

    
    def calcular_total():
        return sum(g["monto"] for g in gastos)

    def refrescar_lista():
        lista_gastos.controls.clear()
        for i, g in enumerate(gastos):
            idx = i  

            def hacer_eliminar(index):
                def eliminar(e):
                    if 0 <= index < len(gastos):
                        gastos.pop(index)
                        refrescar_lista()
                return eliminar

            lista_gastos.controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        g["descripcion"],
                                        weight=ft.FontWeight.W_600,
                                        size=14,
                                    ),
                                    ft.Text(
                                        g["categoria"],
                                        size=12,
                                        color="#718096",
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            ft.Text(
                                f"${g['monto']:,.2f}",
                                size=15,
                                weight=ft.FontWeight.BOLD,
                                color="#2B6CB0",
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE_OUTLINE,
                                icon_color="#E53E3E",
                                tooltip="Eliminar",
                                on_click=hacer_eliminar(idx),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor="white",
                    border_radius=10,
                    padding=ft.padding.symmetric(horizontal=16, vertical=10),
                    shadow=ft.BoxShadow(
                        blur_radius=4,
                        color=ft.Colors.with_opacity(0.08, "black"),
                        offset=ft.Offset(0, 2),
                    ),
                )
            )
        lbl_total.value = f"Total: ${calcular_total():,.2f}"
        page.update()

    def agregar_gasto(e):
        lbl_error.value = ""
        desc = txt_descripcion.value.strip()
        monto_str = txt_monto.value.strip().replace(",", ".")
        if not desc:
            lbl_error.value = "Ingresa una descripción."
            page.update()
            return
        try:
            monto = float(monto_str)
            if monto <= 0:
                raise ValueError
        except ValueError:
            lbl_error.value = "Ingresa un monto válido mayor a 0."
            page.update()
            return

        gastos.append({
            "descripcion": desc,
            "monto": monto,
            "categoria": dd_categoria.value,
        })
        txt_descripcion.value = ""
        txt_monto.value = ""
        refrescar_lista()

    
    btn_agregar = ft.ElevatedButton(
        "Agregar",
        icon=ft.Icons.ADD,
        bgcolor="#3182CE",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click=agregar_gasto,
    )

    
    form_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Nuevo gasto",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#2D3748",
                ),
                ft.Row(
                    controls=[txt_descripcion, txt_monto, dd_categoria],
                    spacing=10,
                ),
                ft.Row(
                    controls=[btn_agregar, lbl_error],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=12,
        ),
        bgcolor="white",
        border_radius=14,
        padding=20,
        shadow=ft.BoxShadow(
            blur_radius=8,
            color=ft.Colors.with_opacity(0.10, "black"),
            offset=ft.Offset(0, 3),
        ),
    )

    
    lista_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            "Mis gastos",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color="#2D3748",
                        ),
                        lbl_total,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=1, color="#E2E8F0"),
                lista_gastos,
            ],
            spacing=10,
            expand=True,
        ),
        bgcolor="white",
        border_radius=14,
        padding=20,
        expand=True,
        shadow=ft.BoxShadow(
            blur_radius=8,
            color=ft.Colors.with_opacity(0.10, "black"),
            offset=ft.Offset(0, 3),
        ),
    )

    
    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "💰 Control de Gastos",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#1A365D",
                ),
                form_container,
                lista_container,
            ],
            spacing=20,
            expand=True,
        )
    )


ft.app(main)
