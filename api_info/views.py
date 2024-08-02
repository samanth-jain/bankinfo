# banks/views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import BankSerializer
from .models import Bank

#API view to get all the Bank lists
class BankListView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

#API view to get all the Banks from the bank name POST request
class Bank_SearchView(APIView):
    def post(self, request):
        bank_name = request.data.get('bank_name', None)
        
        if not bank_name:
            return Response({"error": "Bank name not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        banks = Bank.objects.filter(bank_name__iexact=bank_name)  #Case-insensitive filtering
        
        if not banks.exists():
            return Response({"error": "bank not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

#API view to get all the Banks from the branch name POST request
class Branch_SearchView(APIView):
    def post(self, request):
        branch_name = request.data.get('branch_name', None)
        
        if not branch_name:
            return Response({"error": "Branch name not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        branches = Bank.objects.filter(branch__iexact=branch_name)  #Case-insensitive filtering
        
        if not branches.exists():
            return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BankSerializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
