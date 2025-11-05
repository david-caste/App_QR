from flask import Flask, send_file, request, render_template
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/generate_qr')
def generate_qr():
    url = request.args.get('url')
    
    if not url:
        return "URL no proporcionada", 400

    # Generar el código QR
    img = qrcode.make(url)
    
    # Guardar la imagen en un buffer de memoria (sin necesidad de guardar en disco)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)
    
    return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, download_name='codigo_qr.png')

if __name__ == '__main__':
    app.run(debug=True)
 