from TestWork.celery import app
from .models import File
from django.shortcuts import get_object_or_404

@app.task
def file_handler(id):
    file = get_object_or_404(File, id=id)
    file.processed = True
    file.save(update_fields=['processed'])