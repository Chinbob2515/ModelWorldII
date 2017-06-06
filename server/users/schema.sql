
CREATE TABLE IF NOT EXISTS `users` (
	`id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
	`username` varchar(128) NOT NULL UNIQUE,
	`password` varchar(128) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `races` (
	`id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
	`name` varchar(128) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `entities` (
	`id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
	`name` varchar(128),
	`owner` int(11) NOT NULL,
	`race` int(11) NOT NULL,
	`code` text,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`owner`) REFERENCES users(`id`),
	FOREIGN KEY (`race`) REFERENCES races(`id`)
) ENGINE=InnoDB;


INSERT IGNORE INTO `users` (username, password) VALUES ('world', '');

INSERT IGNORE INTO `races` (name) VALUES ('Dwarf')

