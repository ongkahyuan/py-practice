1. From 1 to 100,000 count all the palindromic prime and save them in a list. 
   - e.g., 2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919...
2. From 1 to 100,000, given two numbers, find all the numbers between those two which are palindromic prime after removing one digit. 
   - e.g., 115 and 130, then the answer should be 115, 116, 117, 118, 119, 121.
3. Count the frequency of each word in an article, print out the top 10 words with frequency, and print out the sentence where the top 10 words appeared for the first and last time. 
   - e.g., [{"keyword": "the", "frequency": 5, "first_time": "It’s a story about people believing what they want to believe, even when there’s evidence to the contrary.", "last_time": "Marjorie Nugent, my mother’s sister and, depending on whom you ask, the meanest woman in East Texas."}].
4. Perform a GET request on "https://dev.beepbeep.tech/v1/sample_customer", the data returned from the API should have the structure below. Print the list of promotions sorted by their titles in descending alphabetical order. 
```
{
	"name": "(str)",
	"email": "(str)", 
	"promotions": [
		{
			"title": "(str)",
			"quantity": (int),
			"type": "discount",
			"discount": (float)
		},
 		{
			"title": "(str)",
			 "quantity": (int), 
			 "type": "redeem"
		}
	]
}
```
   

5. Using the information in the data directory, solve the following:
   1. List the top 10 sellers with the highest review score.
   2. Calculate the top 10 product categories with the highest sales and show their english name.
   3. Count the daily average revenue by the top 10 sellers with the highest total revenue.
   4. Count the monthly revenue in each seller state.
   5. If you are a seller, what kind of products you will sell? Where are you going to open your store? And why?
