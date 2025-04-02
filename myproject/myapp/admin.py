from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)

    def get_model_perms(self, request):
        """Modifie les permissions pour masquer l'application et afficher directement le modèle"""
        perms = super().get_model_perms(request)
        if perms:
            return {'add': perms['add'], 'change': perms['change'], 'delete': perms['delete']}
        return {}

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
