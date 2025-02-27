import flet as ft
import qrcode

count = 1

def main(page: ft.Page):
    global count

    def generate_qr(e):
        '''Generate QR from text_entry text'''
        global count
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_entry.value)
        qr.make(fit=True)

        imagen_qr = qr.make_image(fill_color="black", back_color="white")
        name_file=f"qr_code{count}.PNG"
        imagen_qr.save(name_file)
        show_qr.content =  ft.Image(src=name_file)
        show_qr.update()
        count += 1
        show_msg.value="Your qr was generated"
        show_msg.update()

        text_entry.value=""
        text_entry.update()

    page.title="from text to QR code"
    page.vertical_alignment="center"

    head=ft.Text("Text-to-QR", size=24, color=ft.colors.BLUE_800, text_align="center")
    text_entry = ft.TextField(label="Enter your content here")
    generate_btn = ft.FilledButton(text="Generate QR", on_click=generate_qr)
    show_qr = ft.Container( alignment=ft.alignment.center)
    show_msg= ft.Text(value="", size=15)

    page.add(
        ft.Container(content=head, padding=10, alignment=ft.alignment.center),
        ft.Container(content=text_entry, padding=20),
        ft.Container(content=generate_btn, alignment=ft.alignment.center),
        show_qr,
        ft.Container(content=show_msg, alignment=ft.alignment.center)
        )

ft.app(main)
