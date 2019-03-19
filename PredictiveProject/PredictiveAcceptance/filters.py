from PredictiveAcceptance.models import UniversityNames
import django_filters

class UnviersityNamesFilter(django_filters.FilterSet):
    class Meta:
        model = UniversityNames
        fields = {
            'university_code': ['exact', ],
            'university_name': ['icontains', ],
        }