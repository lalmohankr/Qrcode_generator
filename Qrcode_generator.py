import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

def generate_qr_code(data, filename='qrcode.png', size=10, border=4, color='black', bg_color='white'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=bg_color)
    img.save(filename)
    print(f"QR Code generated and saved as {filename}.")

def main():
    data = input("Enter the data or URL for the QR code: ").strip()
    if not data:
        print("Error: Data cannot be empty.")
        return
    
    filename = input("Enter the filename to save (e.g., 'my_qrcode.png'): ").strip() or 'qrcode.png'
    try:
        size = int(input("Enter the size (box size, default is 10): ").strip() or '10')
        border = int(input("Enter the border size (default is 4): ").strip() or '4')
    except ValueError:
        print("Invalid size or border. Using default values.")
        size = 10
        border = 4

    color = input("Enter the QR code color (default is 'black'): ").strip() or 'black'
    bg_color = input("Enter the background color (default is 'white'): ").strip() or 'white'

    generate_qr_code(data, filename, size, border, color, bg_color)

if __name__ == "__main__":
    main()
