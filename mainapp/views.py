# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document, DocumentClassification
from .forms import DocumentForm, ClassificationForm
from neuralnetwork import get


def list(request):
    documents = get_lastest_documents()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'], day_score = get(request.FILES['docfile']))
            newdoc.save()
        return HttpResponseRedirect(reverse('mainapp.views.detail', kwargs={'image_id':newdoc.id}))
    else:
        form = DocumentForm()

    return render_to_response(
        'index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def detail(request, image_id):
    document = Document.objects.get(id=image_id)
    documents = get_lastest_documents()
    ip = get_client_ip(request)
    submited_value = check_if_already_submited_value(document, ip)

    if request.method == 'POST' and not submited_value:
        form = ClassificationForm(request.POST)
        if form.is_valid():
            submited_value = True
            score = request.POST.getlist('choice_field')[0]
            classification = DocumentClassification(document=document, score=score, ip=ip)
            classification.save()
    else:
        form = ClassificationForm()

    return render_to_response(
        'detail.html',
        {'documents': documents, 'form': form, 'image':document, "submited_value":submited_value},
        context_instance=RequestContext(request)
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_lastest_documents(last=5):
    return Document.objects.all().order_by('-created_at')[:last]

def check_if_already_submited_value(document, ip):
    return len(DocumentClassification.objects.filter(document=document).filter(ip=ip)) != 0
