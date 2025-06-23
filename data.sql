create database data;
use data;

CREATE TABLE cleaned_data (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10, 2),
    CustomerID INT,
    Country VARCHAR(100)
);

SELECT 
    Description, 
    Country,
    COUNT(*) AS total_orders,
    SUM(Quantity) AS total_quantity,
    SUM(UnitPrice * Quantity) AS total_revenue
FROM cleaned_data
GROUP BY Description, Country
ORDER BY total_orders DESC;



