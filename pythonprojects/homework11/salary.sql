/*
 Navicat Premium Data Transfer

 Source Server         : exe
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : exe1

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 25/06/2020 23:27:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for salary
-- ----------------------------
DROP TABLE IF EXISTS `salary`;
CREATE TABLE `salary` (
  `jobname` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of salary
-- ----------------------------
BEGIN;
INSERT INTO `salary` VALUES ('Python开发工程师', '因诺（上海）资产管理有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('python开发工程师', '北京南天软件有限公司', '0.8-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师-财务报表平台', '字节跳动', '2-4万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '扬州万方电子技术有限责任公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师-北京-00113', '北软互联（北京）科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京中软融通科技有限公司', '0.7-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师---0201', '北京视野金融信息服务有限公司', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('python开发工程师-北京', '中电福富信息科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师 数据挖掘', '北京大申烽华科技有限责任公司', '6-8千/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '随锐科技集团股份有限公司', '2-2.5万/月');
INSERT INTO `salary` VALUES ('python开发工程师', '360金融', '2.5-4万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京三六九数动科技有限公司', '2-2.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '深圳市法本信息技术有限公司上海分...', '1.5-2.2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京斯普信信息技术有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京安德医智科技有限公司', '1-1.8万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京寄云鼎城科技有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '天池创新（北京）软件技术有限公司...', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '上海天玑科技股份有限公司', '0.8-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师-北京', '杭州迪普科技股份有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '沈阳信诚计算机信息技术有限公司', '1.2-1.6万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '麦田春雪科贸（北京）有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北明软件有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('python开发工程师（舆情方向）', '太极计算机股份有限公司', '1.1-1.8万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京航标时代检测认证有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '浙江华治数聚科技股份有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('高级Python开发工程师(J11448)', '朗新科技股份有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('python开发工程师', '北京永信至诚科技股份有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '深圳极联信息技术股份有限公司', '1.2-1.5万/月');
INSERT INTO `salary` VALUES ('中高级Python开发工程师 (MJ001804)', '北京启明星辰信息安全技术有限公司...', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '建信金融科技有限责任公司', '30-60万/年');
INSERT INTO `salary` VALUES ('Python开发工程师（全职/***）', '猪八戒股份有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京华文天元信息咨询有限公司', '0.8-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京友聚四海网络科技有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京凯普顿医药科技开发有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京阿拉丁立方信息技术有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京神州新桥科技有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京展云科技有限公司', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '上海微创软件股份有限公司北京分公...', '0.9-1.4万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '深圳市第一企业管理咨询有限公司', '3-4万/月');
INSERT INTO `salary` VALUES ('python开发工程师（RPA实施工程师）', '北京点点智联科技有限公司', '0.6-1万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京华泽云防科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京华路时代信息技术股份有限公司...', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京三维博特科技有限公司', '0.8-1万/月');
INSERT INTO `salary` VALUES ('python爬虫工程师（菱歌数字科技）', '北京鼎盛阳光咨询有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('python爬虫分析工程师', '北京海峰科技有限责任公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('技术新星', '神州数码信息服务股份有限公司', 'None');
INSERT INTO `salary` VALUES ('EPR开发工程师（JAVA/Python）', '紫光同芯微电子有限公司', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('Python开发', '文思海辉技术有限公司Pactera Tec...', '1-1.5万/月');
INSERT INTO `salary` VALUES ('自动化开发工程师（实习生）', '奇虎360科技有限公司', '260元/天');
INSERT INTO `salary` VALUES ('python爬虫高级开发工程师', '北京连盈科技有限公司', '1-3万/月');
INSERT INTO `salary` VALUES ('视频分析算法工程师', '中讯志远（武汉）科技有限公司', '0.8-2万/月');
INSERT INTO `salary` VALUES ('资深Python工程师', '北京安德信业信息咨询有限责任公司...', '2.5-4万/月');
INSERT INTO `salary` VALUES ('大数据挖掘工程师', '湖南金烽信息科技有限公司', '1.5-3万/月');
INSERT INTO `salary` VALUES ('安全分析开发工程师', '完美世界（北京）总部/完美时空', '1.5-2万/月');
INSERT INTO `salary` VALUES ('云BOSS', '亚信科技（中国）有限公司', '1.5-2千/月');
INSERT INTO `salary` VALUES ('后端开发工程师（Python方向）', '中金智汇科技有限责任公司', '1-2万/月');
INSERT INTO `salary` VALUES ('python工程师', '国和瑞斯（北京）科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('python开发', '深圳市捷兴电子商务有限公司', '2-3万/月');
INSERT INTO `salary` VALUES ('python开发', '上海雍米计算机科技有限公司', '2-3万/月');
INSERT INTO `salary` VALUES ('全栈开发工程师', '博彦科技股份有限公司', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('python开发', '广州华钧软件科技有限公司', '2-3万/月');
INSERT INTO `salary` VALUES ('软件工程师-数字轨道', '北京和利时系统工程有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('IT开发助理', '上海企顺信息系统有限公司', '0.8-1万/月');
INSERT INTO `salary` VALUES ('全栈工程师', '北京智谱华章科技有限公司', '2.5-5万/月');
INSERT INTO `salary` VALUES ('Python工程师', '北京先进数通信息技术股份公司', '0.6-1万/月');
INSERT INTO `salary` VALUES ('python开发', '深圳市若昕科技有限公司', '2-3万/月');
INSERT INTO `salary` VALUES ('软件开发工程师（初级）', '北京华云星地通科技有限公司', '0.8-1.1万/月');
INSERT INTO `salary` VALUES ('气象算法工程师', '北京华泰德丰技术有限公司', '1.5-3万/月');
INSERT INTO `salary` VALUES ('Python算法研发工程师一名', '北京立方天地科技发展有限责任公司...', '1-3万/月');
INSERT INTO `salary` VALUES ('诚聘Python数据工程师', '北京环球医疗救援有限责任公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('期权投资-程序化开发', '国元期货有限公司', '0.7-1.2万/月');
INSERT INTO `salary` VALUES ('德企招Python 全栈工程师', '上海科之锐人才咨询有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python爬虫工程师', '天津市淇奥科技发展有限公司', '0.8-1万/月');
INSERT INTO `salary` VALUES ('Software Designer', '埃特博朗咨询（上海）有限公司', '2-2.5万/月');
INSERT INTO `salary` VALUES ('技术架构师 (MJ002954)', '广联达', '3-5万/月');
INSERT INTO `salary` VALUES ('ZC研发工程师', '广州铁科智控有限公司', '20-40万/年');
INSERT INTO `salary` VALUES ('ERP实施顾问', '北京京航安机场工程有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('上位机软件工程师', '北京理工雷科电子信息技术有限公司...', '1.5-2万/月');
INSERT INTO `salary` VALUES ('后台研发工程师(J10343)', '纵目科技（上海）股份有限公司', '1.8-2.5万/月');
INSERT INTO `salary` VALUES ('技术研发（后端）', '北京图灵文化发展有限公司', '2.5-3.5万/月');
INSERT INTO `salary` VALUES ('Python研发工程师', '北京利和制药有限公司', '2-4万/月');
INSERT INTO `salary` VALUES ('支撑工具开发岗（北京、上海）', '联仁健康医疗大数据科技股份有限公...', 'None');
INSERT INTO `salary` VALUES ('数据挖掘工程师', '赛纳生物科技（北京）有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python高级工程师', '中包物联网科技（北京）有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python高级开发工程师', '达观数据', '2-3万/月');
INSERT INTO `salary` VALUES ('科学计算软件高级开发工程师', '北京星亢原生物科技有限公司', '1.5-3.5万/月');
INSERT INTO `salary` VALUES ('Java/Python软件工程师.', '南京拾柴信息科技有限公司', '0.8-2万/月');
INSERT INTO `salary` VALUES ('数据库云平台架构师', '北京海量数据技术股份有限公司', '1.5-3万/月');
INSERT INTO `salary` VALUES ('python课程研发老师', '达内时代科技集团有限公司', '2.5-3万/月');
INSERT INTO `salary` VALUES ('安全研发工程师', '北京华清信安科技有限公司', '0.8-1.2万/月');
INSERT INTO `salary` VALUES ('商业数据开发工程师', '理想汽车', '2-4万/月');
INSERT INTO `salary` VALUES ('资深Python工程师', '北京红铅笔广告有限公司', '1.8-3.6万/月');
INSERT INTO `salary` VALUES ('监控开发工程师', '北京泽塔云科技股份有限公司', '1.5-2万/月');
INSERT INTO `salary` VALUES ('Python网络爬虫工程师', '北京今朝在线科技有限公司', '1-1.2万/月');
INSERT INTO `salary` VALUES ('预研实习生', '北京智通云联科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('软件开发项目经理', '慧科教育科技集团有限公司', '1.8-2.6万/月');
INSERT INTO `salary` VALUES ('安全分析师/安全分析专家', '北京星网锐捷网络技术有限公司', '2.5-5万/月');
INSERT INTO `salary` VALUES ('Python研发工程师', '北京新网医讯技术有限公司', '0.8-1.2万/月');
INSERT INTO `salary` VALUES ('云计算研究员', '北京华胜天成科技股份有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('数据挖掘工程师', '北京燕昆石油科技发展有限责任公司...', '1.5-2万/月');
INSERT INTO `salary` VALUES ('后端开发工程师(J10347)', '北京创源微致软件有限公司', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('课程开发高级专员', '威盛电子（中国）有限公司', '0.7-1.4万/月');
INSERT INTO `salary` VALUES ('RPA开发工程师', '上海屹恒信息科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Django讲师', '北京八维研修学院', '1.5-2万/月');
INSERT INTO `salary` VALUES ('对象存储工程师', '广东紫晶信息存储技术股份有限公司...', '1.5-2万/月');
INSERT INTO `salary` VALUES ('高级Python后端开发工程师', '乐荐信息科技（北京）有限公司', '1.7-3万/月');
INSERT INTO `salary` VALUES ('后台开发工程师', '华录光存储研究院（大连）有限公司...', '1-2万/月');
INSERT INTO `salary` VALUES ('C++开发工程师', '中世国信（北京）信息技术有限公司...', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('python全栈开发', '北京中科基因技术有限公司', '0.7-1.2万/月');
INSERT INTO `salary` VALUES ('python软件工程师', '北京经纬恒润科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('机器人ROS开发工程师', '中国航天科工集团第二研究院206所', '18-22万/年');
INSERT INTO `salary` VALUES ('Python工程师', '马恒达（北京）信息技术服务有限公...', '1.5-2万/月');
INSERT INTO `salary` VALUES ('后端开发工程师（广告）', '北京木瓜移动科技股份有限公司', '2-2.5万/月');
INSERT INTO `salary` VALUES ('运维开发工程师', '央视国际网络有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京华泽云防科技有限公司', '3-4.5千/月');
INSERT INTO `salary` VALUES ('高级Java/Python开发工程师 （后端开发)', '上海杰迈晶雅人力资源有限公司', '1.5-2.7万/月');
INSERT INTO `salary` VALUES ('Python讲师', '湖南潭州教育网络科技有限公司北京...', '4-8千/月');
INSERT INTO `salary` VALUES ('python实习生', '北京捷报数据技术有限公司', '2-3千/月');
INSERT INTO `salary` VALUES ('python开发工程师', '字节跳动', '2-3.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师 - 变现业务', '字节跳动', '2.5-4万/月');
INSERT INTO `salary` VALUES ('python开发工程师', '杭州迪普科技股份有限公司', '10-20万/年');
INSERT INTO `salary` VALUES ('Python开发工程师', '太极计算机股份有限公司', '1.3-2.3万/月');
INSERT INTO `salary` VALUES ('python开发工程师（集成2053）', '北京南天软件有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('python开发工程师', '上海微创软件股份有限公司北京分公...', '1.2-1.6万/月');
INSERT INTO `salary` VALUES ('Python开发', '文思海辉技术有限公司Pactera Tec...', '1-1.5万/月');
INSERT INTO `salary` VALUES ('高级Devops工程师', '北京安德信业信息咨询有限责任公司...', '3-4.5万/月');
INSERT INTO `salary` VALUES ('爬虫工程师（Java或Python）', '北京三六九数动科技有限公司', '2.5-3万/月');
INSERT INTO `salary` VALUES ('Python 工程师', '北京三六九数动科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('PD-DevOps工程师', '北京安德医智科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发（情报分析平台）', '北京启明星辰信息安全技术有限公司...', '1.2-2万/月');
INSERT INTO `salary` VALUES ('python中级工程师', '中包物联网科技（北京）有限公司', '0.8-1.2万/月');
INSERT INTO `salary` VALUES ('科学计算软件开发工程师', '北京星亢原生物科技有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('Python 工程师', '北京友聚四海网络科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Nodejs开发工程师', '北京凯普顿医药科技开发有限公司', '1-2万/月');
INSERT INTO `salary` VALUES ('后端开发工程师', '北京创源微致软件有限公司', '1.5-2.5万/月');
INSERT INTO `salary` VALUES ('python软件工程师', '北京经纬恒润科技有限公司', '1-1.5万/月');
INSERT INTO `salary` VALUES ('Python开发工程师', '北京理工雷科电子信息技术有限公司...', '0.4-1.6万/月');
INSERT INTO `salary` VALUES ('Python开发工程师（实习生）', '北京华泽云防科技有限公司', '4.5-6千/月');
INSERT INTO `salary` VALUES ('python实习生', '完美世界（北京）总部/完美时空', '3-4.5千/月');
INSERT INTO `salary` VALUES ('python讲师', '湖南潭州教育网络科技有限公司北京...', '4-8千/月');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
