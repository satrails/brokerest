brokeREST
=========

Python REST client



Usage
-----

    from brokerest.resources import RestlessModel
	from brokerest.errors import ObjectNotFound

    class User(RestlessModel):
	
    	@classmethod
        def request(cls, method, url, params=None, headers=None, data=None):
            url = config.REST_SERVER + url
    		return RestlessModel.request(method, url, params=params, headers=headers, data=data)
			
			
	try:
		user = User.get(1)
		
	except ObjectNotFound:
		print 'element not found'
		
	user = User.find.filter_by(name='John').all()
	user = User.find.filter_by(name='John').one()


more soon ..