/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - student_perfom
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`student_perfom` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `student_perfom`;

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(20) DEFAULT NULL,
  `sem_duration` varchar(10) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`course_name`,`sem_duration`,`dept_id`) values 
(4,'Computer Science','3',1),
(5,'Computer Science','1',5),
(6,'Physics','1',5),
(7,'BioChemistry','1',5);

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `dept` */

insert  into `dept`(`dept_id`,`dept_name`) values 
(1,'BSc'),
(6,'BCom');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fed_id` int(11) NOT NULL AUTO_INCREMENT,
  `std_id` int(11) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `dates` date DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`fed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fed_id`,`std_id`,`sub_id`,`feedback`,`dates`,`rating`) values 
(1,18,4,'TextEditingController#744b3(TextEditingValue(text: ?Good?, selection: TextSelection.collapsed(offset','2023-01-21',1),
(2,34,2,'Goodggggg','2023-01-21',1),
(3,3,0,'','2023-02-11',2),
(4,3,0,'','2023-02-11',2),
(5,3,0,'','2023-02-11',2),
(6,3,0,'','2023-02-11',2),
(7,3,0,'','2023-02-11',2),
(8,3,1,'gd','2023-02-11',2),
(9,3,1,'gd','2023-02-11',2),
(10,0,0,'\"+feedback+\"','2023-02-11',0),
(11,3,1,'gd','2023-02-11',2),
(12,3,1,'gd','2023-02-11',2),
(13,3,1,'g','2023-02-11',2),
(14,3,1,'g','2023-02-11',2),
(15,3,1,'g','2023-02-11',2),
(16,3,1,'g','2023-02-11',2),
(17,3,1,'g','2023-02-11',2),
(18,3,1,'g','2023-02-11',2),
(19,3,1,'g','2023-02-11',2),
(20,3,2,'gd','2023-02-11',5),
(21,3,4,'gd','2023-02-18',4),
(22,3,1,'good','2023-02-18',5),
(23,3,1,'good','2023-02-18',2),
(24,3,1,'good','2023-02-18',2),
(25,3,1,'good','2023-02-18',3),
(26,3,1,'good','2023-02-18',3),
(27,3,0,'very bad ','2023-02-18',1),
(28,3,0,'very bad ','2023-02-18',5),
(29,3,0,'very bad ','2023-02-18',1);

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `met_id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_id` int(11) DEFAULT NULL,
  `file_name` varchar(25) DEFAULT NULL,
  `date_of_upld` date DEFAULT NULL,
  PRIMARY KEY (`met_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `files` */

insert  into `files`(`met_id`,`sub_id`,`file_name`,`date_of_upld`) values 
(1,4,'static/files/abc.pdf','2023-04-03');

/*Table structure for table `hod` */

DROP TABLE IF EXISTS `hod`;

