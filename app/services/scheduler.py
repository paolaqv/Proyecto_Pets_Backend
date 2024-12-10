from apscheduler.schedulers.background import BackgroundScheduler
import atexit

_scheduler = None  # Variable global para gestionar la instancia del scheduler

def iniciar_scheduler():
    global _scheduler

    if _scheduler is None:  # Solo inicializar si no existe
        from app.services.notificacion_service import NotificacionService

        scheduler = BackgroundScheduler()
        scheduler.add_job(
            NotificacionService.enviar_notificaciones_automaticas,
            'interval',
            minutes=1,
            id='enviar_notificaciones',
            replace_existing=True
        )

        scheduler.start()
        print("Scheduler iniciado.")

        # Registrar para apagado seguro
        atexit.register(lambda: scheduler.shutdown(wait=False))
        _scheduler = scheduler  # Guardar la instancia del scheduler
    return _scheduler
