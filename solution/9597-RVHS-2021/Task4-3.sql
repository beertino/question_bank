SElECT Name, Contact, VehicleType, StartDate, ReturnDate, DailyPrice
FROM RentalRecord
JOIN CAR ON RentalRecord.VIN = Car.VIN
JOIN Customer ON Customer.CustomerID = RentalRecord.CustomerID
WHERE Customer.Name = "Goh Yi Xi"
ORDER BY StartDate ASC