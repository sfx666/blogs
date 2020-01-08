# 数据模型
import datetime


from App.ext import db

# 用户基本资料
class bbs_user(db.Model):
    __tablename__ = "bbs_user"
    uid = db.Column(db.Integer(11), primary_key=True, autoincrement=True)  # 自增id
    username = db.Column(db.String(16), nullable=False)  # 帐号
    password = db.Column(db.String(256), nullable=False)  # 密码（md5加密）
    email = db.Column(db.String(32), nullable=False)  # 邮箱
    udertype = db.Column(db.Boolean(), nullable=False, default=False)  # 帐号类型
    regtime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())  # 注册时间
    lasttime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())  # 最后登录时间
    regip = db.Column(db.Integer(12), nullable=False)  # 注册IP
    picture = db.Column(db.String(256), nullable=False, default='/static/img/timg.jpeg')  # 头像
    grade = db.Column(db.Integer(10), nullable=True, default=0)  # 积分
    problem = db.Column(db.String(256), nullable=True)  # 找回密码
    result = db.Column(db.String(256), nullable=True)  # 答案
    realname = db.Column(db.String(50), nullable=True)  # 真实姓名
    sex = db.Column(db.Boolean(), nullable=True, default=False)  # 性别
    birthday = db.Column(db.String(32), nullable=True)  # 生日
    place = db.Column(db.String(64), nullable=True)  # 所在地
    qq = db.Column(db.String(16), nullable=True)  # qq号
    autograph = db.Column(db.String(512), nullable=True)  # 个人签名
    allowlogin = db.Column(db.Boolean(), nullable=False, default=False)  # 是否允许登录

# 用户黑名单
class bbs_closeip(db.Model):
    __tablename__ = "bbs_closeip"
    id = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)   # 自增id
    ip = db.Column(db.Integer(10), nullable=False)   # IP地址
    addtime = db.Column(db.Integer(10), nullable=False)   # 记录添加时间
    overtime = db.Column(db.Integer(10), nullable=True)   # IP限制结束时间

# 友情链接表
class bbs_link(db.Model):
    __tablename__ = "bbs_link"
    lid = db.Column(db.Integer(6), primary_key=True, nullable=False,autoincrement=True)  # 自增id
    displayorder = db.Column(db.Integer(2), nullable=False, default=0)  # 排序
    name = db.Column(db.String(32), nullable=False)  # 名称
    url = db.Column(db.String(256), nullable=False)  # 链接跳转地址
    description = db.Column(db.text(), nullable=True)  # 描述
    logo = db.Column(db.String(256), nullable=True)  # logo的路由地址
    addtime = db.Column(db.Integer(12), nullable=False)  # 添加时间

# 论坛版块表
class bbs_categroy(db.Model):
    __tablename__ = "bbs_categroy"
    cid = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)  # 自增id
    classname = db.Column(db.String(64), nullable=False)  # 版块名称
    parentid = db.Column(db.Integer(10), nullable=False)  # 父级ID
    classpath = db.Column(db.String(32), nullable=True)  # 关系
    replycount = db.Column(db.Integer(10), nullable=False, default=0)  # 回帖数量
    motifcount = db.Column(db.Integer(10), nullable=False, default=0)  # 帖子数量
    compers = db.Column(db.String(16), nullable=True)  # 版主
    classpic = db.Column(db.String(256), nullable=False, default='/static/img/timg.jpeg')  # 版块ICON
    description = db.Column(db.text(), nullable=True)  # 版块描述
    orderby = db.Column(db.Integer(2), nullable=False, default=0)  # 排序
    lastpost = db.Column(db.String(256), nullable=True)  # 最后发表
    namestyle = db.Column(db.String(16), nullable=True)  #
    ispass = db.Column(db.Integer(2), nullable=False, default=1)  # 审核状态


# 帖子信息表


# 帖子订单表
class bbs_order(db.Model):
    __tablename__ = "bbs_order"
    oid = db.Column(db.Integer(10), primary_key=True, nullable=False, autoincrement=True)  # 自增id
    uid = db.Column(db.Integer(11), nullable=False)  # 用户id（外键）
    tid = db.Column(db.Integer(11), nullable=False)  # 帖子id（外键）
    rate = db.Column(db.Integer(11), nullable=False)  # 价格
    addtime = db.Column(db.Integer(11), nullable=False)  # 创建时间
    ispay = db.Column(db.Boolean(), nullable=False, default=False)  # 是否支付

















