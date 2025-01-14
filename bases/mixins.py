from rest_framework.exceptions import ValidationError


class FilterByFieldsMixin:
    filter_fields = []

    def filter_queryset(self, queryset):
        request_filters = {}
        for field in self.filter_fields:
            if field in self.request.query_params:
                request_filters[field] = self.request.query_params.get(field)
        
        if not request_filters:
            return queryset 
        
        try:
            return queryset.filter(**request_filters)
        except Exception as e:
            raise ValidationError({"detail": f"Erro ao filtrar: {str(e)}"})

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_queryset(queryset)