CREATE TABLE `hod` (
  `hod_id` int(11) NOT NULL AUTO_INCREMENT,
  `teach_lid` int(11) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`hod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `hod` */

insert  into `hod`(`hod_id`,`teach_lid`,`dept_id`) values 
(1,2,1);

/*Table structure for table `hod_notification` */

DROP TABLE IF EXISTS `hod_notification`;

CREATE TABLE `hod_notification` (
  `hod_notif_id` int(15) NOT NULL AUTO_INCREMENT,
  `teach_lid` varchar(30) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`hod_notif_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `hod_notification` */

insert  into `hod_notification`(`hod_notif_id`,`teach_lid`,`notification`,`date`) values 
(1,NULL,'\"++\"','2023-02-19'),
(4,'2','hi','2023-03-06'),
(6,'2','hlo','2023-03-06'),
(7,'2','hi','2023-03-06'),
(9,'2','hi new','2023-04-08'),
(10,'2','hbh','2023-04-08'),
(11,'2','hbh','2023-04-08'),
(12,'2','hbh','2023-04-08'),
(13,'2','hbh','2023-04-08'),
(14,'2','test notification ','2023-04-08'),
(15,'2','test notification ','2023-04-08'),
(16,'2','test notification ','2023-04-08'),
(17,'2','test notification ','2023-04-08'),
(18,'2','test notification ','2023-04-08'),
(19,'2','ok','2023-04-08'),
(20,'2','ok','2023-04-08'),
(21,'2','','2023-04-08'),
(22,'2','ok','2023-04-08'),
(23,'2','ok','2023-04-08'),
(24,'2','','2023-04-08');

/*Table structure for table `internal_mark` */

DROP TABLE IF EXISTS `internal_mark`;

CREATE TABLE `internal_mark` (
  `int_mrk_id` int(11) NOT NULL AUTO_INCREMENT,
  `std_id` int(11) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  `test_mrk` int(11) DEFAULT NULL,
  `semi_mrk` int(11) DEFAULT NULL,
  `assignt_mrk` int(11) DEFAULT NULL,
  `att_mrk` int(11) DEFAULT NULL,
  `total` float NOT NULL,
  `grade` varchar(5) NOT NULL,
  PRIMARY KEY (`int_mrk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `internal_mark` */

insert  into `internal_mark`(`int_mrk_id`,`std_id`,`sub_id`,`test_mrk`,`semi_mrk`,`assignt_mrk`,`att_mrk`,`total`,`grade`) values 
(1,18,4,13,7,10,70,100,'B');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `type` varchar(15) NOT NULL,
  PRIMARY KEY (`Log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Log_id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'hod','111','hod'),
(3,'abc','123','student'),
(4,'abc','345','parent'),
(5,'shabeeb','8129','student'),
(6,'hashim','7593','teacher'),
(7,'','',''),
(8,'bfjf@gmail.com','37389999','student'),
(9,'hh','hh','parent'),
(10,'bfjf@gmail.com','37389999','student'),
(11,'hh','hh','parent'),
(12,'bfjf@gmail.com','37389999','student'),
(13,'hh','hh','parent'),
(14,'bfjf@gmail.com','37389999','student'),
(15,'hh','hh','parent'),
(16,'bfjf@gmail.com','37389999','student'),
(17,'hh','hh','parent'),
(18,'b','b','student'),
(19,'h','gg','parent'),
(20,'b','b','student'),
(21,'h','gg','parent'),
(22,'b','b','student'),
(23,'h','gg','parent'),
(24,'b','b','student'),
(25,'h','gg','parent'),
(26,'midhilesh@gmail','111','student'),
(27,'abc@mail','333','parent'),
(28,'sh@gmail.com','72635737','pending'),
(29,'skc@gmail.com','737363627','parent'),
(30,'shabu@gmail.com','7363738526','pending'),
(31,'hag@gmail.com','9267886377','parent'),
(32,'shabu@gmail.com','7363738526','pending'),
(33,'hag@gmail.com','9267886377','parent'),
(34,'shabu@gmail.com','7363738526','student'),
(35,'hag@gmail.com','9267886377','parent'),
(36,'shabu@gmail.com','7363738526','pending'),
(37,'hag@gmail.com','9267886377','parent'),
(38,'shabu@gmail.com','7363738526','pending'),
(39,'hag@gmail.com','9267886377','parent'),
(40,'shabu@gmail.com','7363738526','pending'),
(41,'hag@gmail.com','9267886377','parent');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notif_id` int(11) NOT NULL AUTO_INCREMENT,
  `notif_date` varchar(15) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notif_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notif_id`,`notif_date`,`notification`) values 
(1,'2022-11-12','dfsdgfds'),
(7,'2022-12-09','Hi All'),
(8,'2023-02-11','\"++\"');

/*Table structure for table `staff_att` */

DROP TABLE IF EXISTS `staff_att`;

CREATE TABLE `staff_att` (
  `staff_att_id` int(11) NOT NULL AUTO_INCREMENT,
  `dates` date DEFAULT NULL,
  `teach_id` int(11) DEFAULT NULL,
  `check_in_time` varchar(7) DEFAULT NULL,
  `check_out_time` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`staff_att_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff_att` */

insert  into `staff_att`(`staff_att_id`,`dates`,`teach_id`,`check_in_time`,`check_out_time`) values 
(1,'2023-04-03',2,'11:30','1:10');

/*Table structure for table `std_attendence` */

DROP TABLE IF EXISTS `std_attendence`;

CREATE TABLE `std_attendence` (
  `std_att_id` int(11) NOT NULL AUTO_INCREMENT,
  `std_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `hours` int(11) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`std_att_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `std_attendence` */

insert  into `std_attendence`(`std_att_id`,`std_id`,`date`,`hours`,`status`) values 
(1,26,'2023-01-19',5,'absent'),
(2,26,'2023-01-19',4,'present');

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `Std_id` int(11) NOT NULL AUTO_INCREMENT,
  `std_lid` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `bld_grp` varchar(5) NOT NULL,
  `H_name` varchar(25) NOT NULL,
  `place` varchar(20) NOT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `Admn_no` int(11) DEFAULT NULL,
  `Reg_no` varchar(15) DEFAULT NULL,
  `Parent_name` varchar(20) DEFAULT NULL,
  `parent_ph` varchar(15) DEFAULT NULL,
  `parent_job` varchar(20) DEFAULT NULL,
  `parent_mail` varchar(20) DEFAULT NULL,
  `Std_ph` varchar(15) DEFAULT NULL,
  `dob` varchar(12) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `sem` int(11) DEFAULT NULL,
  `prev_schl` varchar(20) DEFAULT NULL,
  `cast` varchar(15) DEFAULT NULL,
  `religion` varchar(15) DEFAULT NULL,
  `prev_mark` int(11) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `parent_lid` varchar(30) DEFAULT NULL,
  `Std_mail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Std_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`Std_id`,`std_lid`,`name`,`bld_grp`,`H_name`,`place`,`city`,`state`,`pin`,`Admn_no`,`Reg_no`,`Parent_name`,`parent_ph`,`parent_job`,`parent_mail`,`Std_ph`,`dob`,`course_id`,`sem`,`prev_schl`,`cast`,`religion`,`prev_mark`,`status`,`photo`,`parent_lid`,`Std_mail`) values 
(5,18,'Midhilesh','A','new','kannur','kannur','kerala',670666,12345,'7777','mama','9988776655','eng','abc@mail','8111849900','1891-05-01',4,1,'khss','cast','rel',90,'approved','/static/student/20230211-134215.jpg','27','midhilesh@gmail'),
(9,34,'Shabeeb','B','KC','Velleri','Malappuram','Kerala',673639,2745,'RCAUSCS008','Sk','737363627','Cooli','skc@gmail.com','72635737','0000-00-00',0,6,'PPMHSS','Islam','Mappila',73,'approved','/static/student/20230211-134215.jpg','35','sh@gmail.com');

/*Table structure for table `sub` */

DROP TABLE IF EXISTS `sub`;

CREATE TABLE `sub` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_name` varchar(20) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `sem` int(11) DEFAULT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `sub` */

insert  into `sub`(`sub_id`,`sub_name`,`course_id`,`sem`) values 
(2,'Statistics 1',4,1),
(4,'Mathematics 1',4,1);

/*Table structure for table `sub_allocation` */

DROP TABLE IF EXISTS `sub_allocation`;

CREATE TABLE `sub_allocation` (
  `sub_allo_id` int(11) NOT NULL AUTO_INCREMENT,
  `teach_id` int(11) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sub_allo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `sub_allocation` */

insert  into `sub_allocation`(`sub_allo_id`,`teach_id`,`sub_id`) values 
(1,2,4),
(2,2,2),
(3,2,0),
(4,2,0);

/*Table structure for table `teachers` */

DROP TABLE IF EXISTS `teachers`;

CREATE TABLE `teachers` (
  `teach_id` int(11) NOT NULL AUTO_INCREMENT,
  `Teach_lid` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `dept_id` int(11) NOT NULL,
  `dob` date NOT NULL,
  `qualification` varchar(25) NOT NULL,
  `h_name` varchar(25) NOT NULL,
  `place` varchar(15) NOT NULL,
  `city` varchar(15) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `pin` int(7) NOT NULL,
  `ph_no` varchar(15) NOT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`teach_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `teachers` */

insert  into `teachers`(`teach_id`,`Teach_lid`,`name`,`dept_id`,`dob`,`qualification`,`h_name`,`place`,`city`,`state`,`pin`,`ph_no`,`photo`,`email`,`district`,`post`) values 
(2,1,'has',1,'2022-12-06','mca','gf','','','',0,'11223344','/static/teacher_image/20221206-131714.jpg','abcd@gmail.com','',''),
(4,2,'has',1,'2022-12-06','mca','gf','gdss','','',66,'','/static/teacher_image/20221206-131059.jpg','','','gfd');

/*Table structure for table `time_table` */

DROP TABLE IF EXISTS `time_table`;

CREATE TABLE `time_table` (
  `time_t_id` int(11) NOT NULL AUTO_INCREMENT,
  `time_t_hrs` int(11) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  `days` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`time_t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `time_table` */

insert  into `time_table`(`time_t_id`,`time_t_hrs`,`sub_id`,`days`) values 
(1,0,0,'\" + days + \"'),
(2,0,0,''),
(3,3,2,'monday ');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
