from rest_framework.routers import DefaultRouter
from .views import (UsersViewSet, StocksViewSet, StockPriceHistoryViewSet,
                    PortfoliosViewSet, PortfolioItemsViewSet, TransactionsViewSet, EarningsViewSet)

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'stocks', StocksViewSet)
router.register(r'price-history', StockPriceHistoryViewSet)
router.register(r'portfolios', PortfoliosViewSet)
router.register(r'portfolio-items', PortfolioItemsViewSet)
router.register(r'transactions', TransactionsViewSet)
router.register(r'earnings', EarningsViewSet)

urlpatterns = router.urls
