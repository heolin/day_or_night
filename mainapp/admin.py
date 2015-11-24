from django.contrib import admin

from .models import Document, DocumentClassification

admin.site.register(Document)
admin.site.register(DocumentClassification)
