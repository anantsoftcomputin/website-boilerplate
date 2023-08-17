from django.contrib import admin

from .api import chat_with_gpt3
from .models import Interaction


class InteractionAdmin(admin.ModelAdmin):
    actions = ['get_bot_response']
    list_display = ('user_input', 'bot_response', 'timestamp')
    search_fields = ('user_input', 'bot_response', 'timestamp')

    def get_bot_response(modeladmin, request, queryset):
        for interaction in queryset:
            response = chat_with_gpt3(interaction.user_input)
            interaction.bot_response = response
            interaction.save()

admin.site.register(Interaction, InteractionAdmin)