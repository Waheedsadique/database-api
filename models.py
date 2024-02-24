from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

# country models

class CountryBase(SQLModel):
    country_name : str = Field(unique = True )

class Country(CountryBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    country_users: list["User"] = Relationship(back_populates="country")
    

class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase):
    id : int

class CountryUpdate(CountryBase):
    country_name : Optional[str]

# pin models

class PinBase(SQLModel):
    pin : str = Field(unique = True)

class Pin(PinBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    pin_users : list["User"] = Relationship(back_populates="pin")

class PinCreate(PinBase):
    pass

class PinRead(PinBase):
    id : int

class PinUpdate(PinBase):
    pin : Optional[str]

# city models

class CityBase(SQLModel):
    city_name : str = Field(unique = True)

class City(CityBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    city_users : list["User"] = Relationship(back_populates="city")

class CityCreate(CityBase):
    pass

class CityRead(CityBase):
    id : int

class CityUpdate(CityBase):
    city_name : Optional[str]

# package models

class PackageBase(SQLModel):
    package_name : str = Field(unique = True)

class Package(PackageBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    package_users : list["User"] = Relationship(back_populates="package")

class PackageCreate(PackageBase):
    pass

class PackageRead(PackageBase):
    id : int

class PackageUpdate(PackageBase):
    package_name : Optional[str]

# role models

class RoleBase(SQLModel):
    role_name : str = Field(unique = True)

class Role(RoleBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    role_users : list["User"] = Relationship(back_populates="role")

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id : int

class RoleUpdate(RoleBase):
    role_name : Optional[str]

# referral models

class ReferralBase(SQLModel):
    referral_name : str = Field(unique = True)

class Referral(ReferralBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    referral_users : list["User"] = Relationship(back_populates="referral")

class ReferralCreate(ReferralBase):
    pass

class ReferralRead(ReferralBase):
    id : int

class ReferralUpdate(ReferralBase):
    referral_name : Optional[str]

# withdraw models

class WithdrawBase(SQLModel):
    withdraw_name : str = Field(unique = True)

class Withdraw(WithdrawBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    withdraw_users : list["User"] = Relationship(back_populates="withdraw")

class WithdrawCreate(WithdrawBase):
    pass

class WithdrawRead(WithdrawBase):
    id : int

class WithdrawUpdate(WithdrawBase):
    withdraw_name : Optional[str]


# user models

class UserBase(SQLModel):
    nation_id : str
    email : str = Field(unique = True )
    password : str
    phone : str
    currency : str
    created_at: str = Field(default_factory=datetime.now().isoformat)
    updated_at: str = Field(default_factory=datetime.now().isoformat)
    country_id : Optional[int] = Field(default=None, foreign_key="country.id")
    pin_id : Optional[int] = Field(default=None, foreign_key="pin.id")
    city_id : Optional[int] = Field(default=None, foreign_key="city.id")
    package_id : Optional[int] = Field(default=None, foreign_key="package.id")
    role_id : Optional[int] = Field(default=None, foreign_key="role.id")
    referral_id : Optional[int] = Field(default=None, foreign_key="referral.id")
    withdraw_id : Optional[int] = Field(default=None, foreign_key="withdraw.id")
    
  





class User(UserBase , table = True):
    id : Optional[int] = Field(default = None , primary_key = True)
    country: Optional["Country"] = Relationship(back_populates="country_users")
    pin: Optional["Pin"] = Relationship(back_populates="pin_users")
    city: Optional["City"] = Relationship(back_populates="city_users")
    package: Optional["Package"] = Relationship(back_populates="package_users")
    role: Optional["Role"] = Relationship(back_populates="role_users")
    referral: Optional["Referral"] = Relationship(back_populates="referral_users")
    withdraw: Optional["Withdraw"] = Relationship(back_populates="withdraw_users")

    

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id : int


class UserUpdate(UserBase):
   pass


class UserReadWithAll(UserRead):
    country : CountryRead
    pin : PinRead
    city : CityRead
    package : PackageRead
    role : RoleRead
    referral : ReferralRead
    withdraw : WithdrawRead

