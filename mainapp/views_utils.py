from .models import Document, DocumentClassification

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_lastest_documents(last=4):
    return Document.objects.all().order_by('-created_at')[:last]


def check_if_submited_list(documents, ip):
    return {doc:check_if_submited(doc, ip) for doc in documents}

def check_if_submited(document, ip):
    document_submitions = DocumentClassification.objects.filter(document=document).filter(ip=ip).order_by("created_at")
    if not document_submitions:
        return False
    else:
        return document_submitions[0]
