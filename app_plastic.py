import os
# ----------- variables ----------------------
op_menu = ""          # Selección menú principal
op_menu_producto = ""  # Selección menú productos
nombre_producto = ""  # Nombre del producto
op_tipo_cliente = ""  # Selección General/Socio
tipo_cliente = ""     # --> General/Socio
valor_producto = 0    # Valor por 1 producto
cantidad = 0          # Cantidad de productos
en_efectivo = "N"     # S/N--> en efectivo o NO
subtotal = 0          # Precio X Cantidad
monto_descuento = 0   # valor del dscto aplicado
total_pagar = 0       # Total final a pagar
mensaje = ""          # mensaje para el ticket
# ---- estadísticas ----
recaudacion_total = 0     # ACUMULADOR!!!
total_prod_vendidos = 0   # ACUMULADOR!!!
# ----------- Código Principal -------------------
while True:
    mensaje = ""  # ---> REINICIALIZAR LA VARIABLE
    monto_descuento = 0
    os.system("cls")
    op_menu = str(input('''
    =========== PLASTIC =============                      
    1. Venta de productos
    2. Ver estadísticas
    3. Salir
    \n Elija opción: '''))

    if op_menu == "1":
        os.system("cls")
        print("\n--- Venta de productos ---")
        op_menu_producto = str(input('''
        Producto \t\t Valor General \t Valor Socio
        1.- Tazón \t\t $800 \t\t $500
        2.- Llavero	\t $500 \t\t $300
        3.- Polera estampada \t $5.000 \t $3.000
        \n Elija opción:    '''))

        if op_menu_producto == "1":
            nombre_producto = "Tazón"
            op_tipo_cliente = str(input(f'''
            Seleccinó {nombre_producto}
            (1)General \t (2)Socio
            \n Elija opción:  '''))

            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 800
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 500

        if op_menu_producto == "2":
            nombre_producto = "Llavero"
            op_tipo_cliente = str(input(f'''
            Seleccinó {nombre_producto}
            (1)General \t (2)Socio
            \n Elija opción:  '''))

            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 500
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 300

        if op_menu_producto == "3":
            nombre_producto = "Polera estampada"
            op_tipo_cliente = str(input(f'''
            Seleccinó {nombre_producto}
            (1)General \t (2)Socio
            \n Elija opción:  '''))

            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 5000
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 3000

        cantidad = int(input(f'''
        Seleccionó  {nombre_producto}
        A un precio de ${valor_producto} c/u

        Ingrese la cantidad: '''))

        while not cantidad > 0:
            print("Error, mínimo 1 producto")
            cantidad = int(input(f'''
            Seleccionó  {nombre_producto}
            A un precio de ${valor_producto} c/u

            Ingrese la cantidad: '''))

        subtotal = valor_producto*cantidad

        en_efectivo = str(input(f'''
        subtotal ${subtotal}

        Si paga en efectivo tendra un 20% dscto.

        ¿Paga en efectivo?  S/N ''')).strip().upper()

        if en_efectivo == "S":
            monto_descuento = subtotal*0.20
            mensaje = f"Descuento pago efectivo 20% ${monto_descuento}"

        total_pagar = subtotal-monto_descuento
        # ---- imprimir ticket ---
        os.system("cls")
        print(f'''
        ------- TICKET COMPRA -----
        Producto: {nombre_producto}
        Cantidad de productos:{cantidad}
        Tipo cliente: {tipo_cliente}
        Subtotal ${subtotal}
        {mensaje}
        Total pagar ${total_pagar}   ''')

        os.system("pause")
