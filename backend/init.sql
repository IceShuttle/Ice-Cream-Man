USE SHOP;

CREATE TABLE IF NOT EXISTS ITEMS (
  ID INT NOT NULL AUTO_INCREMENT,
  ITEM_NAME VARCHAR(255) NOT NULL,
  SP FLOAT NOT NULL,
  QUANTITY INT NOT NULL DEFAULT 0,
  PRIMARY KEY(ID)
);

CREATE TABLE IF NOT EXISTS ORDERS (
  ORDER_ID INT AUTO_INCREMENT,
  CUSTOMER_NAME VARCHAR(255),
  CUSTOMER_NO CHAR(10),
  ORDER_DATE DATE NOT NULL,
  AMOUNT FLOAT NOT NULL,
  PRIMARY KEY(ORDER_ID)
);

CREATE TABLE IF NOT EXISTS ORDER_ITEMS (
  SNO INT AUTO_INCREMENT,
  ORDER_ID INT,
  ID INT NOT NULL,
  QUANTITY INT NOT NULL,
  PRIMARY KEY(SNO),
  FOREIGN KEY(ORDER_ID) REFERENCES ORDERS(ORDER_ID),
  FOREIGN KEY(ID) REFERENCES ITEMS(ID)
);

CREATE TABLE IF NOT EXISTS BOUGHT (
  ID INT NOT NULL,
  QUANTITY INT NOT NULL,
  FOREIGN KEY(ID) REFERENCES ITEMS(ID)
);

CREATE TABLE IF NOT EXISTS EXP_ITEMS (
  ID INT NOT NULL,
  QUANTITY INT NOT NULL,
  FOREIGN KEY(ID) REFERENCES ITEMS(ID)
);

CREATE TABLE IF NOT EXISTS DAILY_REPORT (
  REPORT_DATE DATE NOT NULL,
  OPENNING BLOB,
  CLOSING BLOB,
  PRIMARY KEY(REPORT_DATE)
);
