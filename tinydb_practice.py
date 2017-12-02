from tinydb import TinyDB, Query

db = TinyDB('db_practice.json')

def main():
    db.insert({'type':'apple', 'count':7})

main()
