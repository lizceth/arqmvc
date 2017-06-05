from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from app.models import Cliente, Pedido

class ClienteForm(forms.ModelForm):
     class Meta:
         model = Cliente
         fields = ("nombres", "telefono")
    
     def __init__(self, *args, **kwargs):
        super(ClienteForm,
              self).__init__(*args, **kwargs)    
        self.fields['nombres'] = forms.CharField(
            label=capfirst(_(u'Nombres')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

class PedidoForm(forms.ModelForm):
     class Meta:
         model = Pedido
         fields = ('descripcion', 'cliente')
     def __init__(self, *args, **kwargs):
        super(PedidoForm,
               self).__init__(*args, **kwargs)    
        self.fields['fecha'] = forms.CharField(
            label=capfirst(_(u'Fecha')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
         # self.fields['solution'] = forms.ModelChoiceField(
         #    label=capfirst(_(u'Solution')), required=True,
         #    queryset=Solution.objects.filter(is_active=True),
         #    help_text=u'<small class="help-error"></small> %s' % _(
         #        u' '),
         # )