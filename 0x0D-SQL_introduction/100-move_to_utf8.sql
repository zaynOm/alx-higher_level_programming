-- converts a database to UTF8
USE hbtn_0c_0;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mp4 COLLATE utf8mp4_unicode_ci;
