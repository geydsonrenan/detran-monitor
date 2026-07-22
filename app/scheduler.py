from apscheduler.schedulers.blocking import BlockingScheduler
from app.monitor import Monitor

def iniciar():
    monitor = Monitor()

    scheduler = BlockingScheduler()

    scheduler.add_job(
        monitor.verificar,
        "interval",
        seconds=30,
        max_instances=1,
        coalesce=True
    )

    monitor.verificar()

    scheduler.start()