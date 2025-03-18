/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - filmidustry
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`filmidustry` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `filmidustry`;

/*Table structure for table `applications` */

DROP TABLE IF EXISTS `applications`;

CREATE TABLE `applications` (
  `applicant_id` int(200) NOT NULL AUTO_INCREMENT,
  `vacancy_id` int(200) DEFAULT NULL,
  `sender_id` int(200) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `resume` varchar(200) DEFAULT NULL,
  `portfolio_link` varchar(200) DEFAULT NULL,
  `applied_date` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`applicant_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `applications` */

insert  into `applications`(`applicant_id`,`vacancy_id`,`sender_id`,`name`,`email`,`phone`,`resume`,`portfolio_link`,`applied_date`,`status`) values 
(1,NULL,1,'Malavika','malavikat2004@gmail.com','+915566774488','static/appli_imgs358a80e7-80d8-4e1d-9a18-bb4d41ebeac6IMG-20250225-WA0014.jpg','https://github.com/','2025-02-28','pending');

/*Table structure for table `audition` */

DROP TABLE IF EXISTS `audition`;

CREATE TABLE `audition` (
  `audition_id` int(11) NOT NULL AUTO_INCREMENT,
  `fm_id` int(11) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `audition_date` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `time_to_reach` varchar(200) DEFAULT NULL,
  `requirements` varchar(200) DEFAULT NULL,
  `deadline` varchar(200) DEFAULT NULL,
  `contact_number` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`audition_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `audition` */

insert  into `audition`(`audition_id`,`fm_id`,`title`,`description`,`audition_date`,`location`,`time_to_reach`,`requirements`,`deadline`,`contact_number`) values 
(1,1,'new actor','audition for lead rrole actor for new movie','2025-02-15','ernakulam','10:00','an acting degree or shortfilm acted ','2025-03-20','+916677554455');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`description`,`reply`,`date`) values 
(3,1,'site is not loading','pending','2025-02-28'),
(4,1,'site is bugged','pending','2025-02-28');

/*Table structure for table `entertainmententities` */

DROP TABLE IF EXISTS `entertainmententities`;

CREATE TABLE `entertainmententities` (
  `ee_id` int(11) NOT NULL AUTO_INCREMENT,
  `entity_type` varchar(200) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `website_link` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `established_date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ee_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `entertainmententities` */

insert  into `entertainmententities`(`ee_id`,`entity_type`,`name`,`location`,`phone`,`email`,`website_link`,`description`,`established_date`) values 
(2,'muisc','kavitha','kannur','+915566774488','someone@gmail.com','https://foolhardy-welcome.com','an music event conducted as part of  childerns day','2025-02-14');

/*Table structure for table `feature_member` */

DROP TABLE IF EXISTS `feature_member`;

CREATE TABLE `feature_member` (
  `fm_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `prefession` varchar(200) DEFAULT NULL,
  `file` varchar(200) DEFAULT NULL,
  `biography_description` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`fm_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feature_member` */

insert  into `feature_member`(`fm_id`,`fname`,`phone`,`prefession`,`file`,`biography_description`,`email`,`login_id`) values 
(1,'malavika','9946702029','writer','static/feature_files/535f879f-9b70-4ee4-bc0b-6c5d674beea9images.png','a writer looking for creating new stories','tmalavika333@gmail.com',2);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(200) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL,
  `usertype` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`Username`,`Password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'Malavika','Malu@123','feature_members'),
(3,'Malavika','Ammu@123','normal_members');

/*Table structure for table `normal_members` */

DROP TABLE IF EXISTS `normal_members`;

CREATE TABLE `normal_members` (
  `nm_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `professional_intrest` varchar(200) DEFAULT NULL,
  `skills` varchar(200) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nm_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `normal_members` */

insert  into `normal_members`(`nm_id`,`fname`,`phone`,`email`,`image`,`professional_intrest`,`skills`,`login_id`) values 
(1,'Malavika','+918877668899','malavikat2004@gmail.com','static/norm_imgsbae34014-d189-4b4c-9ec8-6d0a8f87620bEo_circle_brown_number-1.svg.png','director','screen play writing',3);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date_time` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`title`,`description`,`date_time`) values 
(1,'audio release','the audio release of new movie','2025-02-20T11:00');

/*Table structure for table `portfolio` */

DROP TABLE IF EXISTS `portfolio`;

CREATE TABLE `portfolio` (
  `portfolio_id` int(11) NOT NULL AUTO_INCREMENT,
  `nm_id` int(11) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `image_video` varchar(200) DEFAULT NULL,
  `achivements` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`portfolio_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `portfolio` */

insert  into `portfolio`(`portfolio_id`,`nm_id`,`title`,`image_video`,`achivements`,`date`) values 
(1,1,'editor','static/portfolio/326662f8-7bfd-41fa-a437-1170eec72664Pin by Emma Young on Nursing wall _ Study motivation inspiration, Medical school inspiration, Study motivation.jpg','sima awards','2025-02-14');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `fm_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `review` varchar(200) DEFAULT NULL,
  `rating` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`fm_id`,`sender_id`,`review`,`rating`,`date`) values 
(5,1,1,'nice writer','3','2025-02-28');

/*Table structure for table `vacancy` */

DROP TABLE IF EXISTS `vacancy`;

CREATE TABLE `vacancy` (
  `vacancy_id` int(200) NOT NULL AUTO_INCREMENT,
  `fm_id` int(200) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `required_skills` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `employment_type` varchar(200) DEFAULT NULL,
  `experience_req` varchar(200) DEFAULT NULL,
  `deadline` varchar(200) DEFAULT NULL,
  `contact_mail` varchar(200) DEFAULT NULL,
  `contact_num` varchar(200) DEFAULT NULL,
  `slots` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`vacancy_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vacancy` */

insert  into `vacancy`(`vacancy_id`,`fm_id`,`title`,`description`,`category`,`required_skills`,`location`,`employment_type`,`experience_req`,`deadline`,`contact_mail`,`contact_num`,`slots`) values 
(1,1,'editor','need spot editors','editor','editing','thrissur','seasonal','2 years','2025-02-18','anyone@gmail.com','+916655774433','6');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
