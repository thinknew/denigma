from django.contrib import admin
from django.db import models
from django import forms

import reversion
from pagedown.widgets import AdminPagedownWidget

from models import Entry, Change, Relation, Alteration, Category, Tag


#class ChangeInline(admin.StackedInline):
#    model = Change
#    fk_name = 'of'
#
#class RelationInline(admin.StackedInline):
#    model = Relation
#    fk_name = 'fr'
#    def save_model(self, request, obj, form, change):
#        obj.user = request.user
#        obj.request = request
#        obj.save()


class EntryAdminForm(forms.ModelForm):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    text = forms.CharField(widget=AdminPagedownWidget(
        attrs={'rows': 30, 'cols': 80, 'style': 'font-family:monospace'}),
        help_text='<a href="http://docutils.sourceforge.net/docs/user/rst/'
                  'quickref.html">reStructuredText Quick Reference</a>'
    )


class EntryAdmin(reversion.VersionAdmin):
    search_fields = ('title', 'text', 'url')
    ordering = ('-created',)
    list_filter = ('published',)
    #inlines = [ChangeInline]
    #inlines = [RelationInline]
    form = EntryAdminForm

    def save_model(self, request, obj, form, change):
        print("EntryAdmin.save_model here!")
        obj.user = request.user
        obj.request = request
        obj.save()


class RelationAdmin(reversion.VersionAdmin):
    ordering = ('-created',)
    def save_model(self, request, obj, form, change):
        print("RelationAdmin.save_model here!")
        obj.user = request.user
        obj.save()


class ChangeAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    ordering  = ('-at',)
    list_filter = ('by',)


class AlterationAdmin(admin.ModelAdmin):
    ordering = ('at',)


class CategoryAdmin(reversion.VersionAdmin):
    ordering = ('name',)


class TagAdmin(reversion.VersionAdmin):
    ordering = ('name',)


admin.site.register(Entry, EntryAdmin)
admin.site.register(Change, ChangeAdmin)
admin.site.register(Relation, RelationAdmin)
admin.site.register(Alteration, AlterationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)