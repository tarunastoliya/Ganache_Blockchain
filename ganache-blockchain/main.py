from flask import Flask, render_template, request, redirect,send_file
import hashlib
import endc
import contractBlock as md
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['GET', 'POST'])
def check_drm():
    # Code to check DRM
    return redirect('/check-page')

@app.route('/check-page', methods=['GET', 'POST'])
def check_page():
    if request.method == 'POST':
        image = request.files.get('image')
        image1 = Image.open(image)
        res = str(hashlib.md5((image1).tobytes()).hexdigest())
        message = md.contract.functions.sayHello(res).call()
        message = str(message)+str(', ')+ str('Text Encoded in Image : ') +str(endc.decode(image=image1))
        #return '<h1 style="width: 50%; margin-top: 20%; margin-left:20%; ">{message}</h1>'.format(message=message)
        return '<table style="width: 50%; margin: 20% auto; border: 3px solid black; border-collapse: collapse; font-size: 20px; text-align: center;">{}</table>'.format(''.join(['<tr><td style="border: 1px solid black; padding: 10px;">{}</td></tr>'.format(entry) for entry in message.split(', ')]))

    return render_template('check.html')

@app.route('/apply')
def apply_drm():
    return redirect('/apply-page')

@app.route('/apply-page', methods=['GET', 'POST'])
def apply_page():
    if request.method == 'POST':
        image = request.files.get('image')
        text = request.form.get('text')
        image = Image.open(image)
        if text != None:
            encoded_image = endc.encode(image, text)
            # Create a buffer for the modified image
            buffer = BytesIO()
            encoded_image.save(buffer, format='PNG')
            buffer.seek(0)

            # Send the buffer as a file
            return send_file(
                buffer,
                mimetype='image/png',
                download_name='processed_image.png',
                as_attachment=True
            )
       
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
