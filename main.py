import flet as ft
def main(page: ft.Page):
    page.title="Examen final - Registro de estudiantes"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.add(ft.Text(value="Registro de participantes", size=25))
    
    nombre = ft.TextField(
        value="",
        label="Escriba su nombre completo: ",
        color=ft.Colors.BLUE,
        on_change=lambda e: print(e.control.value),
        on_submit=lambda e: print("Enter presionado")
    )
    page.add(nombre)
    
    correo = ft.TextField(
        value="",
        label="Escriba su correo electronico",
        color=ft.Colors.BLUE,
    )
    page.add(correo)
    
    page.add(ft.Text("--Taller de interes--"))
    taller = ft.Dropdown(
        value="Taller",
        options=[
            ft.DropdownOption(key="principiantes", text="Python para principiantes."),
            ft.DropdownOption(key="intermedio", text="Flet intermedio."),
            ft.DropdownOption(key="panda", text="Analisis de datos con pandas."),
        ],
    )
    page.add(taller)
    
    page.add(ft.Text("--Modalidad de pago--"))
    pago = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="completo", label="Pago completo"),
            ft.Radio(value="cuotas", label="Pago por cuotas"),
        ])
    )
    page.add(pago)
    
    page.add(ft.Text("--Requiere computadora portatil--"))
    requerimientos = ft.Checkbox(
        label="Si",
        value=False,
        check_color=ft.Colors.WHITE,
        fill_color=ft.Colors.GREEN
    )
    page.add(requerimientos)
    
    page.add(ft.Text("--Nivel de experiencia--"))
    experiencia = ft.Slider(
        value= 1,
        min=0,
        max=5,
        divisions=5
    )
    page.add(experiencia)
    
    def mostrar_resumen(e):
        page.add(nombre, correo, taller, pago, requerimientos, experiencia)
    
    mostrar_resumen=ft.ElevatedButton(
        content="Mostrar ficha del participante",
        icon=ft.Icons.SAVE,
        color=ft.Colors.BLUE,
        on_click=lambda e: print("Click!")
    )
    page.add(mostrar_resumen)
    
    
    ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400)
    ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400)
    
    """page.add(ft.Text("--Ficha del participante--"))
    ft.Text= value="Nombre: " + nombre + "\n",
    ft.Text(value="Correo electronico: " + correo + "\n"),
    ft.Text(value="Taller: " + taller + "\n"),
    ft.Text(value="Pago: " + pago + "\n"),
    ft.Text(value="Requerimientos: " + requerimientos + "\n"),
    ft.Text(value="Experencia: " + experiencia + "\n")"""
    
    ft.ListView(
    controls=[
        ft.Text(str("Nombre: " +nombre + "\n")),
        ft.Text(str("Correo electronico: " + correo + "\n")),
        ft.Text(str("Taller: " + taller + "\n")),
        ft.Text(str("Pago: " + pago + "\n")),
        ft.Text(str("Requerimientos: " + requerimientos + "\n")),
        ft.Text(str(int("Experiencia: " + experiencia + "\n")))
        ],
    )    
ft.run(main)
