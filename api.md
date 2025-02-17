<这里是创建的models，定义和管理数据库的结构（表格），封装了对数据的增、删、改、查操作>
#### 1.base.py

> 这个文件是其他模型的基类，所有其他模型可能会继承它以简化重复的代码。

- **字段**

`id`：自增ID

`created_at`：创建记录的时间（时间戳）

#### 2.rules.py

> 该模型对应数据库中的“规章制度”表。它用于管理社团的各类规章制度，包括文件名称、内容等信息。

- **字段**：

`id`：自增ID

`file_id`：文件唯一标识符

`file_name`：文件名称

`content`：文件内容

#### 3.user.py

> 该模型代表社团的用户信息表，用于存储用户的基本信息如邮箱、用户名、状态、积分等。

- **字段**：

`id`：自增ID

`userid`：用户邮箱

`password`：用户密码（加密存储）

`level`：用户等级（1：编外人员，2：干事，3：部长及以上）

`real``_``name`：用户名

`phone_num`：手机号

`note`：备注信息

`state`：账户状态（0：封禁，1：正常）

`profile_photo`：头像（存储为二进制数据）

`score`：用户积分

#### 4.event.py

> 该模型用于管理活动表，包含活动的ID、名称、时间、地点、描述等信息。

- **字段**：

`id`：活动记录的唯一标识符

`event_id`：活动ID

`event_name`：活动名称

`poster`：活动海报（base64编码的图片）

`description`：活动的描述

`location`：活动地点

`link`：活动相关链接（如报名链接）

`start_time`：活动开始时间

`end_time`：活动结束时间

`registration_deadline`：活动报名截止时间

`created_at`：活动创建时间

`updated_at`：活动最后更新时间

#### 5.project.py

> 该模型用于项目表，记录社团的项目申请、审核、结束等状态。

**字段**：

`id`：项目记录的唯一标识符

`apply_id`：项目申请编号

`project_name`：项目名称

`director`：项目负责人

`college`：学院名称

`major_grade`：项目负责人的专业和年级

`phone_num`：负责人电话

`email`：负责人邮箱

`mentor`：项目导师

`description`：项目描述

`application_file`：申请文件（Base64编码）

`prove_file`：证明文件（Base64编码）

`member`：项目成员（列表）

`start_time`：项目开始时间

`end_time`：项目结束时间

`audit_state`：项目审核状态（0：待审核，1：通过，2：拒绝）

`project_state`：项目状态（0：已结束，1：进行中）

`created_at`：创建时间

#### 6.3d_print.py

> 该模型用于3D打印申请表，记录社团成员的3D打印申请信息，包括申请人、打印机选择、用料量等。

**字段**：

`id`：自增ID

`apply_id`：打印申请单ID

`userid`：申请用户ID

`phone_num`：用户电话

`score`：用户积分

`score_change`：积分变化

`name`：申请人姓名

`quantity`：用料量（单位：克）

`printer`：打印机选择（0: i创街，1: 208）

`file_zip`：文件路径（存储Base64编码的ZIP文件）

`created_at`：创建时间

`updated_at`：更新时间

`state`：审核状态（0: 未审核，1: 审核通过，2: 审核未通过）

`reason`：审核理由

#### 7.task.py

> 该模型用于任务表，管理社团任务的分配、状态更新等。

**字段**：

`id`：任务记录的唯一标识符

`task_id`：任务的唯一ID

`department`：任务所属部门

`task_name`：任务名称

`name`：负责人姓名

`content`：任务详细描述

`state`：任务状态（0: 未完成，1: 已完成）

`deadline`：任务截止时间

#### 8.sites_borrow.py

> 该模型用于场地借用表，用于管理社团成员对场地的申请、审批等。

**字段**：

`id`：场地借用记录的唯一标识符

`apply_id`：借用申请编号

`name`：借用人姓名

`student_id`：学号

`phonenum`：手机号码

`email`：电子邮件

`purpose`：借用目的

`mentor_name`：指导老师姓名

`mentor_phone_num`：指导老师电话

`picture`：场地平面图（base64编码）

`start_time`：借用开始时间

`end_time`：借用结束时间

`state`：申请状态（0: 待审核，1: 审核通过，2: 审核未通过）

`reason`：审核意见

`created_at`：创建时间

`updated_at`：更新时间

#### 9.games.py

> 该模型用于赛事表，记录社团负责宣传的赛事的基本信息，包括赛事编号、名称、时间等。

- **字段**：

`id`：赛事记录的唯一标识符

`game_id`：赛事ID

`name`：赛事名称

`wx_num`：微信号

`qq_num`：QQ号

`introduction`：赛事介绍

`registration_start`：报名开始时间

`registration_end`：报名结束时间

`contest_start`：赛事开始时间

