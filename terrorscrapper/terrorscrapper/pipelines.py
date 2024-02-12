# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime


class TerrorscrapperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        ## Strip all whitespaces from strings
        tuple_cat = ['url', 'image_url', 'dob', 'reward']
        for field_name in tuple_cat:
            value = adapter.get(field_name)
            if value == (None,) or value == []:
                adapter[field_name] = "null"
            else:    
                adapter[field_name] = value[0].strip()
        
        list_cat = ['title', 'about', 'associated_location', 'associated_organization']
        for cat in list_cat:
            value = adapter.get(cat)
            if value == ([],):
                adapter[cat] = "null"
            else:    
                adapter[cat] = value[0][0].strip()
        # char = {"\u00a0" : "", "\u2018": "‘", "\u2018":"’"}
                
        reward_cat = ['reward']
        for reward in reward_cat:    
            value = adapter.get(reward)
            adapter[reward] = value[6:]
        
        date_cat = ['dob']
        from datetime import datetime

        for dob in date_cat:
            value = adapter.get(dob)
            print("Original value:", value)  # Debugging output
            if value == "null":
                adapter[dob] = "null"
            elif ";" in value:
                try:
                    first_date = value.split(";")[0].strip()
                    date_object = datetime.strptime(first_date, '%B %d, %Y')
                    adapter[dob] = date_object.date().isoformat()
                except ValueError:
                    try:    
                        date_object = date_object = datetime.strptime(first_date, '%Y')
                        adapter[dob] = date_object.date().isoformat()
                    except ValueError:
                        adapter[dob] = value
                    
            elif "to" in value:
                try:
                    first_date = value.split("to")[0].strip()
                    date_object = datetime.strptime(first_date, '%B %d, %Y')
                    # print(date_object)
                    adapter[dob] = date_object.date().isoformat()
                except ValueError:
                    try:    
                        date_object = date_object = datetime.strptime(first_date, '%Y')
                        adapter[dob] = date_object.date().isoformat()
                    except ValueError:
                        adapter[dob] = value

            elif len(value) == 4:
                try:
                    date_object = datetime.strptime(value, '%Y')
                    adapter[dob] = date_object.date().isoformat()
                except ValueError:
                    adapter[dob] = value

            elif "or" or "Circa" or "and" or "Approximately" or "," in value:
                last_date = value.split(" ")[-1].strip()
                date_object = datetime.strptime(last_date, '%Y')
                adapter[dob] = date_object.date().isoformat()
            
            else:
                try:
                    date_object = datetime.strptime(value, '%B %d, %Y')
                    adapter[dob] = date_object.date().isoformat()
                except ValueError:
                    date_object = datetime.strptime(value, '%B %Y')
                    adapter[dob] = date_object.date().isoformat()
        return item