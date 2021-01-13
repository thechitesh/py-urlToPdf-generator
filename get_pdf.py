import sys
import generate_pdf


url = sys.argv[1]
save_pdf_path = sys.argv[2]
chrome_driver_path = r'<path-to-chrome-driver>'
wait_time = '120'
print('passed values ', sys.argv)

result = generate_pdf.get_pdf_from_url(url, chrome_driver_path, wait_time)

with open(save_pdf_path, 'wb') as file:
    file.write(result)
    print('generate pdf file is saved at ', save_pdf_path)
