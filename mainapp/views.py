# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document, DocumentClassification
from .forms import DocumentForm, ClassificationForm
from .views_utils import get_client_ip, get_lastest_documents, check_if_submited_list
from neuralnetwork import get

import imghdr


def upload(request):
    ip = get_client_ip(request)

    documents = get_lastest_documents()

    documents_submitions = check_if_submited_list(list(documents), ip)

    wrong_file = False

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'], day_score = get(request.FILES['docfile']))
            newdoc.save()
            return HttpResponseRedirect(reverse('mainapp.views.detail', kwargs={'document_id':newdoc.id}))

    form = DocumentForm()

    return render(request, 'upload.html', {'documents': documents_submitions.items(), 'form': form, 'wrong_file':wrong_file})


def detail(request, document_id):
    ip = get_client_ip(request)

    document = Document.objects.get(id=document_id)
    documents = get_lastest_documents()

    documents_submitions = check_if_submited_list(list(documents)+[document], ip)

    if request.method == 'POST' and not documents_submitions[document]:
        form = ClassificationForm(request.POST)
        if form.is_valid():
            documents_submitions[document] = True
            score = request.POST.getlist('choice_field')[0]
            classification = DocumentClassification(document=document, score=score, ip=ip)
            classification.save()
    else:
        form = ClassificationForm()

    document_info = (document, documents_submitions[document])
    return render(request, 'detail.html', {'documents': documents_submitions.items(), 'form': form, 'document':document_info})

