from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>BMI 计算器</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="number"] {
            width: 200px;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>BMI 计算器</h1>
        <form method="POST">
            <div class="form-group">
                <label>身高 (厘米):</label>
                <input type="number" step="0.1" name="height" required min="1" value="{{height}}">
            </div>
            <div class="form-group">
                <label>体重 (公斤):</label>
                <input type="number" step="0.1" name="weight" required min="1" value="{{weight}}">
            </div>
            <button type="submit">计算 BMI</button>
        </form>
        {% if bmi %}
        <div class="result" style="background-color: {{color}}">
            <h2>您的 BMI: {{bmi}}</h2>
            <p>身体状况: {{category}}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = ''
    color = ''
    height = ''
    weight = ''
    
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        
        # 计算 BMI
        bmi = weight / ((height/100) ** 2)
        bmi = round(bmi, 1)
        
        # 判断身体状况
        if bmi < 18.5:
            category = '体重过轻'
            color = '#FFE4C4'
        elif 18.5 <= bmi < 24:
            category = '体重正常'
            color = '#98FB98'
        elif 24 <= bmi < 28:
            category = '超重'
            color = '#FFA07A'
        else:
            category = '肥胖'
            color = '#FF6B6B'
    
    return render_template_string(
        HTML_TEMPLATE, 
        bmi=bmi,
        category=category,
        color=color,
        height=height,
        weight=weight
    )

if __name__ == '__main__':
    app.run(debug=True)