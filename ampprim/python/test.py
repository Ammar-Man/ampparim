{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (3.0.0)\n",
      "Requirement already satisfied: pandas in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (1.5.2)\n",
      "Requirement already satisfied: openpyxl in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (3.1.2)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from flask) (3.0.0)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from flask) (3.1.2)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from flask) (2.1.2)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from flask) (8.1.3)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from flask) (1.6.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from pandas) (2022.6)\n",
      "Requirement already satisfied: numpy>=1.21.0 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from pandas) (1.23.5)\n",
      "Requirement already satisfied: et-xmlfile in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from openpyxl) (1.1.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\admin\\appdata\\roaming\\python\\python310\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\admin\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\admin\\appdata\\roaming\\python\\python310\\site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 23.3.1 -> 23.3.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install flask pandas openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, redirect, url_for\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "def register_new_item(file_path, new_id, name, size, date, address, custom, condition):\n",
    "    try:\n",
    "        df = pd.read_excel(file_path)\n",
    "    except FileNotFoundError:\n",
    "        df = pd.DataFrame(columns=[\"ID\", \"Name\", \"Size\", \"Date\", \"Address\", \"Custom\", \"Condition\"])\n",
    "\n",
    "    if new_id in df[\"ID\"].values:\n",
    "        return False  # ID already exists\n",
    "    new_item = {\"ID\": new_id, \"Name\": name, \"Size\": size, \"Date\": date, \"Address\": address, \"Custom\": custom, \"Condition\": condition}\n",
    "    df = df.append(new_item, ignore_index=True)\n",
    "    df.to_excel(file_path, index=False)\n",
    "    return True\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/add_item', methods=['POST'])\n",
    "def add_item():\n",
    "    file_path = \"items_registry.xlsx\"\n",
    "    new_id = request.form['id']\n",
    "    name = request.form['name']\n",
    "    size = request.form['size']\n",
    "    date = datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n",
    "    address = request.form['address']\n",
    "    custom = request.form['custom']\n",
    "    condition = request.form['condition']\n",
    "\n",
    "    if register_new_item(file_path, new_id, name, size, date, address, custom, condition):\n",
    "        return redirect(url_for('index'))\n",
    "    else:\n",
    "        return \"Item with this ID already exists!\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
