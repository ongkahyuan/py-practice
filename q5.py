import pandas as pd
import numpy as np
from datetime import datetime

class q5:

    def __init__(self):
        self.customers = pd.read_csv("data/customers.csv")
        self.order_items = pd.read_csv("data/order_items.csv")
        self.order_payments = pd.read_csv("data/order_payments.csv")
        self.order_reviews = pd.read_csv("data/order_reviews.csv")
        self.orders = pd.read_csv("data/orders.csv")
        self.prd_translation = pd.read_csv("data/product_category_name_translation.csv")
        self.products = pd.read_csv("data/products.csv")
        self.sellers = pd.read_csv("data/sellers.csv")

    #part 1: join order reviews with order items with sellers, then summarize by review score
    def part_one(self):
        merge_one = pd.merge(self.order_reviews, self.order_items, how="left", on="order_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")
        review_scores = merge_two.groupby(by="seller_id").agg({"review_score":[np.mean]})
        return review_scores.nlargest(10,("review_score","mean"))[("review_score","mean")].rename("avg_review_score")

    #part 2: join order items with products (on product_id), join with translation, then group by product_name agg by sales revenue.
    def part_two(self):
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.prd_translation, how="left", on="product_category_name")
        group_agg = merge_two.groupby(by="product_category_name_english").count()
        return group_agg.nlargest(10,"order_id")["order_id"].rename("sales")

    #part 3: same as part 2, but agg by sum of price and find the first and last dates in the order_items list
    def part_three(self):
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")
        group_agg = merge_two.groupby(by="seller_id").agg({"price":"sum"})
        total_rev = group_agg.nlargest(10,"price")["price"].rename("total_rev")
        avg_rev_dict = {}
        
        for seller, rev in total_rev.items():
            days = self.find_seller_duration(seller)
            avg_rev_seller = rev/days
            avg_rev_dict[seller] = avg_rev_seller

        avg_rev = pd.Series(data=avg_rev_dict)
        return avg_rev.rename("avg_rev_seller_day")

    #part 4: join order items with sellers and prodcuts, group by seller state, find first and last dates in order_items for each state
    def part_four(self):
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")
        group_agg = merge_two.groupby(by="seller_state").agg({"price":"sum"})
        total_rev = group_agg["price"].rename("total_rev")
        avg_rev_dict = {}
        
        for state, rev in total_rev.items():
            months = self.find_state_duration(state)
            avg_rev_seller = rev/months
            avg_rev_dict[state] = avg_rev_seller

        avg_rev = pd.Series(data=avg_rev_dict)
        return avg_rev.rename("avg_rev_state_month")

    #part 5: find the combination of product category and state that yields the highest profit
    def part_five(self):
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")
        merge_three = pd.merge(merge_two, self.prd_translation, how="left", on="product_category_name")
        add_profit = merge_three.assign(profit = lambda x: x.price - x.freight_value)
        grouped = add_profit.groupby(by=["seller_state","product_category_name_english"]).agg({"profit":"sum", "shipping_limit_date":"max", "shipping_limit_date":"min"})
        return grouped

    #Helper functions

    def find_state_duration(self, seller_state):
        items = pd.merge(self.order_items, self.sellers, how="left", on="seller_id")
        dates = items.loc[items["seller_state"] == seller_state, "shipping_limit_date"]
        first = datetime.strptime(dates.min(), "%Y-%m-%d %H:%M:%S")
        last = datetime.strptime(dates.max(), "%Y-%m-%d %H:%M:%S")

        #Here, it is assumed that each state entered the market for at least a month
        months_between = (last.year-first.year)*12 + last.month-first.month 
        if months_between == 0 or type(months_between) == type(None):
            months_between +=1
        return months_between

    def find_seller_duration(self, seller_id):
        items = self.order_items
        dates = items.loc[items["seller_id"] == seller_id, "shipping_limit_date"]
        first = datetime.strptime(dates.min(), "%Y-%m-%d %H:%M:%S")
        last = datetime.strptime(dates.max(), "%Y-%m-%d %H:%M:%S")
        return (last-first).days

if __name__ == "__main__":
    d = q5()
    # print(d.part_one())
    # print(d.part_two())
    # print(d.part_four())
    print(d.part_five())