
CREATE TABLE IF NOT EXISTS `users` (
	`id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
	`username` varchar(128) NOT NULL UNIQUE,
	`password` varchar(128) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;
