SELECT COLUMN_NAME, 
        COLUMN_TYPE,
        DATA_TYPE, 
        CHARACTER_MAXIMUM_LENGTH, 
        IS_NULLABLE, 
        COLUMN_DEFAULT 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'alx_book_store' 
AND TABLE_NAME = 'Books';
