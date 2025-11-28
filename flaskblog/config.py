class Config:
    # This key is required for Flask sessions and security
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' 
    
    # This sets up the SQLAlchemy database to use the sqlite file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
    # We are adding this now for the pagination feature!
    POSTS_PER_PAGE = 5