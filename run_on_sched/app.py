from chalice import Chalice

app = Chalice(app_name='run_on_sched')


@app.schedule('cron(0 0 * * *)')
def daily_task():
    print("Running daily task at midnight")

