/*
 Navicat Premium Data Transfer

 Source Server         : my_machine
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : 127.0.0.1:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 10/04/2019 20:08:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for person
-- ----------------------------
DROP TABLE IF EXISTS `person`;
CREATE TABLE `person`  (
  `id` int(1) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of person
-- ----------------------------
INSERT INTO `person` VALUES (1, '冯宝宝', 120);
INSERT INTO `person` VALUES (2, '东方月初', 18);
INSERT INTO `person` VALUES (3, '红狐', 400);
INSERT INTO `person` VALUES (4, '张楚岚', 21);
INSERT INTO `person` VALUES (5, '白狐', 5000);
INSERT INTO `person` VALUES (6, '九尾狐', 5000);
INSERT INTO `person` VALUES (7, '狐狸精', 5000);
INSERT INTO `person` VALUES (8, '月华', 5000);
INSERT INTO `person` VALUES (9, '想你', 2018);
INSERT INTO `person` VALUES (10, '都是你', 2018);
INSERT INTO `person` VALUES (11, '爱你', 2018);
INSERT INTO `person` VALUES (12, '想你', 2018);

SET FOREIGN_KEY_CHECKS = 1;
