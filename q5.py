import pandas as pd
import numpy as np

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


    def part_one(self):
        #Join order reviews and sellers to order items
        merge_one = pd.merge(self.order_reviews, self.order_items, how="left", on="order_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")
        
        #Group according to sellers, get the average review score
        review_scores = merge_two.groupby(by="seller_id").agg({"review_score":[np.mean]})
        
        #return the top 10 sellers by review scores
        return review_scores.nlargest(10,("review_score","mean"))[("review_score","mean")].rename("avg_review_score")


    def part_two(self):
        #Join order items and translations to products
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.prd_translation, how="left", on="product_category_name")
        
        #Group according to the category (english), get the number of orders in each category
        group_agg = merge_two.groupby(by="product_category_name_english").count()
        
        #Return the 10 largest categories by order volume
        return group_agg.nlargest(10,"order_id")["order_id"].rename("sales")


    def part_three(self):
        #joining order items and sellers to products
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")

        #Group according to sellers, find the revenue of each, find the 10 with highest revenue
        group_agg = merge_two.groupby(by="seller_id").agg({"price":"sum","shipping_limit_date":["max", "min"]})
        total_rev = group_agg.nlargest(10,("price","sum"))
        
        #find the no. days between the first and last order date (assumed in market for at least 1 day)
        days_between = total_rev.assign(days_between = lambda x: (pd.to_datetime(x["shipping_limit_date", "max"])-pd.to_datetime(x["shipping_limit_date", "min"]))/np.timedelta64(1,"D"))
        days_between.loc[days_between["days_between"]==0, "days_between"] = 1

        #finding daily avg revenue according to revenue/days in market
        avg_rev = days_between.assign(daily_revenue = lambda x: (x["price","sum"] / x["days_between", ""]))
        return avg_rev["daily_revenue"].rename("avg_rev_seller_day")


    def part_four(self):
        """Calculation for monthly revenue: 
        It's assumed that the minimum amount of time any seller can be in the market is 1 month. 
        This is to ensure that states with only a few days worth of orders don't end up with overinflated monthly averages

        For states with more than a months worth of orders, the months between the first and last order date is used (with the assumption that each month is 30.4 days.)
        Monthly revenue is then (total revenue) / (order period in months)
        """

        #joining order items and products to sellers
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")

        #group according to the seller state, taking revenue as sum of prices
        group_agg = merge_two.groupby(by="seller_state").agg({"price":"sum", "shipping_limit_date":["max", "min"]})
        
        #find the no. months between the first and last order date (assumed in market for at least 1 month)
        months_between = group_agg.assign(months_between = lambda x: (pd.to_datetime(x["shipping_limit_date", "max"])-pd.to_datetime(x["shipping_limit_date", "min"]))/np.timedelta64(1,"M"))
        months_between.loc[months_between["months_between"]==0, "months_between"] = 1
        
        #finding monthly revenue according to revenue/months in market per state
        monthly_revenue = months_between.assign(monthly_profit = lambda x: (x["price","sum"] / x["months_between", ""]))
        return monthly_revenue["monthly_profit"]

    #part 5: find the combination of product category and state that yields the highest profit
    def part_five(self):
        """
        As a single seller, I wouldn't be concerned about the state with highest revenue, nor the category with the highest revenue
        Instead, I'd be concerned about: 
            1. Profit (revenue - freight), for max earnings
            2. The combination of category and state with the highest profit. 
        This is to reflect that different categories have different levels of success in different states, and that sellers take home profit rather than revenue. 
        
        Strictly speaking revenue - freight isn't profit, but y'know. 
        """

        #joining order items, sellers, and translations
        merge_one = pd.merge(self.order_items, self.products, how="left", on="product_id")
        merge_two = pd.merge(merge_one, self.sellers, how="left", on="seller_id")
        merge_three = pd.merge(merge_two, self.prd_translation, how="left", on="product_category_name")

        #calculate the "profit" as the difference between price and freight value (ok it's really just revenue after delivery, not profit per se)
        add_profit = merge_three.assign(profit = lambda x: x.price - x.freight_value)

        #grouping the df according to the state and category, also calculating the first and last order dates
        #this is assuming that the monthly profit should be based on the duration that sellers were actually selling in the market
        grouped = add_profit.groupby(by=["seller_state","product_category_name_english"]).agg({"profit":"sum", "shipping_limit_date":["max", "min"]})

        #find the no. months between the first and last order date (assumed in market for at least 1 month)
        months_between = grouped.assign(months_between = lambda x: (pd.to_datetime(x["shipping_limit_date", "max"])-pd.to_datetime(x["shipping_limit_date", "min"]))/np.timedelta64(1,"M"))
        months_between.loc[months_between["months_between"]==0, "months_between"] = 1
        
        #finding monthly profit according to profit/months in market
        monthly_profit = months_between.assign(monthly_profit = lambda x: (x["profit","sum"] / x["months_between", ""]))

        #finding the most profitable combination of state and category
        return (monthly_profit["monthly_profit"].idxmax(), round(monthly_profit["monthly_profit"].max(),2))


if __name__ == "__main__":
    d = q5()
    # print(d.part_three())
    # print(d.part_four())
    print("---------part one---------")
    print(d.part_one())
    for i in range(3): print("")
    print("---------part two---------")
    print(d.part_two())
    for i in range(3): print("")
    print("---------part three---------")
    print(d.part_three())
    for i in range(3): print("")
    print("---------part four---------")
    print(d.part_four())
    for i in range(3): print("")
    print("---------part five---------")
    res = d.part_five()
    print("I'd sell " + str(res[0][1]) + " in " + str(res[0][0]) + " because it's the combination of state and product category that yields the highest monthly profit, at $" + str(res[1]))