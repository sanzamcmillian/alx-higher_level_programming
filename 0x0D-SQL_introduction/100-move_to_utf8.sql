-- Converts the entire database hbtn_0c_0 to UTFS
ALTER database hbtn_oc_c CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER table first_table CONVERT TO CHARACTER SET utf8mb4_unicode_ci;