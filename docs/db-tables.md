# SQLLite Database Tables

* Users (UserID, Username, PasswordHash, Name, JoinDate)
* Buildings (BuildingID, UserID, Building Name, Building Address, Number of Apartments, Number of Renters)
* Apartments (ApartmentID, BuildingID, Apartment Number, Vacant Or Not, Store or Not, Extra Info )
* Renters (RenterID, ApartmentID, Name, Phone Number, Phone Number 2, Lease Start, Lease End, Lease Term, Balance, Extra Info)
* Rent Payments (RenterID, Month, Expense, Payment, Nullify)
* Extra Payments (RenterID, Name, Expense, Payment, Nullify)

