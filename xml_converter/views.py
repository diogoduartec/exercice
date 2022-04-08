from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.forms import UploadXMLForm
from xml_converter.tools import convert_from_xml_to_dict


def upload_page(request):
    if request.method == 'POST':
        form = UploadXMLForm(request.POST, request.FILES)
        if form.is_valid():
            file_converted = convert_from_xml_to_dict(request.FILES['file'])
            return JsonResponse(file_converted)
    return render(request, "upload_page.html")
