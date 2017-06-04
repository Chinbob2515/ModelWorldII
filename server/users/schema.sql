
CREATE TABLE IF NOT EXISTS `users` (
	`id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
	`username` varchar(128) NOT NULL UNIQUE,
	`password` varchar(128) NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `entities` (
	`id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
	`owner` int(11) NOT NULL UNIQUE,
	`race` varchar(128) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`owner`) REFERENCES users(`id`)
) ENGINE=InnoDB;

INSERT INTO users (username, password) VALUES ('world', '');
