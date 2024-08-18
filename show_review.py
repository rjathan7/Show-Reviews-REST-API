from pyairtable import Api

api_key = 'patXclSEZ8TUdw8TU.9770ba6c593be4e1f08395d84d9c44ba62411462798fd45fdecee162634ef585'
base_id = 'app3o6d8wTFJInMNk'
table_id = 'tbljh7jgmnHjf0ZS7'

class ShowReview:
    def __init__(self):
        self.api = Api(api_key)
        self.table = self.api.table('app3o6d8wTFJInMNk', 'tbljh7jgmnHjf0ZS7') 

    def get_show_ratings(self, sort="ASC", max_records=10):
        if not sort:
            return self.table.all(max_records=max_records)
        elif sort == "ASC":
            rating = ["Rating"]
        elif sort == "DESC":
            rating = ["-Rating"]
        
        table = self.table.all(sort=rating, max_records=max_records)
        return table

    def add_show_rating(self, show_title, show_rating, notes=None):
        fields = {'Show': show_title, 'Rating': show_rating, 'Notes': notes}
        self.table.create(fields=fields)


# if __name__ == '__main__':
#     sr = ShowReview()
#     sr.add_show_rating('Naruto', 9)
#     get_show_ratings = sr.get_show_ratings()
#     print(get_show_ratings)