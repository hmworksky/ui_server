create table user_login(
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `username` varchar(30) NOT NULL DEFAULT '' COMMENT '用户名',
    `password` varchar(30) NOT NULL DEFAULT '' COMMENT '密码',
    `nickname` varchar(30)  DEFAULT '' COMMENT '昵称',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COMMENT='用户登录表';


create table generate_data_log(
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `request_id` varchar(30) NOT NULL DEFAULT '' COMMENT '用户名',
    `device` varchar(30) NOT NULL DEFAULT '' COMMENT '设备号',
    `env` varchar(30)  DEFAULT 'test' COMMENT '环境',
    `send_type` varchar(30)  DEFAULT '' COMMENT '发送类型',
    `message` varchar(200)  DEFAULT '' COMMENT '发送的命令',
    `status` int  DEFAULT 0 COMMENT '状态，0：初始状态，1：已连接服务器，2：认证完成，3：发送命令完成',
    `memo` varchar(2000)  DEFAULT '' COMMENT '描述信息',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COMMENT='发送日志表';

alter table generate_data_log add interval_time int COMMENT '发送间隔';
alter table generate_data_log add send_count int COMMENT '发送总数';
alter table generate_data_log add create_time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间';
alter table generate_data_log add update_time datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间';
alter table generate_data_log add current_send_num int COMMENT '当前已发送';


create table app(
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `app_name` varchar(30) NOT NULL DEFAULT '' COMMENT 'App名字',
    `package_name` varchar(30) NOT NULL DEFAULT '' COMMENT '包名',
    `memo` varchar(200)  DEFAULT '' COMMENT '描述信息',
    `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COMMENT='App应用管理';

create table page(
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `app_name` varchar(30) NOT NULL DEFAULT '' COMMENT 'App名字',
    `page_name` varchar(30) NOT NULL DEFAULT '' COMMENT '页面名字',
    `memo` varchar(200)  DEFAULT '' COMMENT '描述信息',
    `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COMMENT='App页面管理';


create table `app_element`(
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `app_name` varchar(30) NOT NULL DEFAULT '' COMMENT 'App名字',
    `page_name` varchar(30) NOT NULL DEFAULT '' COMMENT '页面名字',
    `element_name` varchar(30) NOT NULL DEFAULT '' COMMENT '元素名称',
    `memo` varchar(200)  DEFAULT '' COMMENT '元素描述',
    `find_type` int  DEFAULT 0 COMMENT '查找类型',
    `find_value` varchar(500)  DEFAULT '' COMMENT '查找值',
    `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COMMENT='App元素管理';



