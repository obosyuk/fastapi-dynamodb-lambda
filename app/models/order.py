class OrderModel:
    def __init__(self, id: str, user_id: str, total_price: float, status: str):
        self.id = id
        self.user_id = user_id
        self.total_price = total_price
        self.status = status
