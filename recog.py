from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'path-to-your-directory'  # Adjust the path as necessary

def imstr():
    print(pytesseract.image_to_string(Image.open('test.png')))  # Simple image to string

def imbox():
    print(pytesseract.image_to_boxes(Image.open('test.png')))  # Get bounding box estimates

def imdata():
    print(pytesseract.image_to_data(Image.open('test.png')))  # Get verbose data including boxes, confidences, line and page numbers

def imori():
    print(pytesseract.image_to_osd(Image.open('test.png')))  # Get information about orientation and script detection

def impdf():
    pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')  # Get a searchable PDF
    with open('test.pdf', 'wb') as f:
        f.write(pdf)  # pdf type is bytes by default
    print("PDF saved as 'test.pdf'.")

def imhocr():
    hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')
    with open('output.hocr', 'wb') as f:
        f.write(hocr)
    print("HOCR saved as 'output.hocr'.")

def imxml():
    xml = pytesseract.image_to_alto_xml('test.png')  # Get ALTO XML output
    with open('output.xml', 'w') as f:
        f.write(xml)
    print("ALTO XML saved as 'output.xml'.")

def imtxt():
    text, boxes = pytesseract.run_and_get_multiple_output('test.png', extensions=['txt', 'box'])
    with open('output.txt', 'w') as f:
        f.write(text)
    print("Text saved as 'output.txt'.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Extract text from image")
        print("2. Get bounding box estimates")
        print("3. Get detailed data")
        print("4. Get orientation and script detection")
        print("5. Create a searchable PDF")
        print("6. Get HOCR output")
        print("7. Get ALTO XML output")
        print("8. Get multiple outputs (text and boxes)")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            imstr()
        elif choice == '2':
            imbox()
        elif choice == '3':
            imdata()
        elif choice == '4':
            imori()
        elif choice == '5':
            impdf()
        elif choice == '6':
            imhocr()
        elif choice == '7':
            imxml()
        elif choice == '8':
            imtxt()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
