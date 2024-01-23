from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def register_new_item(file_path, new_id, name, size, date, address, custom, condition):
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["ID", "Name", "Size", "Date", "Address", "Custom", "Condition"])

    if new_id in df["ID"].values:
        return False  # ID already exists
    new_item = {"ID": new_id, "Name": name, "Size": size, "Date": date, "Address": address, "Custom": custom, "Condition": condition}
    df = df.append(new_item, ignore_index=True)
    df.to_excel(file_path, index=False)
    return True

def get_item_info(file_path, item_id):
    try:
        df = pd.read_excel(file_path)
        item_info = df[df['ID'] == item_id].to_dict(orient='records')[0]
        return item_info
    except FileNotFoundError:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    file_path = "items_registry.xlsx"
    new_id = request.form['id']
    name = request.form['name']
    size = request.form['size']
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    address = request.form['address']
    custom = request.form['custom']
    condition = request.form['condition']

    if register_new_item(file_path, new_id, name, size, date, address, custom, condition):
        return redirect(url_for('index'))
    else:
        return "Item with this ID already exists!"

@app.route('/item/<int:item_id>')
def item(item_id):
    file_path = "items_registry.xlsx"
    item_info = get_item_info(file_path, item_id)

    if item_info:
        return render_template('item.html', item_info=item_info)
    else:
        return "Item not found!"

if __name__ == '__main__':
    app.run(debug=True)
