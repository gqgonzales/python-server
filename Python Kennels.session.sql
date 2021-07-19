CREATE TABLE IF NOT EXISTS `Location` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `address` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Customer` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `address` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Animal` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `status` TEXT NOT NULL,
    `breed` TEXT NOT NULL,
    `species` TEXT NOT NULL,
    `customer_id` INTEGER NOT NULL,
    `location_id` INTEGER,
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE IF NOT EXISTS `Employee` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `address` TEXT NOT NULL,
    `location_id` INTEGER NOT NULL,
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);