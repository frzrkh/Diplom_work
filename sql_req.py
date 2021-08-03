import sqlite3
conn = sqlite3.connect('DataBase/db.sqlite')
cur = conn.cursor()

first_insert =  '''
INSERT INTO Users VALUES ( '{}', '{}', 'ы', 0, '')
'''
id_in_table = '''
SELECT TG_ID
FROM Users
WHERE TG_ID = '{}'
'''
update_app_lang = '''
UPDATE Users
SET App_lang = '{}'
WHERE TG_ID = '{}'
'''
app_lang_in_table= '''
SELECT App_lang
FROM Users 
WHERE TG_ID
'''
update_fullname='''
UPDATE Users
SET Fullnane = '{}'
WHERE TG_ID = '{}'
'''

fullname_in_table = '''
SELECT Fullname
FROM Users
Where TG_ID='{}'
'''
