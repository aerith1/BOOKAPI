import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_sqlalchemy import SQLAlchemy
# from models.library import LibraryModel
from create_table import LibraryModel
engine = create_engine('mysql+mysqlconnector://root:root@101.132.17.102:3306/cit')
Base = declarative_base()

# 创建一个会话工厂
Session = sessionmaker(bind=engine)
session = Session()

# class PicBedModel(db.Model):
#     __tablename__='PicBed'
#     png_id = db.Column(db.String(20), primary_key=True)
#     book_id = db.Column(db.Integer)
#     png_link = db.Column(db.String(200))

# new_pic = PicBedModel(
#     png_id = 1,
#     book_id = 1,
#     png_link = 'https://cit-oss-2023-12-10.oss-cn-shanghai.aliyuncs.com/maid.jpg'
# )

new_book = LibraryModel(
    book_name='无职转生3',
    author='LYW',
    introduction='Book Introduction',
    average_score=4.5,
    Cover_link = 'https://cit-oss-2023-12-10.oss-cn-shanghai.aliyuncs.com/maid.jpg',
    amount_book=1
)

session.add(new_book)

session.commit()
session.close()

print('Finish')