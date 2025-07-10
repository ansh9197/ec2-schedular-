from flask import Flask, render_template, request, redirect, url_for, flash
from scheduler import schedule_start, schedule_stop, run_scheduler, list_instances
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    instances = list_instances()
    return render_template('index.html', instances=instances)

@app.route('/schedule', methods=['POST'])
def schedule():
    instance_id = request.form['instance_id']
    start_time = request.form['start_time']
    stop_time = request.form['stop_time']

    if not instance_id or not start_time or not stop_time:
        flash("Please fill all fields.", "danger")
        return redirect(url_for('index'))

    schedule_start(instance_id, start_time)
    schedule_stop(instance_id, stop_time)

    flash(f"Scheduled {instance_id} start at {start_time} and stop at {stop_time}.", "success")

    threading.Thread(target=run_scheduler, daemon=True).start()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)