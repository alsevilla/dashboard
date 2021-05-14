from django import forms
from .models import *
#data input
#facebook
    #facebook page info
class fb_page_info_Form(forms.ModelForm):

    class Meta:
        model = fb_page_info
        fields = "__all__"
    #end facebook page info
    #facebook post data
class fb_post_data_Form(forms.ModelForm):

    class Meta:
        model = fb_post_data
        fields = "__all__"
    #end facebook post data
    #facebook post comments
#end facebook
#philrice text center
class ptc_Form(forms.ModelForm):

    class Meta:
        model = ptc
        fields = "__all__"
# end philrice text center
#philrice website
class pw_Form(forms.ModelForm):

    class Meta:
        model = pw
        fields = "__all__"

class pw_visitor_Form(forms.ModelForm):

    class Meta:
        model = pw_visitor
        fields = "__all__"
#end philrice website
#Pinoy Rice
class pr_visitor_Form(forms.ModelForm):

    class Meta:
        model = pr_visitor
        fields = "__all__"

class pr_upload_Form(forms.ModelForm):

    class Meta:
        model = pr_upload
        fields = "__all__"
#end Pinoy Rice
#radio
class radio_visitor_Form(forms.ModelForm):

    class Meta:
        model = radio_visitor
        fields = "__all__"
class radio_upload_Form(forms.ModelForm):

    class Meta:
        model = radio_upload
        fields = "__all__"
#end radio
#kp

class kp_input_Form(forms.ModelForm):

    class Meta:
        model = kp_input
        fields = "__all__"

class kp_input_stock_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(kp_input_stock_Form, self).__init__(*args, **kwargs)
        self.fields['kp'].queryset = self.fields['kp'].queryset.exclude(title="-")

    class Meta:
        model = kp_input_stock
        fields = "__all__"

class kp_request_Form(forms.ModelForm):

    class Meta:
        model = kp_request
        fields = "__all__"

class kp_distribute_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(kp_distribute_Form, self).__init__(*args, **kwargs)
        self.fields['Kp'].queryset = self.fields['Kp'].queryset.exclude(title="-")

    class Meta:
        model = kp_distribute
        fields = "__all__"


#end kp
#partners
class partners_Form(forms.ModelForm):

    class Meta:
        model = partners
        fields = "__all__"
#end_partners
#intermediaries
class intermediaries_Form(forms.ModelForm):

    class Meta:
        model = intermediaries
        fields = "__all__"
#end intermediaries
#DevCom
    #projprog
class progproj_Form(forms.ModelForm):

    class Meta:
        model = progproj
        fields = "__all__"
    #end projprog
    #publication
class publication_Form(forms.ModelForm):

    class Meta:
        model = publication
        fields = "__all__"
    #end publication
    #awards
class awards_Form(forms.ModelForm):

    class Meta:
        model = awards
        fields = "__all__"
    #end awards
    #staff
class staff_Form(forms.ModelForm):

    class Meta:
        model = staff
        fields = "__all__"
    #end staff
#end data input
