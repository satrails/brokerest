brokeREST
=========

Python REST API client

- extends standard dictionaries returned from requests into user defined generic objects
- handle get, find, create, edit and delete requests
- enable sub-objects, and sub-objects of sub-objects, and so on..
- enable custom properties and methods in objects
- easy to override request method with custom headers
- throw readable errors ObjectNotFound, RequestError, IntegrityError, AccessError, MethodError


Usage example
-------------

Assume REST API structure with two related objects:

    http://example.com/api/book
	http://example.com/api/author
	http://example.com/api/author/<id>/books


It does'n metter if subobjects (author's books) are returned in same request od not. Code to handle that would look like:


    from brokerest.resources import RestlessModel
	from brokerest.errors import ObjectNotFound

    class OurApiModel(RestlessModel):
	
    	@classmethod
        def request(cls, method, url, params=None, headers=None, data=None):
			# add here any specific request headers and variables
			url = config.REST_SERVER + url
    		return RestlessModel.request(method, url, params=params, headers=headers, data=data)
			
	
	class Book(OurApiModel):
		pass
		
	class Author(OurApiModel):
		
		inline_models = {'books': Book}
		
		@property
		def name(self):
			return self.first_name + ' ' + self.last_name

	
	try:
		# browse
		author = Author.find.filter_by(last_name='Shakespeare').one()
		print author.name
		for book in author.books:
			print book.title
		
		# add
		new_author = Author()
		new_author.first_name = 'Joseph'
		new_author.last_name - 'Conrad'
		new_author.save()
		
		# edit
		old_author = Author.get(new_author.id)
		old_author.first_name = 'Konrad'
		old_author.last_name - 'Korzeniowski'
		old_author.save()
		
		# delete
		authors = Author.find.filter_by(first_name='William').all()
		for author in authors:
			author.delete()
		
	except Author.ObjectNotFound:
		print 'element not found'
		


more soon ..