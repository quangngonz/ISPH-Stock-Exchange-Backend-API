from django.db import models

class Users(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    house = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Stocks(models.Model):
    stock_ticker = models.CharField(max_length=3, primary_key=True)
    stock_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    current_price = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.stock_ticker

class StockPriceHistory(models.Model):
    price_history_id = models.CharField(max_length=50, primary_key=True)
    stock_ticker = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    price = models.FloatField()
    timestamp = models.DateTimeField()

class Portfolios(models.Model):
    portfolio_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    points_balance = models.IntegerField()

class PortfolioItems(models.Model):
    portfolio_item_id = models.CharField(max_length=50, primary_key=True)
    portfolio = models.ForeignKey(Portfolios, on_delete=models.CASCADE)
    stock_ticker = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Transactions(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]
    transaction_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    stock_ticker = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField()

class Earnings(models.Model):
    earning_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    points = models.IntegerField()
    code = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
