from itemadapter import ItemAdapter
import re
from decimal import Decimal
from scrapy.exceptions import DropItem

class ModifyPricePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('price'):
            clean_price = re.sub(r'[^0-9.,]', '', str(adapter['price']).strip())
            clean_price = clean_price.replace(',', '.')
            adapter['price'] = Decimal(clean_price)
            return item 
        else:
            raise DropItem(f"Missing price in {item}")

class ModifyReviewsCountPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('reviews_count'):
            clean_reviews_count = re.sub(r'[^0-9]', '', str(adapter['reviews_count']))
            adapter['reviews_count'] = int(clean_reviews_count)
            return item 
        else:
            raise DropItem(f"Missing Review Count in {item}")
        
class ModifyReviewsScorePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('reviews_score'):
            clean_reviews_score = str(adapter['reviews_score']).strip()
            adapter['reviews_score'] = Decimal(clean_reviews_score)
            return item 
        else:
            raise DropItem(f"Missing Review Score in {item}")