`contest_end`：赛事结束时间

`link`：赛事链接

`created_at`：创建时间

#### 10.clean.py

> 该模型用于扫除记录表，用于记录社团成员的打扫任务，包含任务内容、责任人等。

**字段**：

`id`：记录ID

`record_id`：扫除记录编号

`name`：人员姓名

`userid`：人员ID（邮箱）

`times`：扫除次数

`created_at`：创建时间

`updated_at`：最后更新时间

#### 11.publicity_link.py

> 该模型用于宣传链接表，管理社团的宣传资料链接，支持增加、删除等操作。

**字段**：

`id`：链接记录ID

`name`：提交人姓名

`userid`：提交人邮箱

`link`：秀米链接

#### 12.arrange.py

> 该模型用于排班表，记录社团成员的工作安排，包括排班时间、任务等信息。

**字段**：

`id`：安排记录ID

`name`：干事姓名

`type`：工作类型（如活动文案、公众号等）

`order`：工作顺序

#### 13.messages.py

> 该模型用于消息表，用于存储社团成员之间的通知与消息。

**字段**：

`id`：消息记录ID

`sender_id`：发送者ID

`receiver_id`：接收者ID

`content`：消息内容

`sent_at`：消息发送时间

`status`：消息状态（如已读、未读）

#### 14.duty_record.py

> 该模型用于值班记录表，用于记录社团成员的值班信息。

**字段**：

`id`：记录ID

`name`：值班人员姓名

`userid`：值班人员ID

`start_time`：值班开始时间

`end_time`：值班结束时间

`total`：值班时长（小时）

`created_at`：创建时间

#### 15.duty_apply.py

> 该模型用于值班申请表，记录社团成员的值班申请和状态。

**字段**：

`id`：申请ID

`apply_id`：申请编号

`name`：申请人姓名

`userid`：申请人ID（邮箱）

`day`：值班日期

`time_section`：值班时段（1-6）

`created_at`：创建时间

#### 16.stuff.py

> 该模型用于物资管理表，记录社团的物资信息，包括物品名称、数量、使用状态等。

**字段**：

` ``id`：物资记录的唯一标识符

`stuff_id`：物资的唯一编号

`type`：物资类型

`stuff_name`：物资名称

`number`：物资数量

`description`：物资描述

`created_at`：物资创建时间

`updated_at`：物资最后更新时间

#### 17.stuff_borrow.py

> 该模型用于物品借用表，记录社团成员的物品借用情况，包括借用人、借用时间、借用物品等。

字段：

`id`：借用记录ID

`sb_id`：借物编号

`userid`：借用人邮箱

`name`：借用人姓名

`phone_num`：借用人电话

`email`：借用人邮箱

`grade`：借用人年级

`major`：借用人专业

`project_num`：项目编号

`type`：物品类型

`stuff_name`：物品名称

`stuff_quantity_change`：物品数量变化（负数表示借出）

`deadline`：归还截止时间

`reason`：借用原因

`categories`：借物类别（0个人，1团队）

`state`：审核状态（0未审核，1已审核）



<这里将简要描述每个API的路由和作用。>

1. users.py
- 描述：用于处理与用户相关的所有API请求，包括用户注册、登录等功能。
2. rules.py
- 描述：提供社团的规章制度相关的API接口，支持增、删、改、查。
3. events.py
- 描述：管理社团活动的API接口，处理活动的创建、查询和管理。
4. projects.py
- 描述：管理项目立项的API接口，处理项目的创建、查询和管理。
5. 3dprint.py
- 描述：处理与3D打印机相关的API，主要用于提交打印申请、查询历史记录等。
6. tasks.py
- 描述：管理社团任务的API接口，支持任务的创建、分配、状态更新等操作。
7. stuff_borrow.py
- 描述：管理物品借用相关的API，记录物品的借用和归还。
8. stuff.py
- 描述：管理社团物资的API接口，记录社团拥有的物品、库存等信息。
9. site_borrow.py
- 描述：管理场地借用的API接口，处理场地申请、审批等功能。
10. games.py
- 描述：管理社团赛事相关的API接口，处理比赛的创建、查询等。
11. clean.py
- 描述：管理社团的清洁任务，记录并分配清扫任务。
12. publicity_link.py
- 描述：管理社团宣传资料的链接，存储和更新宣传内容。
13. arrange.py
- 描述：管理社团成员的排班安排。
14. messages.py
- 描述：管理社团成员之间的消息和通知。
15. duty_record.py
- 描述：记录社团成员的值班信息。
16. duty_apply.py
- 描述：处理值班申请，成员可以申请参与值班。
17. stuff.py
- 描述：处理物资类别、数量管理。
18. stuff_borrow.py
- 描述：处理借物申请，借物审核等。