from django.contrib import admin
from chat.models import Conversation, Message


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_group')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'text', 'img', 'date', 'status')
    search_fields = ('text', )


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
