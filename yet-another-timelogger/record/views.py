from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from record.models import Record
from django.forms import ModelForm, DateTimeField, widgets
from datetime import datetime
from django import forms


class RecordForm(ModelForm):
    start_time = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        initial="2008-12-01 12:03",
        widget=forms.DateTimeInput(attrs={
            'class': 'start_time datetime_picker',
            'id': 'start_time_id'
        }))

    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        initial="2008-12-01 12:03",
        widget=forms.DateTimeInput(attrs={
            'class': 'end_time datetime_picker',
            'id': 'end_time_id'
        }))

    class Meta:
        model = Record
        fields = ['action', 'start_time', 'end_time']


@login_required
def record(request):
    form = RecordForm()
    queryset = Record.objects.all()[:10]
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # db is changed
            queryset = Record.objects.all()[:10]
            return render(request, 'record/record.html', {
                'form': form,
                'queryset': queryset
            })
        else:
            return HttpResponse(status=400)

    return render(request, 'record/record.html', {
        'form': form,
        'queryset': queryset
    })


@login_required
def delete(request, part_id):
    object = Record.objects.get(pk=part_id)
    if object:
        object.delete()
    return HttpResponseRedirect(reverse("record"))
