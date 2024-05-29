import flet as ft
import webbrowser

def main(page: ft.Page):
    
    def share_by_whatsapp(e):
        "Share the ciphered text by whatsapp"
        text= the_message.value
        url = f"https://wa.me/?text={text}"
        webbrowser.open(url)

    def encrypt_text(key):
        "Encrypting 'user_text' using 'user_key'"
        new_text = ""
        for char in user_text.value:
            if char.isalpha():
                char = convert_char(char, key)
            new_text += char
        update_texts(new_text)

    def validate_data(e):
        "Validate data and eval action"
        if len(user_text.value):
            try:
                the_key =  int(user_key.value) % 26
                if e.control == encrypt_b:
                    encrypt_text(the_key)
                else:
                    encrypt_text(-the_key)
            except:
                ...

    def update_texts(new_text):
        user_text.value = ""
        user_key.value = ""
        the_message.value = f"\"{new_text}\""
        share_b.visible=True
        page.update()
    
    def convert_char(c, key):
        "Return the new one in upper or lower as the original"
        new_order = ord(c.upper()) + key
        if new_order > 90: 
            new_order -= 26
        if new_order < 65: 
            new_order += 26 

        if c.islower():
            return chr(new_order).lower()
        return chr(new_order)


    page.title = "CA3S45 says:"
    page.window_maxwidth = 640
    page.horizontal_alignment="center"
    page.vertical_aligment="center"
    page.theme_mode = "dark"
    page.bgcolor="black"
    page.scroll="auto"
    page.padding=30
    logo = ft.Image(
        src=f"img/caesar_says.png", height=240)
    head = ft.Container(content=logo, width=540, padding=10)
    
    #Take the text
    user_text = ft.TextField(label="Your message here", multiline=True, text_size=18, bgcolor=ft.colors.GREY_900)
    #Take the Key
    user_key = ft.TextField(label="Your key (number)", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), text_size=15, bgcolor=ft.colors.GREY_900)
    
    #The buttons
    encrypt_b = ft.ElevatedButton(text="Encrypt", on_click=validate_data)
    decrypt_b = ft.ElevatedButton(text="Decrypt", on_click=validate_data)
    share_b = ft.IconButton(
            icon=ft.icons.SHARE,                    
            icon_size=30,
            on_click=share_by_whatsapp,
            visible=False)

    the_message = ft.Text(value="", size=18, italic=True, color=ft.colors.INDIGO_300, selectable=True)

    help_text = ft.Text(value="Enter your Message and Key, cipher or decrypt \nand share it!",  italic=True, size=16, text_align="center")
    
    #The ABOUT text
    expan = ft.ExpansionTile(
            title=ft.Text("About Caesar Cipher"),
            maintain_state=True,
            collapsed_text_color=ft.colors.GREY_500,
            controls=[
                ft.Markdown(value="In cryptography, a __CAESAR CIPHER__ is one of the simplest encryption techniques. It is a monoalphabetic rotation cipher used by Gaius Julius Caesar to send secret messages to his generals in the field. In the event that one of his messages got intercepted, his opponent could not read them. This clearly provided him with a significant strategic edge. Caesar rotated each letter of the plaintext forward three times to encrypt, so that A became D, B became E, etc._")],
            controls_padding=30,
        )

    page.add(head, 
        help_text, user_text, user_key, 
        ft.Row(controls=[encrypt_b, decrypt_b], 
            alignment="center", spacing=50,
        ),
        ft.Container(content=the_message, padding=30),
        share_b,
        expan,
    )

ft.app(target=main)
