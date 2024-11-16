import psutil
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    Message = None

    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)

    if  cpu_percent > 80 or mem_percent > 80:
     Message = "high CPU or Memory Utiliazation detected, Plese scale up"

    #return f"CPU Utilization: {cpu_percent} and Memory Utilization: {mem_percent}"

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
    