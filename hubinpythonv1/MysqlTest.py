from sqlalchemy import Column, String,DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(32), primary_key=True)
    user_name = Column(String(64))
    user_type = Column(String(16))
    status = Column(String(16))
    password = Column(String(64))
    last_login_time = Column(DateTime)
    create_time = Column(DateTime)
    modify_time = Column(DateTime)

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://bdm296810582:172252156@bdm296810582.my3w.com/bdm296810582_db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id==1).one()
allUsers = session.query(User).filter()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.user_name)
# 关闭Session:
session.close()