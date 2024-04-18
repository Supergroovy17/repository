#1. Product Review Analysis


#reviewed in class 


reviews =  ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

def review_highlight(reviews):
    key_words=["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing","bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    for review in reviews:
        for kw in key_words:
            review = review.replace(kw, kw.upper())
            review = review.replace(kw.title(),kw.upper())
        
        print(review)

review_highlight(reviews)
