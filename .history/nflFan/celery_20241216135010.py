from celery.schedules import crontab

app.conf.beat_schedule = {
    'update-playgame-data-every-wednesday': {
        'task': 'nflFan.tasks.update_playgame_display',
        'schedule': crontab(minute=0, hour=0, day_of_week=3),  # Chaque mercredi à minuit
    },
}
