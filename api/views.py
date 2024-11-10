from rest_framework import viewsets
from .models import Users, Stocks, StockPriceHistory, Portfolios, PortfolioItems, Transactions, Earnings
from .serializers import (UsersSerializer, StocksSerializer, StockPriceHistorySerializer,
                          PortfoliosSerializer, PortfolioItemsSerializer, TransactionsSerializer, EarningsSerializer)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class StocksViewSet(viewsets.ModelViewSet):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer

class StockPriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = StockPriceHistory.objects.all()
    serializer_class = StockPriceHistorySerializer

class PortfoliosViewSet(viewsets.ModelViewSet):
    queryset = Portfolios.objects.all()
    serializer_class = PortfoliosSerializer

class PortfolioItemsViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItems.objects.all()
    serializer_class = PortfolioItemsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

class EarningsViewSet(viewsets.ModelViewSet):
    queryset = Earnings.objects.all()
    serializer_class = EarningsSerializer
