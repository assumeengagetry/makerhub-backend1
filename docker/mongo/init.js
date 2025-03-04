// filepath: /society-management/society-management/docker/mongo/init.js
db = db.getSiblingDB('admin');  // 切换到 admin 数据库
var rootUser = db.getUser("root")
if (!rootUser){
// 创建 root 用户
db.createUser({
    user: "root",
    pwd: "123456",
    roles: [
        { role: "root" , db: "admin"}
    ]
});
}
// 切换到应用数据库
db = db.getSiblingDB('makerhub');
