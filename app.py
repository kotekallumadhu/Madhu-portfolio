from flask import Flask, render_template, request, redirect, send_file, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash('Thank you for your message!')
        # Here you can add logic to send/store the message
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return send_file("static/Kotekallu_Madhu_Resume.pdf", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
