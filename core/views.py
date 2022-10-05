from django.shortcuts import redirect, render
from django.template import RequestContext
from .models import Area, Experience, Form
from .forms import FormForm, AreaForm, ExperienceForm
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateResponse
from pdf2docx import Converter
from django.http import FileResponse

@login_required(login_url='/login')
def area(request, pk):
    obj = Form.objects.get(id=pk)
    return render(request, 'core/area.html', {'obj': obj})


@login_required(login_url='/login')
def experience(request, pk):
    obj = Form.objects.get(id=pk)
    return render(request, 'core/experience.html', {'obj': obj})


@login_required(login_url='/login')
def add_experience(request, pk):
    obj = Form.objects.get(id=pk)
    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        form.save(commit=False)
        form.instance.form = obj
        form.save()
        return redirect('home')
    return render(request, 'core/add_experience.html', {'form': form})


@login_required(login_url='/login')
def delete_experience(request, pk):
    experience = Experience.objects.get(id=pk)
    if request.method == 'POST':
        experience.delete()
        return redirect('home')
    return render(request, 'core/delete-experience.html')


@login_required(login_url='/login')
def edit_experience(request, pk):
    area = Experience.objects.get(id=pk)
    form = ExperienceForm(instance=area)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=area)
        form.save()
        return redirect('home')
    return render(request, 'core/edit_experience-form.html', {'form': form})


@login_required(login_url='/login')
def add_area(request, pk):
    obj = Form.objects.get(id=pk)
    form = AreaForm()
    if request.method == 'POST':
        form = AreaForm(request.POST)
        form.save(commit=False)
        form.instance.form = obj
        form.save()
        return redirect('home')
    return render(request, 'core/add_area-form.html', {'form': form})


@login_required(login_url='/login')
def edit_area(request, pk):
    area = Area.objects.get(id=pk)
    form = AreaForm(instance=area)
    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        form.save()
        return redirect('home')
    return render(request, 'core/edit_area-form.html', {'form': form})


@login_required(login_url='/login')
def delete_area(request, pk):
    area = Area.objects.get(id=pk)
    if request.method == 'POST':
        area.delete()
        return redirect('home')
    return render(request, 'core/delete-area.html')


def pdf(request, pk):
    form = Form.objects.get(id=pk)
    context = RequestContext(request)
    template = 'core/pdf.html'
    

    context = {
        'form': form,

    }
    footer = '/home/grzegorz/crm_test/crm/core/templates/core/header.html'
    if form.logo == 'TAK':
        return PDFTemplateResponse(
            request=request,
            cmd_options={
                'quiet': True,
                'header-html': '/home/grzegorz/crm_test/crm/core/templates/core/header.html',
                'footer-html': '/home/grzegorz/crm_test/crm/core/templates/core/footer.html',

            },
            
            template=template,
            context=context,
            
        )
    if form.logo == 'NIE':
        return PDFTemplateResponse(
            request=request,
            cmd_options={
                'quiet': True,
                'header-html': '/home/grzegorz/crm_test/crm/core/templates/core/header_logo.html',
                'footer-html': '/home/grzegorz/crm_test/crm/core/templates/core/footer.html',
        
            },
            
            template=template,
            context=context,
            
        )
        
        



@login_required(login_url='/login')
def docx(request, pk):
    form = Form.objects.get(id=pk)
    context = RequestContext(request)
    template = 'core/pdf.html'
    filename = 'my_pdf.pdf'

    context = {
        'form': form,

    }
    footer = '/home/grzegorz/crm_test/crm/core/templates/core/footer.html'
    if form.logo == 'TAK':
        response = PDFTemplateResponse(
            request=request,
            cmd_options={
                'quiet': True,
                'header-html': '/home/grzegorz/crm_test/crm/core/templates/core/header.html',
                'footer-html': '/home/grzegorz/crm_test/crm/core/templates/core/footer.html',

            },

            template=template,
            context=context,

        )
        with open("file.pdf", "wb") as f:
            f.write(response.rendered_content)

        pdf_file = 'file.pdf' 
        docx_file = 'file.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        response = FileResponse(open('file.docx', 'rb'))

        return response

    if form.logo == 'NIE':
        response = PDFTemplateResponse(
            request=request,
            cmd_options={
                'quiet': True,
                'header-html': '/home/grzegorz/crm_test/crm/core/templates/core/header_logo.html',
                'footer-html': '/home/grzegorz/crm_test/crm/core/templates/core/footer.html',

            },

            template=template,
            context=context,

        )
        with open("file.pdf", "wb") as f:
            f.write(response.rendered_content)

        pdf_file = 'file.pdf' 
        docx_file = 'file.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        response = FileResponse(open('file.docx', 'rb'))

    return response

@login_required(login_url='/login')
def home(request):
    user = request.user
    if user.is_superuser:
        form = Form.objects.all()
    else:
        form = Form.objects.filter(author=user)
    form_count = Form.objects.filter(author=request.user).count()
    return render(request, 'core/home.html', {
        'forms': form,
        'form_count': form_count,
    })


@login_required(login_url='/login')
def add_form(request):
    form = FormForm
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('home')
    return render(request, 'core/new-form.html', {
        'form': form,
    })


@login_required(login_url='/login')
def edit_form(request, pk):
    obj = Form.objects.get(id=pk)
    form = FormForm(instance=obj)
    if request.method == 'POST':
        form = FormForm(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('home')
    return render(request, 'core/edit-form.html', {
        'form': form,
    })


@login_required(login_url='/login')
def remove_form(request, pk):
    form = Form.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('home')
    return render(request, 'core/delete-form.html', {
        'form': form,
    })
