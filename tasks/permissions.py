from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Permissões são permitidas apenas ao autor da tarefa
        return obj.owner == request.user
