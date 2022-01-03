from config.database import Database

class OrderService:

    def __init__(self):
        self.db = Database()

    def list(self, member_idx):
        try:
            query = 'SELECT \
                        order_no, \
                        product_name, \
                        order_price, \
                        order_datetime, \
                        pay_datetime \
                    FROM \
                        Orders \
                    WHERE \
                        member_idx = %(member_idx)s \
                    ORDER BY order_datetime DESC'
            param = {
                'member_idx': member_idx
            }

            result = self.db.executeAll(query, param)
            return result
        except Exception as e:
            return e
    
    def getLastOrder(self, member_idx):
        try:
            query = 'SELECT \
                        order_no, \
                        product_name, \
                        order_price, \
                        order_datetime, \
                        pay_datetime \
                    FROM \
                        Orders \
                    WHERE \
                        member_idx = %(member_idx)s \
                    ORDER BY order_datetime DESC \
                    LIMIT 1'
            param = {
                'member_idx': member_idx
            }

            result = self.db.executeOne(query, param)
            return result
        except Exception as e:
            return None