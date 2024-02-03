from rest_framework.response import Response



class CustomListModelMixin:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        """
        this is a list 


        this shows the list of an object 
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)