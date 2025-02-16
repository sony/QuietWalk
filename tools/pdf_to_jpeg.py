from pdf2image import convert_from_path

pdf_path = "/home/0000104070/workspace/aibo_walk_web/static/pdfs/fig1.pdf"
poppler_path = "/usr/bin"  # Change this to your Poppler path

images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

for i, image in enumerate(images):
    image.save(f"output_page_{i+1}.jpg", "JPEG")
