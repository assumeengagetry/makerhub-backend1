// filepath: /society-management/society-management/docker/mongo/init.js

// 创建数据库
db = db.getSiblingDB('society_db');

// 创建集合
db.createCollection('users');
db.createCollection('rules');
db.createCollection('events');
db.createCollection('projects');
db.createCollection('print_jobs');
db.createCollection('tasks');
db.createCollection('sites_borrow');
db.createCollection('games');
db.createCollection('clean_records');
db.createCollection('publicity_links');
db.createCollection('arrangements');
db.createCollection('messages');
db.createCollection('duty_records');
db.createCollection('duty_applications');
db.createCollection('stuff');
db.createCollection('stuff_borrow');

// 创建索引
db.users.createIndex({ "userid": 1 }, { unique: true });
db.users.createIndex({ "phone_num": 1 });

db.events.createIndex({ "event_id": 1 }, { unique: true });
db.events.createIndex({ "created_at": -1 });

db.projects.createIndex({ "apply_id": 1 }, { unique: true });
db.projects.createIndex({ "director": 1 });

db.print_jobs.createIndex({ "apply_id": 1 }, { unique: true });
db.print_jobs.createIndex({ "userid": 1 });

db.tasks.createIndex({ "task_id": 1 }, { unique: true });
db.tasks.createIndex({ "deadline": 1 });

db.sites_borrow.createIndex({ "apply_id": 1 }, { unique: true });
db.sites_borrow.createIndex({ "start_time": 1 });

db.games.createIndex({ "game_id": 1 }, { unique: true });

db.messages.createIndex({ "sender_id": 1 });
db.messages.createIndex({ "receiver_id": 1 });
db.messages.createIndex({ "sent_at": -1 });

db.duty_records.createIndex({ "userid": 1 });
db.duty_records.createIndex({ "start_time": 1 });

db.duty_applications.createIndex({ "apply_id": 1 }, { unique: true });
db.duty_applications.createIndex({ "userid": 1 });

db.stuff.createIndex({ "stuff_id": 1 }, { unique: true });
db.stuff.createIndex({ "type": 1 });

db.stuff_borrow.createIndex({ "sb_id": 1 }, { unique: true });
db.stuff_borrow.createIndex({ "userid": 1 });

// 创建管理员用户
db.users.insertOne({
    userid: "xsk13969662263@outlook.com",
    password: "_assume060801Xsk_", // 
    level: 3,
    real_name: "管理员",
    phone_num: "15192018057",
    state: 1,
    score: 100,
    created_at: new Date()
});
